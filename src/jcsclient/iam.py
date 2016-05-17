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

import config
import argparse
from jcsclient import help
from jcsclient import utils
from jcsclient import requestify


def utility(args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    args = args[1:]
    parser = utils.get_argument_parser()
    return params, parser, args

class Controller(object):
    """IAM Controller class

    This class has all the functions for IAM

    It acts as a wrapper over how the calls are
    internally handled

    In the controller methods, first argument passed
    in list of args is the Action name
    """

    def __init__(self):
        self.url = config.get_service_url('iam')
        self.headers = {}
        self.version = '2016-04-14'
        self.verb = 'GET'

    def create_params_dict(self, array):
        params = dict()
        array = array[1:]
        l = len(array)
        if l%2 != 0:
            print "ERROR: Missing parameter values in request\n"
            raise Exception
        for index in range(0,l,2):
            if index % 2 == 0 and array[index][:2] != "--":
                print "ERROR: improper request"
                print "Refer to jcs iam --help "
                raise Exception
            params[array[index][2:]] = array[index+1]
        return params


    def create_user(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name', required = True)
        parser.add_argument('--email')
        parser.add_argument('--password')
        args = parser.parse_args(args)
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                       params)


    def delete_user(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name', required = False)
        parser.add_argument('--id', required = False)
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                       params)


    def list_users(self, args):
        params, parser, args = utility(args)
        args = parser.parse_args(args)
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                       params)


    def update_user(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        parser.add_argument('--new-email')
        parser.add_argument('--new-password')
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        if args.new_email is None and args.new_password is None:
            parser.error("at least one of --new-email and --new-password is required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                               params)


    def get_user(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                                       params)


    def get_user_summary(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                       params)


    def create_credential(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--user-name')
        parser.add_argument('--user-id')
        args = parser.parse_args(args)
        if args.user_name is None and args.user_id is None:
            parser.error("at least one of --user-name and --user-id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                       params)


    def delete_credential(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--access-key')
        parser.add_argument('--id')
        args = parser.parse_args(args)
        if args.access_key is None and args.id is None:
            parser.error("at least one of --access-key and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                       params)


    def get_user_credential(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--user-name')
        parser.add_argument('--user-id')
        args = parser.parse_args(args)
        if args.user_name is None and args.user_id is None:
            parser.error("at least one of --user-name and --user-id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                       params)


    def create_group(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name', required = True)
        parser.add_argument('--description')
        args = parser.parse_args(args)
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                       params)


    def get_group(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                       params)


    def delete_group(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                       params)


    def list_groups(self, args):
        params, parser, args = utility(args)
        args = parser.parse_args(args)
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                               params)


    def assign_user_to_group(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--user-name')
        parser.add_argument('--user-id')
        parser.add_argument('--group-name')
        parser.add_argument('--group-id')
        args = parser.parse_args(args)
        if args.user_name is None and args.user_id is None:
            parser.error("at least one of --user-name and --user-id required")
        if args.group_name is None and args.group_id is None:
            parser.error("at least one of --group-name and --group-id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                       params)


    def check_user_in_group(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--user-name')
        parser.add_argument('--user-id')
        parser.add_argument('--group-name')
        parser.add_argument('--group-id')
        args = parser.parse_args(args)
        if args.user_name is None and args.user_id is None:
            parser.error("at least one of --user-name and --user-id required")
        if args.group_name is None and args.group_id is None:
            parser.error("at least one of --group-name and --group-id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                       params)


    def remove_user_from_group(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--user-name')
        parser.add_argument('--user-id')
        parser.add_argument('--group-name')
        parser.add_argument('--group-id')
        args = parser.parse_args(args)
        if args.user_name is None and args.user_id is None:
            parser.error("at least one of --user-name and --user-id required")
        if args.group_name is None and args.group_id is None:
            parser.error("at least one of --group-name and --group-id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                       params)


    def list_groups_for_user(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                       params)


    def list_user_in_group(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def update_group(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        parser.add_argument('--new-name')
        parser.add_argument('--new-description')
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        if args.new_name is None and args.new_description is None:
            parser.error("at least one of --new-name and --new-description is required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def get_group_summary(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def create_policy(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--policy-document', required = True)
        args = parser.parse_args(args)
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def get_policy(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def list_policies(self, args):
        params, parser, args = utility(args)
        args = parser.parse_args(args)
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def delete_policy(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def update_policy(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        parser.add_argument('--policy-document', required = True)
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def attach_policy_to_user(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--user-name')
        parser.add_argument('--user-id')
        parser.add_argument('--policy-name')
        parser.add_argument('--policy-id')
        args = parser.parse_args(args)
        if args.user_name is None and args.user_id is None:
             parser.error("at least one of --user-name and --user-id required")
        if args.policy_name is None and args.policy_id is None:
            parser.error("at least one of --policy-name and --policy-id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def detach_policy_from_user(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--user-name')
        parser.add_argument('--user-id')
        parser.add_argument('--policy-name')
        parser.add_argument('--policy-id')
        args = parser.parse_args(args)
        if args.user_name is None and args.user_id is None:
            parser.error("at least one of --user-name and --user-id required")
        if args.policy_name is None and args.policy_id is None:
            parser.error("at least one of --policy-name and --policy-id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def attach_policy_to_group(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--group-name')
        parser.add_argument('--group-id')
        parser.add_argument('--policy-name')
        parser.add_argument('--policy-id')
        args = parser.parse_args(args)
        if args.group_name is None and args.group_id is None:
            parser.error("at least one of --group-name and --group-id required")
        if args.policy_name is None and args.policy_id is None:
            parser.error("at least one of --policy-name and --policy-id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def detach_policy_from_group(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--group-name')
        parser.add_argument('--group-id')
        parser.add_argument('--policy-name')
        parser.add_argument('--policy-id')
        args = parser.parse_args(args)
        if args.group_name is None and args.group_id is None:
            parser.error("at least one of --group-name and --group-id required")
        if args.policy_name is None and args.policy_id is None:
            parser.error("at least one of --policy-name and --policy-id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def get_policy_summary(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def create_resource_based_policy(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--policy-document', required = True)
        args = parser.parse_args(args)
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def get_resource_based_policy(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def list_resource_based_policies(self, args):
        params, parser, args = utility(args)
        args = parser.parse_args(args)
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def delete_resource_based_policy(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def update_resource_based_policy(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        parser.add_argument('--policy-document', required = True)
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def attach_policy_to_resource(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--policy-name')
        parser.add_argument('--policy-id')
        parser.add_argument('--policy-document', required = True)
        args = parser.parse_args(args)
        if args.policy_name is None and args.policy_id is None:
            parser.error("at least one of --policy-name and --policy-id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def detach_policy_from_resource(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--policy-name')
        parser.add_argument('--policy-id')
        parser.add_argument('--policy-document', required = True)
        args = parser.parse_args(args)
        if args.policy_name is None and args.policy_id is None:
            parser.error("at least one of --policy-name and --policy-id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)


    def get_resource_based_policy_summary(self, args):
        params, parser, args = utility(args)
        parser.add_argument('--name')
        parser.add_argument('--id')
        args = parser.parse_args(args)
        if args.name is None and args.id is None:
            parser.error("at least one of --name and --id required")
        utils.populate_params_from_cli_args(params, args)
        return requestify.make_request(self.url, self.verb, self.headers,
                                        params)

