#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import os.path
import sys
import time
import re
import hci

# regular expression config
BT_ADDR_FORMATE = re.compile('(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})')
LOGCAT_DATE_FORMATE = re.compile('(\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3} )')
DEVICE_NAME = re.compile(': Utils__\[(.+)\(')

