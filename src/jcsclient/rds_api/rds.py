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
from jcsclient import requestify

def create_db_instance(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--db-instance-identifier', required=True, help='server name')
    parser.add_argument('--db-instance-class', required=True)
    parser.add_argument('--engine', required=True)
    parser.add_argument('--allocated-storage', required=True)
    parser.add_argument('--master-username', required=True)
    parser.add_argument('--master-user-password', required=True)
    args = parser.parse_args(args)
    utils.populate_params_from_cli_args(params, args)
    return requestify.make_request(url, verb, headers, params)

def describe_db_instances(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--instance-identifier', required=False, help='server name')
    args = parser.parse_args(args)
    utils.populate_params_from_cli_args(params, args)
    return requestify.make_request(url, verb, headers, params)

def delete_db_instance(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--db-instance-identifier', required=True)
    # TODO(rushiagr): If one doesn't specify skip-final-snapshot, then he/she
    # has to specify final-db-snapshot-identifier compulsarily. Add this check
    final_arg = parser.add_mutually_exclusive_group(required=True)
    final_arg.add_argument('--skip-final-snapshot', dest='skip_final_snapshot',
            action='store_true')
    final_arg.set_defaults(skip_final_snapshot=False)
    final_arg.add_argument('--final-db-snapshot-identifier', required=False)
    args = parser.parse_args(args)
    utils.populate_params_from_cli_args(params, args)
    return requestify.make_request(url, verb, headers, params)

def modify_db_instance(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--db-instance-identifier', required=True)
    parser.add_argument('--preferred-maintenance-window', required=False)
    parser.add_argument('--preferred-backup-window', required=False)
    parser.add_argument('--backup-retention-period', required=False)
    parser.add_argument('--new-db-instance-identifier', required=False)
    args = parser.parse_args(args)
    utils.populate_params_from_cli_args(params, args)
    return requestify.make_request(url, verb, headers, params)

def describe_db_snapshots(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--db-instance-identifier', required=False)
    parser.add_argument('--db-snapshot-identifier', required=False)
    parser.add_argument('--snapshot-type', required=False)
    args = parser.parse_args(args)
    utils.populate_params_from_cli_args(params, args)
    return requestify.make_request(url, verb, headers, params)

def create_db_snapshot(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--db-instance-identifier', required=True)
    parser.add_argument('--db-snapshot-identifier', required=True)
    args = parser.parse_args(args)
    utils.populate_params_from_cli_args(params, args)
    return requestify.make_request(url, verb, headers, params)

def delete_db_snapshot(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--db-snapshot-identifier', required=True)
    args = parser.parse_args(args)
    utils.populate_params_from_cli_args(params, args)
    return requestify.make_request(url, verb, headers, params)

def restore_db_instance_from_db_snapshot(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--db-instance-identifier', required=True)
    parser.add_argument('--db-snapshot-identifier', required=True)
    parser.add_argument('--db-instance-class', required=False)
    parser.add_argument('--preferred-maintenance-window', required=False)
    parser.add_argument('--preferred-backup-window', required=False)
    parser.add_argument('--backup-retention-period', required=False)
    args = parser.parse_args(args)
    utils.populate_params_from_cli_args(params, args)
    return requestify.make_request(url, verb, headers, params)
