#!/usr/bin/env python

import os
import pexpect
from .data_processing import DataProcess


class TransferData(DataProcess):
    """
    transfers the data files from output directory to remote vm - hadoop cluster
    """

    def __init__(self, input_path, output_path, backup_path):
        super(DataProcess, self).__init__(input_path, output_path, backup_path)

    def transfer_data(self, remote_user, remote_machine):
        """
        transfers the data from input path to output path. output path is usually a node in hadoop cluster
        :param: remote_user :string: the username in hadoop node
        :param: remote_machine:string : the ip address/hostname of the hadoop cluster node
        :return:
        """
        print("Starting to transfer the filtered data to hadoop cluster")
        files = self.check_path(self.input_path)
        if files:
            status = self.create_output_path()
            assert status, "Error: Could not create output path"
            status = self.create_backup_path()
            assert status, "Error: Could not create backup path"
            for file in files:
                file_path = os.path.join(self.input_path, file)
                scp_cmd = 'scp {} {}@{}:/{}'.format(file_path, remote_user, remote_machine, self.output_path)
                print("----- scp_cmd = ", scp_cmd)
                pexpect.run(scp_cmd)
                # take the baack up of the transfered file
                status = self.take_backup(file_path)
                if not status:
                    print("Error: Failed to take a backup of the file")
                self.wait_timeout(1)
            else:
                print("There are no files to transfer. Will wait for 2secs")
                self.wait_timeout(2)


class TestTransferData(object):
    """
    unit tests for TransferData class
    """

    @classmethod
    def setup_class(cls):
        cls.input_path = "/home/hduser/hadoop/app/Bigdata/filter_out"
        cls.backup_path = "/home/hduser/hadoop/app/Bigdata/transfer_backup"
        cls.output_path = '/home/hduser/hadoop/app/Bigdata/transfer_out'
        cls.remote_user = 'hduser'
        cls.remote_machine = 'localhost'
        cls.td = TransferData(cls.input_path, cls.output_path, cls.backup_path)

    def test_transferd(self):
        """
        unittest to verify the functionality of transfer_data process
        :return:
        """
        self.td.transfer_data(self.remote_user, self.remote_machine)
        files = self.td.check_path(self.td.output_path)
        assert files, "The copying of files to Hadoop cluster failed"
        files = self.td.check_path(self.td.backup_path)
        assert files, "Error: Backup failed"

