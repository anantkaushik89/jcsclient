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

from jcsclient import config
from jcsclient import help
from jcsclient.monitoring_api import monitoring

class Controller(object):
    """Monitoring Controller class

    This class has all the functions for monitoring

    It acts as a wrapper over how the calls are
    internally handled

    In the controller methods, first argument passed
    in list of args is the Action name
    """

    def __init__(self):
        self.url = config.get_service_url('mon')
        self.headers = {}
        self.version = '2016-03-01'
        self.verb = 'GET'

    def list_metrics(self, args):
        """
        Gives a detailed list of all images visible in
        the account

        param args: Arguments passed to the function

        The function expects either no input or a list of
        specific images to describe
        """
        return monitoring.list_metrics(self.url, self.verb, self.headers,
                                       self.version, args)

    def get_metric_statistics(self, args):
        """
        Create a key pair to be used during instance
        creation

        param args: Arguments passed to the function

        The function expects a key-name as necessary
        input
        """
        return monitoring.get_metric_statistics(self.url, self.verb,
                                                self.headers, self.version,
                                                args)
