import hci

def is_hci(file):
    ret = False
    try:
        f = open(file,'rb')
        c = f.read(16)
        line = c[:7].decode()
        print(line)
        if "btsnoop" in line:
            ret = True
        del line
        return ret
    except:
        help()
        return ret

def help():
    print("please input hci log")

def parse(file):
    print("Target:",file)
    try:
        f = open(file,'rb')
        #header parse
        c = f.read(16)
        #frame parse
        buf = f.read()
        pkts, _ =hci.from_binary(buf)

    except:
        print("Parse Error")
    print("Parse Done")


if '__main__' != __name__:
    pass
else:
    #while True:
        #print("Input cli:")
        #file = input()
    file = 'btsnoop_hci.cfa'
    if not is_hci(file):
        exit(0)
    parse(file)
