#!/usr/bin/env python
import logging
import os
import subprocess
import time


FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


class DataProcess(object):
    """
    This is the base class has has the implemantation of common functionalities like creating paths, deleting paths,
    moving files etc.
    """
    def __init__(self, input_path, output_path, backup_path):

        handler = logging.StreamHandler()
        formatter = logging.Formatter(FORMAT)
        handler.setFormatter(formatter)
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
        self.input_path= input_path
        self.output_path = output_path
        self.backup_path = backup_path

    def _create_path(self, path):
        """
        This is a pricate method used to create the specified path recursively
        :param path:
        :return: status: boolean - True if path exists or is successfully created, else False
        """
        status = True
        par_path = os.path.dirname(path)
        if not os.path.exists(par_path):
            status = self._create_path(par_path)
        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except Exception as e:
                self.logger.exception(e)
                status = False
        return status

    def create_input_path(self):
        """
        create the input directory if it does not exist
        :return: status: boolean
        """
        return self._create_path(self.input_path)

    def create_output_path(self):
        """
        create the output directory if it does not exist
        :return: status: boolean
        """
        return self._create_path(self.output_path)

    def create_backup_path(self):
        """
        create the backup directory if it does not exist
        :return: status: boolean
        """
        return self._create_path(self.backup_path)

    def check_path(self, path):
        """
        checks to see if there are any files in the input path and returns the LIST of names of the files if present.
        :return: file_list : List of the files in the input directory
        """
        file_list = []
        if os.path.exists(path):
            cmd = 'ls {}'.format(path)
            proc = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = proc.communicate()
            file_list = out.splitlines()
            self.logger.info("INFO: the files in the {} are : {}".format(path, file_list))
        return file_list

    def move_files(self, bak_file, to_dir):
        """
        move the files from from_dir to to_dir
        :param bak_file:
        :param to_dir:
        :return: status: boolean
        """
        status = False
        bak_file = os.path.abspath(bak_file)
        bak_file_path = os.path.abspath(to_dir)
        mv_cmd = 'mv {} {}'.format(bak_file, bak_file_path)
        status = self._create_path(to_dir)
        if status:
            move_proc = subprocess.Popen(mv_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = move_proc.communicate()

        files_list = self.check_path(to_dir)
        if os.path.basename(bak_file) in files_list:
            status = True
        return status

    def copy_files(self, file_to_cp, to_dir):
        """
        move the files from from_dir to to_dir
        :param file_to_cp:
        :param to_dir:
        :return: status: boolean
        """
        self.logger.info("Copying {} to {}".format(file_to_cp, to_dir))
        cp_cmd = 'cp {} {}'.format(file_to_cp, to_dir)
        status = self._create_path(to_dir)
        if status:
            cp_proc = subprocess.Popen(cp_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = cp_proc.communicate()
            self.logger.debug("out = {}".format(out))
        files_list = self.check_path(to_dir)
        if file_to_cp in files_list:
            status = True
        return status

    def take_backup(self, bak_file):
        """
        copies the file from input folder to backup folder
        :return:
        """
        self.logger.info("Taking backup of the file {}".format(bak_file))
        return self.move_files(bak_file, self.backup_path)


    def wait_timeout(self, timeout):
        """
        waits for timeout secs
        :return:
        """
        time.sleep(timeout)


class TestBaseClass(object):
    """
    Unit tests for testing the DataProcess class
    """
    @classmethod
    def setup_class(cls):
        cls.dp = DataProcess("/home/latha/input", "/home/latha/output", "/home/latha/extra/backup")

    def test_create_input_path(self):
        status = self.dp.create_input_path()
        assert status, "Failed to create input path"

    def test_create_output_path(self):
        status = self.dp.create_output_path()
        assert status, "Failed to create output path"

    def test_create_backup_path(self):
        status = self.dp.create_backup_path()
        assert status, "Failed to create backup path"

    def test_check_path(self):
        file_list = self.dp.check_path(self.dp.input_path)
        assert bool(file_list), "Failed: The input list must have been empty but it has the " \
                                "following contents: {}".format(file_list)

