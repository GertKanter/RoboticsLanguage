#
#   This is the Robotics Language compiler
#
#   Language.py: Definition of the language for this package
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

default_output = ''

language = {

    'Reals': {
        'output':
        {
            'RosCpp': '{% if "option" in childrenTags %}{% if option(code,"bits").text == "64"%}double{% else %}float{% endif %}{% else %}float{% endif %}',
        },
    },

    'Integers': {
        'output':
        {
            'RosCpp': 'int{% if "option" in childrenTags %}{{option(code,"bits").text}}{% else %}32{% endif %}_t',
        },
    },

    'Naturals': {
        'output':
        {
            'RosCpp': 'uint{% if "option" in childrenTags %}{{option(code,"bits").text}}{% else %}32{% endif %}_t',
        },
    },

    'Strings': {
        'output':
        {
            'RosCpp': 'std::string',
        },
    },

    'Booleans': {
        'output':
        {
            'RosCpp': 'bool',
        },
    },

    'string': {
        'output':
        {
            'RosCpp': '"{{text}}"',
        },
    },

    'integer': {
        'output':
        {
            'RosCpp': '{% if parameters["Outputs"]["RosCpp"]["strict"] %}int({{text}}){% else %}{{text}}{% endif %}',
        },
    },

    'natural': {
        'output':
        {
            'RosCpp': '{% if parameters["Outputs"]["RosCpp"]["strict"] %}uint({{text}}){% else %}{{text}}{% endif %}',
        },
    },

    'boolean': {
        'output':
        {
            'RosCpp': '{{text}}',
        },
    },

    'real': {
        'output':
        {
            'RosCpp': '{% if parameters["Outputs"]["RosCpp"]["strict"] %}double({{text}}){% else %}{{text}}{% endif %}',
        },
    },

}
