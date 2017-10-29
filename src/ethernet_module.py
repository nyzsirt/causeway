#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sh


class EthernetModules:
    def __init__(self):
        self.interfaces = {}
        self.mask_direction = 0
        self.current_mask = 0
        self.smbus_id = 0

    def determine_bridges_interface(self):
        """
        get bridge interface and their items
        """
        current_bridge = ""

        """
        output of sh.brctl("show"):

        bridge name     bridge id               STP enabled     interfaces
        br0             8000.08002794df68       no              enp0s8
                                                                enp0s9
        """
        for line in sh.brctl("show"):
            if len(line.split()) == 1:
                self.interfaces[current_bridge].append(line.split()[0])
            elif len(line.split()) > 1:
                current_bridge = line.split()[0]
                self.interfaces[line.split()[0]] = [line.split()[0], line.split()[-1]]
