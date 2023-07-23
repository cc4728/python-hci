#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import os.path
import sys
import time
import datetime
import hci

#hci config
HCI_FILE = [""]
HCI_Filter = [""]

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

def process_hci(src_file,des_file):
    list = []
    with open(src_file, 'rb') as f:
        #header parse
        header = f.read(16)
        if not "btsnoop" in header[:7].decode('utf-8', 'ignore'):
            #print("Skip_no_header: ", file)
            return
        print("Start_process: ", src_file)
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
        line = "\tParse Done: " + file
        list.append(line)
        with open(des_file, 'ab+') as w:
            for i in list:
                if i[-1] != '\n':
                    i += '\n'
                w.write(i.encode('utf-8', 'ignore'))
        print(line)
        print("\tResult at:%s"%des_file)
    print("Fininsh_process:{}\t{:.2f}MB\n".format(file, os.stat(file).st_size / (1024 * 1024)))


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

    for key in HCI_FILE:
        get_all_file(path, hci_list, key)

#    print(hci_list)
    for file in hci_list:
        #create new result file
        name = os.path.basename(file).split('.')[0]
        result_path = '%s\\parse_%s_%s.txt'%(result,name,datetime.datetime.now().strftime('%f'))
        process_hci(file,result_path)

    del hci_list
    print("Fininsh parse_hci.py")
    print("auto close 3s later......")
    time.sleep(3)
