#!/usr/bin/env python

import sys
from move_raw_data import MoveRawData
from filterd import FilterData
from stored import StoreData
from transferd import TransferData
import logging
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


class StartProcesses(object):
    """
    the object of this class will have the capability to start all the nesports processes
    """
    def __init__(self, md_in="/home/hduser/hadoop/app/Bigdata/data",
                 md_bk="/home/hduser/hadoop/app/Bigdata/move_raw_backup",
                 md_out='/home/hduser/hadoop/app/Bigdata/input',
                 fd_in="/home/hduser/hadoop/app/Bigdata/input",
                 fd_bk="/home/hduser/hadoop/app/Bigdata/filter_backup",
                 fd_out='/home/hduser/hadoop/app/Bigdata/filter_out',
                 td_in="/home/hduser/hadoop/app/Bigdata/filter_out",
                 td_bk="/home/hduser/hadoop/app/Bigdata/transfer_backup",
                 td_out='/home/hduser/hadoop/app/Bigdata/transfer_out',
                 remote_user='hduser',
                 remote_machine='localhost',
                 sd_in='/home/hduser/hadoop/app/Bigdata/transfer_out',
                 sd_bk='/home/hduser/hadoop/app/Bigdata/stored_backup',
                 sd_out='/user/hduser/app/data'):
        self.remote_user = remote_user
        self.remote_machine = remote_machine
        self.move_raw_data = MoveRawData(md_in, md_out, md_bk)
        self.filter_data = FilterData(fd_in, fd_out, fd_bk)
        self.transfer_data = TransferData(td_in, td_out, td_bk)
        self.store_data = StoreData(sd_in, sd_out, sd_bk)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(FORMAT)
        handler.setFormatter(formatter)
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def start_processes(self):
        """
        This process starts the processes in sequence
        1. move_raw data
        2. filterdata
        3. transfer data to hadoop node
        4. load data to hdfs
        :return:
        """
        import time
        timeout = time.time() + 1800  # keep polling for raw data for 30 mins
        while time.time() < timeout:
            if not self.move_raw_data.input_path:
                self.logger.info("{} is not a valid input path for raw data....Please check the path and try again: "
                      "Bye...".format(self.move_raw_data.input_path))
                sys.exit(1)
            self.move_raw_data.move_raw_data()
            if not self.filter_data.input_path:
                self.logger.info("{} is not a valid path to filter data....Please check the path and try again: "
                      "Bye...".format(self.filter_data.input_path))
                sys.exit(1)
            self.filter_data.filter_data()
            if not self.transfer_data.input_path:
                self.logger.info("{} is not a valid path for transfer data....Please check the path and try again: "
                      "Bye...".format(self.transfer_data.input_path))
                sys.exit(1)
            self.transfer_data.transfer_data(self.remote_user, self.remote_machine)
            if not self.store_data.input_path:
                self.logger.info("{} is not a valid input path for stored process....Please check the path and try again: "
                      "Bye...".format(self.store_data.input_path))
                sys.exit(1)
            self.store_data.store_data()

            self.logger.info("Success: Finished all the processes .... Will wait for 10secs and poll for Raw data")

            time.sleep(10)

if __name__ == '__main__':
    start_procs = StartProcesses()
    start_procs.start_processes()
    print("Timed out! please start the processes again....")
