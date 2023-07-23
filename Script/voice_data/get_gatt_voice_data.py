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
    return pkts


if '__main__' != __name__:
    pass
else:
    #while True:
        #print("Input cli:")
        #file = input()
    file = 'demo.cfa'
    if not is_hci(file):
        exit(0)
    ptks = parse(file)
    cnt = 0
    adpcm_buf = []
    for i in ptks:
        cnt += 1;
        if i.packet_type == 2:
            frame_bin = i.binary
            if i.data_length == 127 and frame_bin[10:12] == b'\x3c\x00': # total len = 127, handle = 60, audio data
                print(cnt," ",frame_bin[12:])
                adpcm_buf.append(frame_bin[12:])
            if i.data_length == 14 and frame_bin[10:12] == b'\x3f\x00': # total len = 14, handle = 63, audio sync
                print("sync")

    try:
        f = open('adpcm','wb')
        for i in adpcm_buf:
            f.write(i)
        f.close()
    except:
        pass

