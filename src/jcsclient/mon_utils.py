# Copyright (c) 2016 Jiocloud.com, Inc. or its affiliates.  All Rights Reserved
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#

from jcsclient import utils

def populate_monitoring_params_from_args(params, args):
    """After the argparser has processed args, populate the
       params dict, processing the given args for mitoring.

       param params: a dict to save the processed args

       param args: Namespace object where args are saved

       returns: None
    """
    if not isinstance(args, dict):
        args = vars(args)
    for arg in args:
        key = utils.underscore_to_camelcase(arg)
        if isinstance(args[arg], list):
            push_monitoring_indexed_params(params, key, args[arg])
        elif args[arg]:
            params[key] = args[arg]


def push_monitoring_indexed_params(params, key, vals):
    """Populate the params dict for list of vals
    dimensions will be converted to dimensions.member.1.{}

    param params: dictionary to populate

    param key: key to be used in the dictionary

    param vals: list of values to be saved in the dict

    return: Nothing
    """
    idx = 0
    for val in vals:
        idx += 1
        elements = val
        key_index = key + '.member.' + str(idx)
        # This is for cases like --dimensions 'Name=xyz,Values=abc'
        elements = val.split(',')
        if len(elements) == 1 and val.find('=') == -1:
            params[key_index] = val
            continue
        for element in elements:
            if element.find('=') != -1:
                parts = element.split('=')
                if len(parts) != 2:
                    msg = 'Unsupported value ' + element + 'given in request.'
                    raise ValueError(msg)
                element_key, element_val = parts[0], parts[1]
                if element_key == 'Values':
                    element_key = element_key[:-1] + "." + str(idx)
                updated_key = key_index + '.' + element_key
                params[updated_key] = element_val
            else:
                msg = 'Bad request syntax. Please see help for valid request.'
                raise ValueError(msg)

