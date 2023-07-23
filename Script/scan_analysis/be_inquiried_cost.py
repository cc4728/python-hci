import os
import hci
import re

ScanFilter = ["HCI_Inquiry","HCI_LE_Set_Scan_Enable","HCI_Inquiry_Cancel",
              "HCI_LE_Advertising_Report","APCF",
              "HCI_LE_Set_Scan_Parameters",	"HCI_LE_Set_Extended_Scan_Enable",
              "HCI_LE_Set_Extended_Scan_Parameters",
              "HCI_Extended_Inquiry_Result","HCI_LE_Extended_Advertising_Report",
              "HCI_Inquiry_Result_with_RSSI",]

TIME_FORMATE = re.compile('(\d{2}:\d{2}:\d{2}.\d{4})')

#target is address or name
def be_inquiry_cost(target,buff,des_file=None):
    line = []
    cost = []
    total_scan = 0
    if not len(buff):
        print("Not found scan hci package")
        return

    if des_file:
        if os.path.exists(des_file):
            os.remove(des_file)

    #le device
    start = ""
    find = ""
    for l in buff:
        #print(l)
        if "HCI_LE_Set_Extended_Scan_Enable" in l or "HCI_LE_Set_Scan_Enable" in l:
            print(l)
            line.append(l)
            if 'Disable' in l:
                start = ""
            else:
                total_scan +=1
                start = l

        if not start:
            continue

        if start and not find and target in l :
            if "HCI_LE_Extended_Advertising_Report" in l or "HCI_LE_Advertising_Report" in l:
                find = l
                start_time = TIME_FORMATE.search(start)[0]
                find_time = TIME_FORMATE.search(find)[0]
                cost_time = hci.ts2num(find_time) - hci.ts2num(start_time)
                res = "start(%s)-find(%s) cost<%f>s"%(start_time,find_time,cost_time)
                print(res)
                line.append(res)
                cost.append(cost_time)

    if len(cost):
        #process le scan
        total = 0
        for c in cost:
            total += c
        res = "\nTotal init Start Scan %d times\nFound device %d times" \
              "\n \t total_cost<%f>s  average_cost<%f>s"%(total_scan,len(cost),total,total/len(cost))
        print(res)
        line.append(res)
        return line
    else:
        # other check BR/EDR inq
        start = ""
        find = ""
        for l in buff:
            # print(l)
            if "HCI_Inquiry" in l :
                print(l)
                line.append(l)
                total_scan += 1
                start = l

            if "HCI_Inquiry_Cancel" in l :
                start = ""

            if not start:
                continue

            if start and not find and target in l:
                if "HCI_Inquiry_Result_with_RSSI" in l or "HCI_Extended_Inquiry_Result" in l:
                    find = l
                    start_time = TIME_FORMATE.search(start)[0]
                    find_time = TIME_FORMATE.search(find)[0]
                    cost_time = hci.ts2num(find_time) - hci.ts2num(start_time)
                    res = "start(%s)-find(%s) cost<%f>s" % (start_time, find_time, cost_time)
                    print(res)
                    line.append(res)
                    cost.append(cost_time)

        if len(cost):
            total = 0
            for c in cost:
                total += c
            res = "\nTotal init Start Scan %d times\nFound device %d times" \
                  "\n \t total_cost<%f>s  average_cost<%f>s" % (total_scan, len(cost), total, total / len(cost))
            print(res)
            line.append(res)
        return line


if __name__ == '__main__':

    print("Please input hci log")
    print("Please input target device name or address")

    #need process hci log
    src = "C:\\Users\\jing\\Desktop\\parseHci\\python-hci\\DemoHciLog\\ums.cfa"
    #save parse result path
    des = "be_inquired_cost.txt"

    buff = hci.parse(src,des,ScanFilter)
    be_inquiry_cost("Jing_test_right",buff)



