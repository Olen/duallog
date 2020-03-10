#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test script for the duallog module.

Checks whether log rotation works properly.
"""


# Import required packages.
import logging
import duallog
from time import sleep


# Write many log messages to file to test log rotation.
duallog.setup('logtest', rotation='hourly')

for n in range(1, 120):
    logging.error('This is test log message no. {:06d}.'.format(n))
    sleep(60)
