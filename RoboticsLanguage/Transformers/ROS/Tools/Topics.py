#
#   This is the Robotics Language compiler
#
#   Topics.py: Processes all code for Ros topics, messages and types
#
#   Created on: June 22, 2017
#       Author: Gabriel A. D. Lopes
#      Licence: Apache 2.0
#    Copyright: 2014-2017 Robot Care Systems BV, The Hague, The Netherlands. All rights reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import dpath.util
from RoboticsLanguage.Base import Utilities

ros_type_mapping = {
    'Booleans': 'Bool',
    'Reals32': 'Float32',
    'Reals64': 'Float64',
    'Integers8': 'Int8',
    'Integers16': 'Int16',
    'Integers32': 'Int32',
    'Integers64': 'Int64',
    'Naturals8': 'UInt8',
    'Naturals16': 'UInt16',
    'Naturals32': 'UInt32',
    'Naturals64': 'UInt64',
    'Strings': 'String',
}

cpp_type_mapping = {
    'Booleans': 'bool',
    'Reals32': 'float',
    'Reals64': 'double',
    'Integers8': 'int8_t',
    'Integers16': 'int16_t',
    'Integers32': 'int32_t',
    'Integers64': 'int64_t',
    'Naturals8': 'uint8_t',
    'Naturals16': 'uint16_t',
    'Naturals32': 'uint32_t',
    'Naturals64': 'uint64_t',
    'Strings': 'string',
}


def getFlow(signal, variable, code):

  # get options
  topic_name = signal.xpath('option[@name="rosTopic"]')[0].getchildren()[0].text
  flow = signal.xpath('option[@name="rosFlow"]')[0].getchildren()[0].text

  # look for assignments:
  assignments = code.xpath(
      '//assign/variable[@name="' + variable + '" and count(preceding-sibling::*)=0]|//assign/domain[count(preceding-sibling::*)=0]/variable[@name="' + variable + '" and  count(preceding-sibling::*)=0]')
  assigned = len(assignments) > 0

  # find all instances of the variable except of its definitions
  all = code.xpath('//variable[@name="' + variable + '" and not(parent::element)]')

  # also find domain names with matching variable names
  matching_name_in_domain = code.xpath(
      '//variable[@name="' + variable + '" and (parent::domain) and count(preceding-sibling::*)>0]')

  # usages are the oposite of assignments
  usages = [x for x in all if x not in assignments]

  # also make sure to remove matching names in a domain
  usages = [x for x in usages if x not in matching_name_in_domain]
  used = len(usages) > 0

  # figure out the type of flow
  flow = 'outgoing' if assigned and not used else flow
  flow = 'incoming' if not assigned and used else flow
  flow = 'bidirectional' if assigned and used else flow

  # save flow on code structure
  code.xpath('//element/variable[@name="' + variable + '"]/../Signals/option[@name="rosFlow"]/string')[0].text = flow

  return flow, usages, assignments, topic_name


def setPublish(variable, flow, assignments):
  # if flow is outgoing or bidirectional find all assignments and add a publishing function
  if flow in ['outgoing', 'bidirectional']:
    for variable_element in assignments:
      assignment = Utilities.getFirstParent(variable_element, 'assign')

      if 'postRosCpp' not in assignment.attrib.keys():
        assignment.attrib['postRosCpp'] = ''

      assignment.attrib['postRosCpp'] += ';' + variable + '_publisher.publish(' + variable + ');'


def checkTypes(signal, variable, assignments, usages, code, parameters):

  # check if signal is using a default type instead of a ros type
  if signal.xpath('option[@name="rosType"]/string')[0].text == '':

    # Tell every assignment with this variable in the left side to use to data domain
    for element in assignments:
      Utilities.getFirstParent(element, 'assign').attrib['preAssignRosCpp'] = '.data'

    # Tell all usages not with a domain parent to use data domain
    for use in usages:
      # if use.getparent().tag != 'domain':
      use.attrib['returnDomainRosCpp'] = '.data'

    # get the type of the signal
    topic_type = signal.getchildren()[0]

    # Find the type for the topic
    if topic_type.tag in ['Reals', 'Integers', 'Naturals']:

      # default value for bits
      bits = '32'

      # try to get the specified bits parameter
      for option in topic_type.xpath('option[@name="bits"]'):
        bits = option.getchildren()[0].text

      ros_type = 'std_msgs::' + ros_type_mapping[topic_type.tag + bits]
      cpp_type = cpp_type_mapping[topic_type.tag + bits]

    elif topic_type.tag in ['Booleans', 'Strings']:
      ros_type = 'std_msgs::' + ros_type_mapping[topic_type.tag]
      cpp_type = cpp_type_mapping[topic_type.tag]

    else:
      # @REFACTOR just a placeholder for now
      ros_type = 'std_msgs::Empty'
      cpp_type = 'int'
  else:
    ros_type = signal.xpath('option[@name="rosType"]/string')[0].text.replace('/', '::')
    cpp_type = ros_type

  return code, parameters, ros_type, cpp_type


def process(code, parameters):
  '''Processes all the ROS topics in the RoL code'''

  parameters['Transformers']['ROS']['topicDefinitions'] = []

  # for each signal in definitions with rostopic
  for signal in code.xpath('/node/option[@name="definitions"]/*//element/Signals/option[@name="rosTopic"]/string[text()!=""]/../..'):

    # get the parent element to extract the variable name
    variable = signal.getparent().xpath('variable/@name')[0]

    # get flow, usages and assignments of the variable
    flow, usages, assignments, topic_name = getFlow(signal, variable, code)

    # if flow is outgoing or bidirectional add a publishing function to all assignments
    setPublish(variable, flow, assignments)

    # check types and make sure .data is added when needed
    code, parameters, ros_type, cpp_type = checkTypes(signal, variable, assignments, usages, code, parameters)

    # Save the variable name on the `Signals` tag. Helps simplifying code
    signal.attrib['ROSvariable'] = variable

    # save type in base/variables
    parameters['Transformers']['Base']['variables'][variable]['type'] = ros_type

    # add header file for msg
    parameters['Outputs']['RosCpp']['globalIncludes'].add(ros_type.replace('::', '/') + '.h')

    # save the topic definitions
    parameters['Transformers']['ROS']['topicDefinitions'].append({'variable': variable,
                                                                  'ros_type': ros_type,
                                                                  'cpp_type': cpp_type,
                                                                  'topic_name': topic_name,
                                                                  'flow': flow})

  return code, parameters
