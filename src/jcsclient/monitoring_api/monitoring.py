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

import argparse
from jcsclient import utils
from jcsclient import mon_utils
from jcsclient import requestify

def list_metrics(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--metric-name', nargs='?', required=False)
    parser.add_argument('--starting-token', nargs='?', required=False,
                        dest='next_token')
    parser.add_argument('--max-items', nargs='?', type=int, required=False)
    parser.add_argument('--namespace', nargs='?', required=False)
    parser.add_argument('--dimensions', nargs='+', required=False)
    args = parser.parse_args(args)
    mon_utils.populate_monitoring_params_from_args(params, args)
    return requestify.make_request(url, verb, headers, params)

def get_metric_statistics(url, verb, headers, version, args):
    params = {}
    params['Action'] = utils.dash_to_camelcase(args[0])
    params['Version'] = version
    args = args[1:]
    parser = utils.get_argument_parser()
    parser.add_argument('--metric-name', nargs='?', required=True)
    parser.add_argument('--namespace', nargs='?', required=True)
    parser.add_argument('--start-time', nargs='?', required=True)
    parser.add_argument('--end-time', nargs='?', required=True)
    parser.add_argument('--period', nargs='?', type=int, required=True)
    parser.add_argument('--units', nargs='?',
                        choices=['Seconds', 'Microseconds', 'Milliseconds',
                        'Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes',
                        'Terabytes', 'Bits', 'Kilobits', 'Megabits',
                        'Gigabits', 'Terabits', 'Percent', 'Count',
                        'Bytes/Second', 'Kilobytes/Second', 'Megabytes/Second',
                        'Gigabytes/Second', 'Terabytes/Second', 'Bits/Second',
                        'Kilobits/Second', 'Megabits/Second',
                        'Gigabits/Second', 'Terabits/Second', 'Count/Second',
                        'None'], required=False)
    parser.add_argument('--statistics', nargs='+',
                        choices=['SampleCount', 'Average', 'Sum',
                                 'Minimum', 'Maximum'], required=True)
    parser.add_argument('--dimensions', nargs='+', required=False)
    args = parser.parse_args(args)
    mon_utils.populate_monitoring_params_from_args(params, args)
    return requestify.make_request(url, verb, headers, params)
