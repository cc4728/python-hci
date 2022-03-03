#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import os.path
import sys
import time
import datetime

#hci config
HCI_FILE = ["btsnoop_hci.cfa","btsnoop_hci.log","BT_HCI_"]

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

    with open(file, 'rb') as f:
        #header parse
        header = f.read(16)
        if not "btsnoop" in header[:7].decode('utf-8', 'ignore'):
            print("Skip_no_header: ", file)
            return
        #frame parse
        buf = f.read()
        with open(REPORT_FILE, 'ab+') as w:
            if os.stat(REPORT_FILE).st_size < 16:
                w.write(header)
            w.write(buf)
        print("Fininsh_process:{}\t{:.2f}MB".format(file, os.stat(file).st_size / (1024 * 1024)))

def remove_repeat_path(file_path_list):
    # 去掉重复路径
    return list(set(file_path_list))

def remove_repeat_name(file_path_list):
    names_list = []
    tmp = remove_repeat_path(file_path_list)
    # 去掉重复文件名
    for i in file_path_list:
        name = ""
        if '\\' in i:
            names = i.split('\\')
            name = names[-1]
        else:
            name = i
        if not name in names_list:
            names_list.append(name)
        else:
            tmp.remove(i)
    return tmp

if __name__ == '__main__':
    hci_list = []
    name = ""
    print("Start merge_hci.py")
    if len (sys.argv) > 1 and sys.argv[1]:
        print ("Now open =>", sys.argv[1])
        path = sys.argv[1]
    else:
        path = os.getcwd()
        print ("Now open =>", path)

    for key in HCI_FILE:
        get_all_file(path, hci_list, key)

#remove repreat name
    hci_list = remove_repeat_name(hci_list)
    print (len(hci_list))


#    print(hci_list)
    for file in hci_list:
        #create new result file
        if '\\' in file:
            name = file.split('\\')[-1]
        else:
            name = file
        if not REPORT_FILE:
            REPORT_FILE = datetime.datetime.now().strftime('%M%S_%f')+'_'+name
        process_hci(file)
        if os.path.exists(REPORT_FILE) and os.stat(REPORT_FILE).st_size > 300*1024*1024:
                print("Create:{}\t{:.2f}MB".format(REPORT_FILE, os.stat(REPORT_FILE).st_size / (1024 * 1024)))
                REPORT_FILE = datetime.datetime.now().strftime('%M%S_%f') + '_' + name

    del hci_list
    print("Fininsh merge_hci.py")
    print("auto close 3s later......")
    time.sleep(3)

