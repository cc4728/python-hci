#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import os.path
import sys
import time
import re
import hci

# regular expression config
BT_ADDR_FORMATE = re.compile('(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})')           # xx:xx:xx:xx:xx:xx
LOGCAT_DATE_FORMATE = re.compile('(\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3} )')      #02-06 22:27:39.405
DEVICE_NAME = re.compile(': Utils__\[(.+)\(')                                   # Utils__[PHLRC(24:9F:89:13:22:BD)]

#logcat config
LOGCAT_FILE = ["logcat.log","logcat.txt"]
START_TAG = "BluetoothAdapterService: startDiscovery"
END_TAG = "BluetoothAdapterService: cancelDiscovery"
RESULT_TAG = "GenericBluetoothWizard: Utils__["

#hci config
HCI_FILE = ["btsnoop_hci.cfa","btsnoop_hci.log"]
HCI_Filter = ["HCI_Inquiry","HCI_LE_Set_Scan_Enable","HCI_Inquiry_Cancel",
              "HCI_LE_Advertising_Report","APCF","HCI_LE_Set_Scan_Parameters",
              "HCI_Extended_Inquiry_Result","HCI_LE_Extended_Advertising_Report"]


#save report
REPORT_FILE = "scan_analysis_report.txt"


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
                if key in names[-1:]:
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
                if key in names[-1:]:
                    list.append(file)

#正则表达式
def get_info(line):
    address = None
    name = None
    data = None
    #print(line)
    if line:
        a = BT_ADDR_FORMATE.search(line)
        if a:
            #print("address:",a[0])
            address = a[0]
            #print("address:", address)
        n = DEVICE_NAME.search(line)
        if n:
            #print("name:",n[0])
            name = n[0][10:-1]
            #print("name:", name)
        d = LOGCAT_DATE_FORMATE.search(line)
        if d:
            #print("data:",d[0])
            data = d[0]
    return data,name,address,

# read file by line , ingore read error
def process_logcat(file):
    list = []
    with open(file, 'rb') as f:
        started = 0
        end = 0
        dev_list = []
        line = f.readline().decode('utf-8', 'ignore')
        while line:
            if START_TAG in line:
                started = 1
                end = 0
                data, name, address = get_info(line)
                line = "".join('\n{} ============ [Start Discover]============').format(data.ljust(22))
                list.append(line)
                dev_list.clear()
            elif END_TAG in line :
                end = 1
                started = 0
                data, name, address = get_info(line)
                line = "".join('{}============ [Stop Discover] ============\n').format(data.ljust(22))
                list.append(line)
            elif RESULT_TAG in line and started == 1 and end == 0:
                data,name,address = get_info(line)
                if address and address not in dev_list:
                    line = "".join('{}{}{}').format(data.ljust(22),name.ljust(35),address.ljust(25))
                    list.append(line)  #remove repeat device
                    dev_list.append(address)
            else:
                pass
            line = f.readline().decode('utf-8', 'ignore')

    if list:
        line = "Finish Process: " + file + '\n'
        list.append(line)

    for i in list:
        print(i)
    return list

def process_hci(file):
    list = []
    with open(file, 'rb') as f:
        #header parse
        c = f.read(16)
        if not "btsnoop" in c[:7].decode():
            print("not hci")
            return
        #frame parse
        buf = f.read()
        pkts, _ =hci.from_binary(buf)
        cnt = 0
        for frame in pkts:
            cnt += 1
            if frame.packet_type == 1 or frame.packet_type == 4:
                line = "".join('{} {}').format(str(cnt).ljust(6),frame)
                for key in HCI_Filter:
                    if key in line:
                        list.append(line)
                        break

    if list:
        line = "Finish Process: " + file + '\n'
        list.append(line)

    for i in list:
        print(i)
    return list

if __name__ == '__main__':
    logcat_list = []
    logcat_list_res = []
    hci_list = []
    hci_list_res = []
    print("Start scan_analysis.py")
    if len (sys.argv) > 1 and sys.argv[1]:
        print ("Now open =>", sys.argv[1])
        path = sys.argv[1]
        for key in LOGCAT_FILE:
            get_all_file(path, logcat_list, key)
        for key in HCI_FILE:
            get_all_file(path, hci_list, key)
    else:
        print("Please input file path, and retry")

#    print(logcat_list)
    for file in logcat_list:
        logcat_list_res += process_logcat(file)
#    print(hci_list)
    for file in hci_list:
        hci_list_res += process_hci(file)

    if hci_list_res or logcat_list_res:
         with open(REPORT_FILE, 'w') as f:
            for i in logcat_list_res:
                line = i+'\n'
                f.write(line)
            for i in hci_list_res:
                line = i+'\n'
                f.write(line)

    del logcat_list
    del hci_list
    print("Fininsh scan_analysis.py")
    print("auto close 3s later......")
    time.sleep(3)
