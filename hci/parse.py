#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import os.path
from .from_binary import from_binary

def is_hci(file):
    try:
        if not os.path.exists(file):
            print("file not exist")
            return False

        with open(file, 'rb') as f:
            #header parse
            header = f.read(16)
            if not "btsnoop" in header[:7].decode('utf-8', 'ignore'):
                #print("Skip_no_header: ", file)
                return False
    except:
        return False
    return True

"""
filepath: target dir
list:     return all file list 
filter_files: a part of target file name
"""

def get_all_file(filepath, list, filter_file_name = None):
    if not os.path.exists(filepath):
        print("file not exist")
        return
    if os.path.isfile(filepath):
        if not filter_file_name:
            list.append(filepath)
        else:
            if '\\' in filepath:
                names = filepath.split('\\')
                if filter_file_name in names[-1]:
                    list.append(filepath)
            else:
                if filter_file_name in filepath:
                    list.append(filepath)
        return

    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            get_all_file(fi_d, list,filter_file_name)
        else:
            file = os.path.join(filepath, fi_d)
            if not filter_file_name :
                list.append(file)
            else:
                names = file.split('\\')
                if filter_file_name in names[-1]:
                    list.append(file)


"""
src_file:       target single file
des_file:       result save at
filter:         target hci pkt list
"""
def parse(src_file,des_file,filter = None):
    list = []

    if not is_hci(src_file):
        return list

    if os.path.exists(des_file):
        os.remove(des_file)

    with open(src_file, 'rb') as f:
        #header parse
        header = f.read(16)
        print("Start_process: ", src_file)
        #frame parse
        buf = f.read()
        pkts, _ = from_binary(buf)
        cnt = 0
        for frame in pkts:
            cnt += 1
            if frame.packet_type == 1 or frame.packet_type == 4:
                line = "".join('{} {}').format(str(cnt).ljust(6),frame)
                if filter:
                    for key in filter:
                        if key in line:
                            list.append(line)
                else:
                    #save all
                    list.append(line)
    if list:
        line = "\tParse Done: " + src_file
        list.append(line)
        with open(des_file, 'ab+') as w:
            for i in list:
                if i[-1] != '\n':
                    i += '\n'
                w.write(i.encode('utf-8', 'ignore'))
        print(line)
        print("\tResult at:%s"%des_file)
    print("Fininsh_process:{}\t{:.2f}MB\n".format(src_file, os.stat(src_file).st_size / (1024 * 1024)))
    return list