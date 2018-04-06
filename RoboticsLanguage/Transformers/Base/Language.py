# -*- coding: utf-8 -*-
#
#   This is the Robotics Language compiler
#
#   Language.py: Definitions of the base language
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

from RoboticsLanguage.Base.Types import singleString, singleReal, singleInteger, singleNatural, manyStrings, manyExpressions, manyCodeBlocks, codeBlock, anything
from RoboticsLanguage.Base.Types import returnNothing, returnCodeBlock

# temp
language = {
    # base types
    'Reals': {
        'definition': {
            'optionalArguments': {'bits': singleInteger},
            'optionalDefaults': {'bits': 32},
            'argumentTypes': anything,
            'returnType': returnNothing
        },
        'input':
        {
            'RoL':
            {
              'alternatives': ['ℝ']
            }
        },
        'output':
        {
            'HTMLDocumentation': 'Real',
            'HTMLGUI': 'Real',
            'RoL': 'Reals',
        },
        'localisation':
        {
            'pt': 'real'
        },
        'documentation':
        {
            'title': 'Real numbers type',
            'description': 'A type representing real numbers. Assumptions on the number of bits used by the compiler to represent a real number is given as information in the editor.',
            'usage': 'x in Reals'
        }
    },
    'Integers': {
        'definition': {
            'optionalArguments': {'bits': singleInteger},
            'optionalDefaults': {'bits': 32},
            'argumentTypes': anything,
            'returnType': returnNothing
        },
        'input':
        {
          'RoL':
          {
              'alternatives': ['ℤ']
          }
        },
        'output':
        {
            'HTMLDocumentation': 'Integer',
            'HTMLGUI': 'Integer',
            'RoL': 'Integers',
        },
        'localisation':
        {
            'pt': 'inteiro'
        },
        'documentation':
        {
            'title': 'Integer numbers type',
            'description': 'A type representing integer numbers. Assumptions on the number of bits used by the compiler to represent an integer number is given as information in the editor.',
            'usage': 'x in Integers'
        }

    },
    'Naturals': {
        'definition': {
            'optionalArguments': {'bits': singleNatural},
            'optionalDefaults': {'bits': 32},
            'argumentTypes': anything,
            'returnType': returnNothing
        },
        'input':
        {
          'RoL':
          {
              'alternatives': ['ℕ']
          }
        },
        'output':
        {
            'HTMLDocumentation': 'Natural',
            'HTMLGUI': 'Natural',
            'RoL': 'Naturals',
        },
        'localisation':
        {
            'pt': 'natural'
        },
        'documentation':
        {
            'title': 'Natural numbers type',
            'description': 'A type representing natural numbers. Assumptions on the number of bits used by the compiler to represent an natural number is given as information in the editor.',
            'usage': 'x in Naturals'
        }

    },
    'Strings': {
        'definition': {
            'argumentTypes': anything,
            'returnType': returnNothing
        },
        'output':
        {
            'HTMLDocumentation': 'String',
            'HTMLGUI': 'String',
            'RoL': 'Strings',
        },
        'localisation':
        {
            'pt': 'texto'
        },
        'documentation':
        {


        }
    },
    'Booleans': {
        'definition': {
            'argumentTypes': anything,
            'returnType': returnNothing
        },
        'input':
        {
            # 'RoL':
            # {
            #     'prefix': ['Booleans', '𝔹']
            # }
        },
        'output':
        {
            'HTMLDocumentation': 'Boolean',
            'HTMLGUI': 'Boolean',
            'RoL': 'Booleans',
        },
        'localisation':
        {
            'pt': 'boleano'
        },
        'documentation':
        {
        }
    },

    'Signals': {
            'output':
            {
            },
            'localisation':
            {
                'pt': 'sinal'
            },
            'documentation':
            {
                'title': 'A time or event based signal',
                'description': 'Defines a signal type.',
                'usage': 'x in Signals(Reals,rostopic:\'/test/signal\')'
            }
    },

    'string': {
        'output':
        {
            'RosCpp': '"{{text}}"',
            'HTMLDocumentation': '{{text}}',
            'HTMLGUI': '{{text}}',
            'RoL': '"{{text}}"',
        },
        'localisation':
        {
            'pt': 'texto'
        },
        'documentation':
        {
        }
    },


    'integer': {
        'output':
        {
            'RosCpp': 'int({{text}})',
            'HTMLDocumentation': '{{text}}',
            'HTMLGUI': '{{text}}',
            'RoL': '{{text}}',
        },
        'localisation':
        {
            'pt': 'inteiro'
        },
        'documentation':
        {
        }
    },
    'natural': {
        'output':
        {
            'RosCpp': 'uint({{text}})',
            'HTMLDocumentation': '{{text}}',
            'HTMLGUI': '{{text}}',
            'RoL': '{{text}}',
        },
        'localisation':
        {
            'pt': 'natural'
        },
        'documentation':
        {
        }
    },

    'boolean': {
        'output':
        {
            'RosCpp': '{{text}}',
            'HTMLDocumentation': '{{text}}',
            'HTMLGUI': '{{text}}',
            'RoL': '{{text}}',
        },
        'localisation':
        {
        },
        'documentation':
        {
        }
    },



    'real': {
        'output':
        {
            'RosCpp': 'float({{text}})',
            'HTMLDocumentation': '{{text}}',
            'HTMLGUI': '{{text}}',
            'RoL': '{{text}}',
        },
        'localisation':
        {
            'pt': 'real'
        },
        'documentation':
        {
        }
    },

    # special types
    'vector': {
        'input': {
            'RoL': {
                'bracket': {'open':'[',
                            'close':']',
                          'arguments': 'values'}
            }
        },
        'output':
        {
        },
        'localisation':
        {
            'pt': 'vector'
        },
        'documentation':
        {
        }
    },

    'set': {
        'input': {
            'RoL': {
                'bracket': {'open':'{',
                            'close':'}',
                          'arguments': 'values'}
            }
        },
        'output':
        {
          'RosCpp':'{% if parentTag=="assign"%}tie({{children|join(", ")}}){% else %}set({{children|join(", ")}}){% endif %}'
        },
        'localisation':
        {
            'pt': 'conjunto'
        },
        'documentation':
        {
        }
    },

    'associativeArray': {
        'input': {
            'RoL': {
                'bracket': {'open':'{',
                            'close':'}',
                          'arguments': 'keyValues'}
            }
        },
        'output': {
        },
        'localisation':
        {
        },
        'documentation':
        {
            'title': 'Set',
            'description': 'A set of values',
            'usage': 'a = { b, c ,d }'
        }
    },




    # base elements

    'function': {
        'definition': {
            'argumentTypes': anything,
            'returnType': returnNothing
        },
        'output':
        {
            'RosCpp': '{{attributes["name"]}}({{children|join(", ")}})',
        },
        'documentation':
        {
        }
    },

    'return': {
        'definition': {
            'argumentTypes': anything,
            'returnType': returnNothing
        },
        'output':
        {
          'RosCpp':'{% if children|length==1 %}return {{children|first}}{% else %}return std::make_tuple({{children|join(", ")}}){% endif %}'
        },
        'localisation':
        {
        },
        'documentation':
        {
        }
    },

    'functionDefinition': {
        'definition': {
            'argumentTypes': anything,
            'returnType': returnNothing
        },
        'output':
        {
            'RosCpp': '{% set returns = attribute(xpaths(code,"returns"),"RosCpp") %}{% if returns=="" %}void{% else %}{{returns}}{% endif %} {{attributes["name"]}}({{attribute(xpaths(code,"arguments"),"RosCpp")}})',
        },
        'documentation':
        {
        }
    },

    'arguments': {
        'definition': {
            'argumentTypes': anything,
            'returnType': returnNothing
        },
        'output':
        {
            'RosCpp': '{{children|join(", ")}}',
        },
        'documentation':
        {
        }
    },

    'content': {
        'definition': {
            'argumentTypes': anything,
            'returnType': returnNothing
        },
        'output':
        {
            'RosCpp': '{{children|join(";\n")}}',
        },
        'documentation':
        {
        }
    },

    'returns': {
        'definition': {
            'argumentTypes': anything,
            'returnType': returnNothing
        },
        'output':
        {
            'RosCpp': '{% if children|length==0 %}void{% elif children|length==1 %}{{children|first}}{% else %}std::tuple<{{children|join(", ")}}>{% endif %}',
        },
        'documentation':
        {
        }
    },


    'variable': {
        'definition': {
            'argumentTypes': anything,
            'returnType': returnNothing
        },
        'output':
        {
            'RosCpp': '{{attributes["name"]}}',
            'HTMLDocumentation': '{{attributes["name"]}}',
            'HTMLGUI': '{{attributes["name"]}}',
            'RoL': '{{attributes["name"]}}',
        },
        'localisation':
        {
            'pt': 'variável'
        },
        'documentation':
        {
        }
    },

    'option': {
        'output':
        {
        },
        'localisation':
        {
            'pt': 'parâmetro'
        },
        'documentation':
        {
        }
    },

    # 'name': {
    #     'output':
    #     {
    #     },
    #     'localisation':
    #     {
    #         'pt': 'parâmetro'
    #     },
    #     'documentation':
    #     {
    #     }
    # },

    'element': {
            'definition': {
                'argumentTypes': anything,
                'returnType': returnNothing
            },
        'input': {
            'RoL': {
                'infix': { 'key':['in', '∈'],
                'order': 150 }
            }
        },
        'output':
        {
          'RosCpp':'{{children[1]}} {{attribute(code.xpath("variable"),"name")}}'
        },
        'localisation':
        {
            'pt': 'elemento'
        },
        'documentation':
        {
            'title': 'Element of a set of type',
            'description': 'Defines a variable to be an element of a set or a type. If a set is provided, then the variable takes the type of the elements of the set',
            'usage': 'x in Reals'
        }
    },

    'defineFunction': {
            'definition': {
                'argumentTypes': anything,
                'returnType': returnNothing
            },
        'input': {
            },
        'output':
        {
        },
        'localisation':
        {
        },
        'documentation':
        {
        }
    },


    #
    # 'functionDefinition': {
    #     'input': {
    #         'RoL': {
    #             'custom': ['define', ':', '->', ',', '->', '']
    #         }
    #     },
    #     'output':
    #     {
    #         'RosCpp': 'function({{children|join(",")}})',
    #         'HTMLDocumentation': '{{text}}',
    #         'HTMLGUI': '{{text}}',
    #         'RoL': '{{text}}',
    #     },
    #     'localisation':
    #     {
    #         'pt': 'definirFunção'
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    'block': {
        'definition': {
            'argumentTypes': anything,
            'returnType': returnCodeBlock
        },
        'output':
        {
        'RosCpp':'{{";\n".join(children)}}'
        },
        'localisation':
        {
        },
        'documentation':
        {
        }
    },

    'anything': {
        'definition': {
            'argumentTypes': anything,
            'returnType': returnNothing
        },
        'output':
        {
        },
        'localisation':
        {
        },
        'documentation':
        {
        }
    },

    # main structures
    'node': {
        'definition': {
            'optionalArguments': {'name': singleString,
                                  'rate': singleReal,
                                  'initialise': anything,
                                  'finalise': anything,
                                  'definitions': anything },
            'optionalDefaults': {'name': 'unnamed',
                                 'rate': 1,
                                 'initialise':'',
                                 'finalise':'',
                                 'definitions':''},
            'argumentTypes': anything,
            'returnType': returnNothing
        },
        'output':
        {
        },
        'localisation':
        {
            'pt': 'nó',
            'el': 'κόμβος'
        },
        'documentation':
        {
            'title': 'The main software node',
            'description': 'This is the main RoL node. Definitions, initialisation, events, etc., are defined here.',
            'usage': 'node(\n  name:"hello world",\n  initialise(print("hello world"))\n)'
        }
    },
    # 'initialise': {
    #     'definition': {
    #         'argumentTypes': manyExpressions,
    #         'returnType': returnCodeBlock
    #     },
    #     'output':
    #     {
    #         'RosCpp': '{{children|join(";\n")}};\n',
    #         'HTMLDocumentation': '{{children|first}}',
    #         'HTMLGUI': '{{children|first}}',
    #         'RoL': '{{children|first}}',
    #     },
    #     'localisation':
    #     {
    #         'pt': 'inicializar',
    #         'el': 'αρχικοποίηση',
    #         'nl': 'initialiseren'
    #     },
    #     'documentation':
    #     {
    #     }
    # },

    # 'finalise': {
    #     'output':
    #     {
    #         'RosCpp': '{{children|join(";\n")}};\n',
    #         'HTMLDocumentation': '{{children|first}}',
    #         'HTMLGUI': '{{children|first}}',
    #         'RoL': '{{children|first}}',
    #     },
    #     'localisation':
    #     {
    #         'pt': 'finalizar'
    #     },
    #     'documentation':
    #     {
    #     }
    # },


    'cycle': {
        'output':
        {
            'RosCpp': '{{children|join(";\n")}};\n',
            'HTMLDocumentation': '{{children|first}}',
            'HTMLGUI': '{{children|first}}',
            'RoL': '{{children|first}}',
        },
        'localisation':
        {
            'pt': 'repetir'
        },
        'documentation':
        {
        }
    },

    # 'definitions': {
    #     'output':
    #     {
    #         'RosCpp': '{{children|join(";\n")}};\n',
    #         'HTMLDocumentation': '{{children|first}}',
    #         'HTMLGUI': '{{children|first}}',
    #         'RoL': '{{children|first}}',
    #     },
    #     'localisation':
    #     {
    #         'pt': 'definicoes'
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    'events': {
        'output':
        {
        },
        'localisation':
        {
            'pt': 'eventos'
        },
        'documentation':
        {
        }
    },

    'Event': {
        'output':
        {
        },
        'localisation':
        {
            'pt': 'eventos'
        },
        'documentation':
        {
        }
    },

    'Time': {
        'output':
        {
        },
        'localisation':
        {
            'pt': 'eventos'
        },
        'documentation':
        {
        }
    },

    # special keywords
    'print': {
        'definition': {
            'optionalArguments': {'level': singleString},
            'optionalDefaults': {'level': 'info'},
            'argumentTypes': manyStrings,
            'returnType': returnNothing
        },
        'output':
        {
            'RosCpp': 'ROS_INFO_STREAM({{children|first}})',
            'HTMLDocumentation': 'print({{children|first}})',
            'HTMLGUI': '',
            'RoL': 'print({{children|first}})',
        },
        'localisation':
        {
            'pt': 'imprimir',
            'el': 'εκτύπωσε',
            'nl': 'afdrukken'
        },
        'documentation':
        {
        }
    },

    'if': {
        'output':
        {
        },
        'localisation':
        {
            'pt': 'se',
        },
        'documentation':
        {
        }
    },


    #
    # # special keywords
    # 'shortComment': {
    #     'output':
    #     {
    #         'RosCpp': '/* {{text}} */',
    #         'HTMLDocumentation': 'print({{children|first}})',
    #         'HTMLGUI': '',
    #         'RoL': '# {{text}}',
    #     },
    #     'localisation':
    #     {
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # # special keywords
    # 'longComment': {
    #     'output':
    #     {
    #         'RosCpp': 'ROS_INFO({{children|first}})',
    #         'HTMLDocumentation': 'print({{children|first}})',
    #         'HTMLGUI': '',
    #         'RoL': 'print({{children|first}})',
    #     },
    #     'localisation':
    #     {
    #     },
    #     'documentation':
    #     {
    #     }
    # },


}
