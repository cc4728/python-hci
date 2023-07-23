#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import os.path
import sys
import time
import datetime
import hci


if __name__ == '__main__':
    hci_list = []
    result = ""
    print("Start parse_hci.py")
    if len (sys.argv) > 1 and sys.argv[1]:
        print ("Now open =>", sys.argv[1])
        path = sys.argv[1]
    else:
        path = os.getcwd()
        print ("Now open =>", path)

    if len (sys.argv) > 2 and sys.argv[2]:
        print ("Log Save at =>", sys.argv[2])
        path = sys.argv[2]
    else:
        result = "tmp"
        print ("Log Save at =>", result)

    hci.get_all_file(path, hci_list, None)

#    print(hci_list)
    for file in hci_list:
        #create new result file
        name = os.path.basename(file).split('.')[0]
        result_path = '%s\\parse_%s_%s.txt'%(result,name,datetime.datetime.now().strftime('%f'))
        hci.parse(file, result_path)

    del hci_list
    print("Fininsh parse_hci.py")
    print("auto close 3s later......")
    time.sleep(3)
