#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import os.path
import sys
import time
import datetime
import hci

#hci config
HCI_FILE = ["btsnoop_hci"]

HCI_Filter = ["HCI_Role_Change"]

#save report
REPORT_FILE = ""

def get_all_file(filepath, list, key=None):
    if not os.path.exists(filepath):
        print("file not exist")
        return
    if os.path.isfile(filepath):
        if not key:
            list.append(filepath)
        else:
            if '\\' in filepath:
                names = filepath.split('\\')
                if key in names[-1]:
                    list.append(filepath)
            else:
                if key in filepath:
                    list.append(filepath)
        return

    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            get_all_file(fi_d, list,key)
        else:
            file = os.path.join(filepath, fi_d)
            if not key :
                list.append(file)
            else:
                names = file.split('\\')
                if key in names[-1]:
                    list.append(file)

def process_hci(file):
    list = []
    print("Start_process: ",file)
    with open(file, 'rb') as f:
        #header parse
        header = f.read(16)
        if not "btsnoop" in header[:7].decode('utf-8', 'ignore'):
            print("Skip_no_header: ", file)
            return
        #frame parse
        buf = f.read()
        pkts, _ =hci.from_binary(buf)
        cnt = 0
        for frame in pkts:
            cnt += 1
            if frame.packet_type == 1 or frame.packet_type == 4:
                line = "".join('{} {}').format(str(cnt).ljust(6),frame)
                if HCI_Filter :
                    for key in HCI_Filter:
                        if key in line:
                            list.append(line)
                else:
                    #save all
                    list.append(line)
    if list:
        line = "Finish Process: " + file + '\n'
        list.append(line)
        with open(REPORT_FILE, 'ab+') as w:
            for i in list:
                if i[-1] != '\n':
                    i += '\n'
                w.write(i.encode('utf-8', 'ignore'))
    print("Fininsh_process:{}\t{:.2f}MB".format(file, os.stat(file).st_size / (1024 * 1024)))

if __name__ == '__main__':
    hci_list = []
    print("Start parse_hci.py")
    if len (sys.argv) > 1 and sys.argv[1]:
        print ("Now open =>", sys.argv[1])
        path = sys.argv[1]
    else:
        path = os.getcwd()
        print ("Now open =>", path)

    for key in HCI_FILE:
        get_all_file(path, hci_list, key)

#    print(hci_list)
    for file in hci_list:
        #create new result file
        if not REPORT_FILE:
            REPORT_FILE = 'parse_'+datetime.datetime.now().strftime('%M%S_%f')
        process_hci(file)

    del hci_list
    print("Fininsh parse_hci.py")
    print("auto close 3s later......")
    time.sleep(3)
