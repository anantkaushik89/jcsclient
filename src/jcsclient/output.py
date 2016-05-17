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

import json
import xmltodict
import requests
from jcsclient import exception
from jcsclient import utils
from jcsclient.utils import SUCCESS

class OutputFormat(object):
    """
    Class to handle how the response from the APIs would be processed
    and displayed to the user.

    Currently there is no command line option to configure how the
    output would be displayed. Thus, there is no __init__() function.
    As the cli is enhanced, this section would be made configurable.
    """
    def display(self, response, headers, webobject=True):
        resp_json = ""
        request_id = None
        try:
            if headers and headers.get('x-jcs-request-id'):
                request_id = headers.get('x-jcs-request-id')
            elif headers and headers.get('request-id'):
                request_id = headers.get('request-id')
            if response:
                if webobject:
                    resp_dict = json.loads(response)
                else:
                    resp_dict = response
                if not request_id:
                    request_id = utils.requestid_in_response(resp_dict)
                resp_json = json.dumps(resp_dict, indent=4, sort_keys=True)
        except:
            try:
                resp_ordereddict = xmltodict.parse(response)
                resp_json = json.dumps(resp_ordereddict, indent=4,
                                       sort_keys=True)
                resp_dict = json.loads(resp_json)
                if not request_id:
                    request_id = utils.requestid_in_response(resp_dict)
                resp_json = json.dumps(resp_dict, indent=4, sort_keys=True)
                resp_json = resp_json.replace("\\n", "\n")
                resp_json = resp_json.replace("\\", "")
            except Exception as e:
                raise e
                #raise exception.UnknownOutputFormat()
        # Handle request-id displaying
        if not request_id:
            raise exception.UnknownOutputFormat()
        output_msg = resp_json
        output_msg += "\nRequest-Id: " + request_id
        print(output_msg)

def format_result(response):
    """
    Rational for the branching - In certain APIs, we would have edited
    the final output to do some processing, like get-password-data

    So, generally, this function expects requests.Response object. But
    in certain cases, we pass a normal dict or xml to the formatter
    and thus the conversion can be handled here.
    """
    if response is not None:
        try:
            output_formatter = OutputFormat()
            if isinstance(response, requests.Response):
                output_formatter.display(response.content, 
                                         headers=response.headers)
                status = response.status_code
                if status != 200 and status != 204:
                    response.raise_for_status()
                else:
                    return SUCCESS
            else:
                output_formatter.display(response, headers=None,
                                         webobject=False)
                return SUCCESS
        except RuntimeError as e:
            """this a special case when the content has already been consumed
            for example, get-object api of dss
            dump request id here
            """
            if str(e) == 'The content for this response was already consumed':
                if response.headers and response.headers.get('x-jcs-request-id'):
                    output_msg = "\nRequest-Id: " + response.headers.get('x-jcs-request-id')
                    print(output_msg)
                pass
            else:
                raise
    return SUCCESS
