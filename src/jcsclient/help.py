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

import utils

VERSION = '\nJCS cli 1.0 (April 15 2016)'

ERROR_STRING = (
    "jcs <service> <API> [parameters]\n"
    " Available Services: compute, dss, vpc, iam, rds, mon\n"
    "\n"
    " To see help text, you can run:\n"
    "  jcs help\n"
    "  jcs <service> help\n"
    "  jcs <service> <API> help\n"
    " \n"
)

HELP_TOPICS_DIRNAME = "help_topics"

class Helper(object):
    def __init__(self):
        curr_path = utils.get_dir_path(__file__)
        self.help_dir = utils.join_path(curr_path, HELP_TOPICS_DIRNAME)

    def process_help_file(self, help_file):
        print(VERSION)
        try:
            with open(help_file, 'r') as f:
                print(f.read())
        except IOError as e:
            print(ERROR_STRING)

    def show(self, args):
        """
        Display the help for requested service/api

        Join the keywords inputs to return the help file

        Example:
        jcs compute help
        This would point to help_topics/compute.txt

        jcs compute describe-instances help
        This would point to help_topic/describe-instances.txt
        """
        help_file = self.help_dir
        for arg in args:
            if arg != 'help':
                help_file = utils.join_path(help_file, arg)
            else:
                if help_file == self.help_dir:
                    # Display jcs help
                    help_file = utils.join_path(help_file, 'jcs')
                help_file += '.txt'
                # Handle errors like jcs compute help describe-instances
                if 'help' != args[-1]:
                    raise IndexError()

        self.process_help_file(help_file)
