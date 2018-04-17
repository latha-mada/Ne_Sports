#!/usr/bin/env python

import os
import re
from data_processing import DataProcess


class FilterData(DataProcess):
    """
    This class has the fuctionality of filtering data
    """

    def __init__(self, input_path, output_path, backup_path):
        super(FilterData, self).__init__(input_path, output_path, backup_path)

    def filter_data(self):
        """
        Filters the data in the input path and copies to the output folder
        :return:
        """
        retain_indexes = [16, 19, 21, 23, 28, 29, 40, 42, 45]
        retain_list = []
        self.logger.info("Starting to filter the raw data from {}".format(self.input_path))
        file_list = self.check_path(self.input_path)
        if file_list:
            status = self.create_output_path()
            assert status, "Error: Could not create output path"
            status = self.create_backup_path()
            assert status, "Error: Could not create backup path"
            for f in file_list:
                # file names are in the form nfl_2017.csv
                season = re.search(r'.*_(.*)\..*', f).group(1)
                outfile = os.path.join(self.output_path, f)
                infile = os.path.join(self.input_path, f)
                with open(infile, 'rb') as fin, open(outfile, 'wb') as fout:
                    i = 0
                    for line in fin:
                        # ignore the heading
                        if i == 0:
                            i += 1
                            continue
                        else:
                            # the first field in the output file is the season
                            retain_list = [season]
                            try:
                                fields = line.split(',')
                                """
                                # filter the data if
                                # player(fields[16] name is not defined, play type(fields[28]) is nor Pass or Run
                                """
                                if fields[28] == 'NA' or fields[16] == 'NA' or fields[16] == '' or fields[28] not in ['Run', 'Pass']:
                                    continue
                                i += 1
                                for index in retain_indexes:
                                    retain_list.append(fields[index])
                                fout.write(','.join(retain_list))
                                fout.write(os.linesep)
                            except IndexError:
                                continue
                            except Exception as e:
                                self.logger.exception(e)
                                continue
                bak_file = os.path.join(self.input_path, f)
                status = self.take_backup(bak_file)
                if not status:
                    self.logger.info("Error : during backup")

        else:
            self.logger.info("Input is empty. Will wait for 5sec")
            self.wait_timeout(5)


class TestFilterData(object):
    """
    unit tests for FilterData class
    """

    @classmethod
    def setup_class(cls):
        cls.input_path = "/home/latha/my_django/input"
        cls.backup_path = "/home/latha/my_django/filter_backup"
        cls.output_path = '/home/latha/my_django/filter_out'
        cls.fd = FilterData(cls.input_path, cls.output_path, cls.backup_path)

    def test_filterd(self):
        """
        unittest to verify the functionality of filterd process
        :return:
        """
        self.fd.filter_data()
        files = self.fd.check_path(self.fd.output_path)
        assert files, "Error in copying the filtered data to {}".format(self.fd.output_path)
        files = self.fd.check_path(self.fd.backup_path)
        assert files, "Error: Backup failed"
