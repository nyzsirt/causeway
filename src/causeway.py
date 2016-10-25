#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sh
import time
import constants
from daemon import Daemon


class Causeway(Daemon):
    def __init__(self, _pid_file):
        """
        init functions
        """
        super(Causeway, self).__init__(_pid_file)
        self.ethernet_modules = []
        self.model_name = ""

    def read_model_name(self):
        """
        get appliance model name from config file
        """
        content = open(constants.HWCODE_FILE_PATH)
        self.model_name = content.readlines()[0].strip()

    # def determine_awake_smbus(self):d
    def run(self):
        """
        This is run method
        """
        while True:
            # TODO: core causeway process
            time.sleep(3)

if __name__ == '__main__':
    causewayd = Causeway(constants.PID_FILE)
    causewayd.start()
