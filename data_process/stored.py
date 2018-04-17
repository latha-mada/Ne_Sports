#!/usr/bin/env python

import os
import pexpect
from .data_processing import DataProcess
import re


class StoreData(DataProcess):
    """
    Loads the data files from local file system hadoop distributed file system
    """

    def __init__(self, input_path, output_path, backup_path):
        super(DataProcess, self).__init__(input_path, output_path, backup_path)

    def store_data(self):
        """
        stores the data from local file system to hadoop file system.
        :return:
        """
        hdfs_cmd = "hdfs dfs"
        print("Starting to load the data from {} to hdfs {}".format(self.input_path, self.output_path))
        files = self.check_path(self.input_path)
        if files:
            status = self.create_backup_path()
            assert status, "Error: could not create backup folder"
            for file in files:
                print("------------file = ", file)
                season = re.search(r'.*_(.*)\..*', file).group(1)
                hdfs_path = os.path.join(self.output_path, season)
                mkdir = '{} -mkdir -p {}'.format(hdfs_cmd, hdfs_path)
                file_path = os.path.join(self.input_path, file)
                put_cmd = '{} -put {} {}'.format(hdfs_cmd, file_path, hdfs_path)
                pexpect.run(mkdir)
                self.wait_timeout(2)
                print("Copying {} to hdfs {}".format(file_path, hdfs_path))
                pexpect.run(put_cmd)
                print("Copied....")
                status = self.take_backup(file_path)
                if not status:
                    print("Error: could not backup the file {}".format(file_path))
                self.wait_timeout(6)
            else:
                print("There are no files to copy to hdfs. Checking after 10secs")
                self.wait_timeout(10)


class TestStoreData(object):
    """
    unit tests for StoreData class
    """

    @classmethod
    def setup_class(cls):
        cls.input_path = '/home/hduser/hadoop/app/Bigdata/transfer_out'
        cls.backup_path = '/home/hduser/hadoop/app/Bigdata/stored_backup'
        cls.output_path = '/user/hduser/app/data'
        cls.sd = StoreData(cls.input_path, cls.output_path, cls.backup_path)

    def test_stored(self):
        """
        unittest to verify the functionality of stored process
        :return:
        """
        self.sd.store_data()
        files = self.sd.check_path(self.sd.backup_path)
        assert files, "The copying of files to hdfs failed"

