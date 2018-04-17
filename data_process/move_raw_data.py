#!/usr/bin/env python

import os
import sys
import subprocess
from data_processing import DataProcess


class MoveRawData(DataProcess):

    def __init__(self, input_path, output_path, backup_path):
        super(MoveRawData, self).__init__(input_path, output_path, backup_path)

    def move_raw_data(self):
        """
        moves the raw data preset in the input folder to output folder and copies the contents of the files in backup
        :return:
        """
        self.logger.info("Starting to move the raw data from {} to {}".format(self.input_path, self.output_path))
        file_list = self.check_path(self.input_path)
        if file_list:
            status = self.create_output_path()
            assert status, "Error: Could not create output path"
            status = self.create_backup_path()
            assert status, "Error: Could not create backup path"
            for i in range(len(file_list)):
                f = file_list[i]
                file1 = os.path.join(self.input_path, f)
                self.logger.info(file1)
                status = self.copy_files(file1, self.output_path)
                assert status, "Errror: Failed to copy {} to {}".format(file1, self.output_path)
                self.wait_timeout(1)
        else:
            self.logger.info("there are no files in the input path. Waiting for 10sec")
            self.wait_timeout(10)


class TestMoveRawData(object):
    """
    unit tests for MoveRawData class
    """
    @classmethod
    def setup_class(cls):
        cls.input_path = "/home/latha/my_django/nfl_data"
        cls.backup_path = "/home/latha/my_django/move_raw_backup"
        cls.output_path = '/home/latha/my_django/input'
        cls.md = MoveRawData(cls.input_path, cls.output_path, cls.backup_path)

    def test_move_raw_data(self):
        """
        unittest to verify the functionality of move_raw_data process
        :return:
        """
        self.md.move_raw_data()
        files = self.md.check_path(self.md.output_path)
        assert files, "Error in moving the data to {}".format(self.md.output_path)














