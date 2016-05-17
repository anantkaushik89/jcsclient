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

import os
import re
import importlib
import argparse
import json
import binascii
import xmltodict
from jcsclient import help
from jcsclient import exception
from Crypto.PublicKey import RSA
# Set codes for success and failure of APIs.
# This can be enhanced to return service specific
# error codes down the line.
SUCCESS = 0
FAILURE = 255

def load_service(service):
    """
    Import the module for requested service. Raise exception if
    the required module isnt found.

    param service: string representing the service to be loaded

    return: requested module
    """
    try:
        current_mod = get_dir_name(__file__)
        return importlib.import_module('.' + service,
                                       package=current_mod)
    except ImportError as ie:
        raise exception.ServiceNotFound(service)

def get_module_method(controller, method, service):
    """
    Get the member from Controller object in mod_name. Raise
    exception if the required member isnt found.


    return: requested method
    """
    try:
        return getattr(controller, method)
    except AttributeError as ae:
        raise exception.MethodNotFound(service, method)

def create_controller(service, service_name):
    """
    Create Controller object for the particular module. Raise
    an exception if the controller object cant be created.

    param service: module loaded in memory

    param service_name: string representing the module name

    return: Controller object
    """
    try:
        return getattr(service, 'Controller')()
    except AttributeError as ae:
        raise exception.UnImplementedService(service_name)

def get_dir_name(filename):
    """Return the current directory name from filename

    param filename: The file whose directory name has 
            to be returned

    return: string with directory name
    """
    return os.path.basename(os.path.dirname(__file__))

def get_dir_path(filename):
    """Return the current directory path from filename

    param filename: The file whose directory path has 
            to be returned

    return: string with directory path
    """
    return os.path.abspath(os.path.dirname(__file__))

def join_path(path_a, path_b):
    """Join the paths given as inputs to form final path

    param path_a: String representing path as prefix

    param path_b: String representing path as suffix

    return: string with joined path
    """
    return os.path.join(path_a, path_b)

def dash_to_underscore(keyword):
    """Change dash '-' to underscore '_' in string

    param keyword: string where the replacement has to
            be done

    return: string. Example one-two changes to one_two
    """
    return keyword.replace('-', '_')

def underscore_to_camelcase(keyword):
    """Change underscore '_' to CamelCase string in string

    param keyword: string which has to be modified as
            above

    return: string. Example one_two changes to OneTwo
    """
    parts = keyword.split('_')
    keyword = ''
    for part in parts:
        if part == 'db':
            part = 'DB'
        else:
            part = part.capitalize()
        keyword += part
    return keyword

def dash_to_camelcase(keyword):
    """Change dash '-' to CamelCase string in string

    param keyword: string which has to be modified as
            above

    return: string. Example one-two changes to OneTwo
    """
    parts = keyword.split('-')
    keyword = ''
    for part in parts:
        if part == 'db':
            part = 'DB'
        else:
            part = part.capitalize()
        keyword += part
    return keyword

def push_indexed_params(params, key, vals):
    """Populate the params dict for list of vals

    Here the key would be changed from plural to
    singular, dropping the last 's'.
    So --image-ids jmi-xxx jmi-yyy would be treated
    as ImageId.1=jmi-xxx&ImageId.2=jmi-yyy

    param params: dictionary to populate

    param key: key to be used in the dictionary

    param vals: list of values to be saved in the dict

    return: Nothing
    """
    # Naive way to check plural, but works
    if key[-1] == 's':
        key = key[:-1]

    idx = 0
    for val in vals:
        idx += 1
        elements = val
        key_index = key + '.' + str(idx)
        # This is for cases like --filter 'Name=xyz,Values=abc'
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


def get_protocol_and_host(url):
    """Validate a given url and extract the protocol and
       host from given url.
       If the url if invalid, a tuple of (None, None) is
       returned to the caller.

       param url: Input url to be parsed

       returns: Tuple of protocol and host. So if input is
            https://compute.jiocloud.com, the method returns
            (https, compute.jiocloud.com)
    """

    url_regex = re.compile('(http[s]?)://((?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)')
    url_parts = url_regex.match(url)
    if not url_parts:
        return (None, None)
    else:
        return (url_parts.group(1), url_parts.group(2))


def populate_params_from_cli_args(params, args):
    """After the argparser has processed args, populate the
       params dict, processing the given args.

       param params: a dict to save the processed args

       param args: Namespace object where args are saved

       returns: None
    """
    if not isinstance(args, dict):
        args = vars(args)
    for arg in args:
        key = underscore_to_camelcase(arg)
        if isinstance(args[arg], list):
            push_indexed_params(params, key, args[arg])
        elif args[arg]:
            params[key] = args[arg]

def get_argument_parser():
    """
    Argument Parser to be used for argument parsing

    The default argument parser has been overridden
    to edit its behaviour in how the help is shown
    and how errors are handled.
    """
    return argparse.ArgumentParser(add_help=False, usage=help.ERROR_STRING,
                             formatter_class=argparse.RawTextHelpFormatter)

def web_response_to_json(response):
    """
    Modify the web response output to json format

    param response: response object from requests library

    return: json object representing the response content
    """
    try:
        if response:
            resp_dict = json.loads(response.content)
    except:
        try:
            resp_ordereddict = xmltodict.parse(response.content)
            resp_json = json.dumps(resp_ordereddict, indent=4,
                                   sort_keys=True)
            resp_dict = json.loads(resp_json)
        except:
            raise exception.UnknownOutputFormat()
    return resp_dict

def import_ssh_key(private_key_file, passphrase=None):
    """
    Import contents from RSA private key file

    param private_key_file: path to private key file 

    param passphrase: passphrase for the private key, by default
            None

    return: contents from private key file
    """
    key_file_contents = None
    private_key_file = os.path.abspath(private_key_file)
    try:
        with open(private_key_file, 'r') as key_file:
            key_file_contents = key_file.readlines()
        return RSA.importKey(key_file_contents, passphrase=passphrase)
    except IOError as ie:
        raise exception.PrivateKeyNotFound(private_key_file)
    except Exception as e:
        raise exception.ImportKeyError(private_key_file)

def pkcs1_unpad(text):
    """Helper function for handling pkcs1 standard padding"""
    if len(text) > 0 and text[0] == '\x02':
        # Find end of padding marked by nul
        pos = text.find('\x00')
        if pos > 0:
            return text[pos+1:]
    return None

def long_to_bytes(val):
    """Helper function for changing raw decrypted password contents"""
    try:
        width = val.bit_length()
    except:
        width = len(val.__hex__()[2:-1]) * 4
    width += 8 - ((width % 8) or 8)
    fmt = '%%0%dx' % (width // 4)
    s = binascii.unhexlify(fmt % val)
    return s

def requestid_in_response(response):
    """Helper function for returning request id from response of API"""
    for keys in response:
        if keys.lower() == 'requestid':
            request_id = response.get(keys)
            response.pop(keys)
            return request_id
        elif isinstance(response.get(keys), dict):
            request_id = requestid_in_response(response.get(keys))
            if request_id:
                return request_id
    return None
