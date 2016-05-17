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

import config
from jcsclient import help
from jcsclient.compute_api import image
from jcsclient.compute_api import key_pair
from jcsclient.compute_api import instance
from jcsclient.compute_api import volume
from jcsclient.compute_api import snapshot

class Controller(object):
    """Compute Controller class

    This class has all the functions for compute

    It acts as a wrapper over how the calls are
    internally handled

    In the controller methods, first argument passed
    in list of args is the Action name
    """

    def __init__(self):
        self.url = config.get_service_url('compute')
        self.headers = {}
        self.version = '2016-03-01'
        self.verb = 'GET'

    def describe_images(self, args):
        """
        Gives a detailed list of all images visible in
        the account

        param args: Arguments passed to the function

        The function expects either no input or a list of 
        specific images to describe
        """
        return image.describe_images(self.url, self.verb, self.headers,
                                     self.version, args)

    def create_key_pair(self, args):
        """
        Create a key pair to be used during instance
        creation

        param args: Arguments passed to the function

        The function expects a key-name as necessary
        input
        """
        return key_pair.create_key_pair(self.url, self.verb, self.headers,
                                        self.version, args)
 
    def delete_key_pair(self, args):
        """
        Delete a key pair from your account

        param args: Arguments passed to the function

        The function expects a key-name as necessary
        input
        """
        return key_pair.delete_key_pair(self.url, self.verb, self.headers,
                                        self.version, args)
 
    def describe_key_pairs(self, args):
        """
        Describes all key pair in your account

        param args: Arguments passed to the function

        The function expects no arguments
        """
        return key_pair.describe_key_pairs(self.url, self.verb,
                                           self.headers, self.version, args)

    def import_key_pair(self, args):
        """
        Import the public key from an RSA keypair that was
        created using a third-party application

        param args: Arguments passed to the function

        The function expects the following arguments -
        1. Unique name of Key Pair to import
        2. Public Key Material in base64 encoded form
        """
        return key_pair.import_key_pair(self.url, self.verb, self.headers,
                                        self.version, args)

    def describe_instances(self, args):
        """
        Describes instances in your account

        param args: Arguments passed to the function

        The function expects either of the following:
        1. No argument
        2. List of instances to be described
        3. List of filters from which instances would
           be selected.
        """
        return instance.describe_instances(self.url, self.verb,
                                           self.headers, self.version, args)

    def stop_instances(self, args):
        """
        Stop instances in your account

        param args: Arguments passed to the function

        The function expects one or more instances to
        be stopped.
        """
        return instance.stop_instances(self.url, self.verb,
                                       self.headers, self.version, args)

    def start_instances(self, args):
        """
        Start instances in your account

        param args: Arguments passed to the function

        The function expects one or more instances to
        be started.
        """
        return instance.start_instances(self.url, self.verb,
                                        self.headers, self.version, args)

    def reboot_instances(self, args):
        """
        Reboot instances in your account

        param args: Arguments passed to the function

        The function expects one or more instances to
        be rebooted.
        """
        return instance.reboot_instances(self.url, self.verb,
                                         self.headers, self.version, args)

    def terminate_instances(self, args):
        """
        Terminate instances in your account

        param args: Arguments passed to the function

        The function expects one or more instances to
        be terminated.
        """
        return instance.terminate_instances(self.url, self.verb,
                                            self.headers, self.version,
                                            args)

    def get_password_data(self, args):
        """
        Get password for instance in your account. You
        need to also provide the private key file to
        get unencrypted password data.

        param args: Arguments passed to the function

        The function expects the following as input
        1. Instance id
        2. Private key file path (Optional)
        3. Passphrase (incase one is set for the key file)
        """
        return instance.get_password_data(self.url, self.verb,
                                          self.headers, self.version,
                                          args)

    def describe_instance_types(self, args):
        """
        Gives a description of instance types present.

        param args: Arguments passed to the function

        The function expects either no input or a list of
        specific instance types to describe
        """
        return instance.describe_instance_types(self.url, self.verb,
                                                self.headers,
                                                self.version, args)

    def run_instances(self, args):
        """
        Launch specified number of instances in your
        account.

        param args: Arguments passed to the function

        The function expects following arguments -
        1. image id
        2. instance type id
        3. subnet id (optional)
        4. security group id (optional)
        5. key name (optional, but needed to access machine)
        6. instance count (optional)
        7. private ip address (optional)
        8. block device mapping (optional)
        """
        return instance.run_instances(self.url, self.verb, self.headers,
                                      self.version, args)

    def attach_volume(self, args):
        """
        Attach volume to given instance using particular device name
        to be used by the instance.

        param args: Arguments passed to the function

        The functions expects the following arguments -
        1. Instance Id
        2. Volume Id
        3. Device name
        """
        return volume.attach_volume(self.url, self.verb, self.headers,
                                    self.version, args)

    def detach_volume(self, args):
        """
        Detach volume from given instance.

        param args: Arguments passed to the function

        The functions expects the following arguments -
        1. Volume Id
        2. Instance Id (optional)
        3. Force (optional)
        """
        return volume.detach_volume(self.url, self.verb, self.headers,
                                    self.version, args)

    def show_delete_on_termination_flag(self, args):
        """
        View the status of the DeleteOnTermination property for a volume
        that is attached to an instance.

        param args: Arguments passed to the function

        The functions expects the Volume Id in arguments
        """
        return volume.show_delete_on_termination_flag(self.url,
                                       self.verb, self.headers,
                                       self.version, args)

    def update_delete_on_termination_flag(self, args):
        """
        Update the status of the DeleteOnTermination property for a
        volume that is attached to an instance.

        param args: Arguments passed to the function

        The functions expects the following arguments -
        1. Volume Id
        2. Delete on termination flag as bool
        """
        return volume.update_delete_on_termination_flag(self.url,
                                         self.verb, self.headers,
                                         self.version, args)

    def create_volume(self, args):
        """
        Create a new volume which can be attached to an instance.
        This volume can be created empty or from an existing 
        snapshot.

        param args: Arguments passed to the function

        The function expects either of the following -
        1. Size as integer (for empty volume)
        2. Snapshot Id
        """
        return volume.create_volume(self.url, self.verb,
                                    self.headers, self.version,
                                    args)

    def delete_volume(self, args):
        """
        Delete an existing and available volume. The volume
        should be in 'available' state to delete.

        param args: Arguments passed to the function

        The function expects volume id to be deleted
        """
        return volume.delete_volume(self.url, self.verb,
                                    self.headers, self.version,
                                    args)

    def describe_volumes(self, args):
        """
        Get a detailed list of volumes in your account

        param args: Arguments passed to the function

        The function can take following as optional args -
        1. List of volume ids to be described
        2. MaxResults - Max number of results to be shown
        3. NextToken - Id of last volume seen if max number of results
           is less than total volumes.
        4. Detail - by default this is true. Set to false to
           suppress detail
        """
        return volume.describe_volumes(self.url, self.verb,
                                    self.headers, self.version,
                                    args)



    def create_snapshot(self, args):
        """
        Create a new snapshot from a existing volume.

        param args: Arguments passed to the function

        The function expects either of the following -
        Volume Id 
        """
        return snapshot.create_snapshot(self.url, self.verb,
                                    self.headers, self.version,
                                    args)

    def delete_snapshot(self, args):
        """
        Delete an existing and completed snapshot. The snapshot
        should be in 'completed' state to delete.

        param args: Arguments passed to the function

        The function expects snapshot id to be deleted
        """
        return snapshot.delete_snapshot(self.url, self.verb,
                                    self.headers, self.version,
                                    args)

    def describe_snapshots(self, args):
        """
        Get a detailed list of snapshots in your account

        param args: Arguments passed to the function

        The function can take following as optional args -
        1. List of snapshot ids to be described
        2. MaxResults - Max number of results to be shown
        3. NextToken - Id of last snapshot seen if max number of results
           is less than total volumes.
        4. Detail - by default this is true. Set to false to
           suppress detail
        """
        return snapshot.describe_snapshots(self.url, self.verb,
                                    self.headers, self.version,
                                    args)
