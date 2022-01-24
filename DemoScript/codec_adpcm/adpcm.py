import struct

indexTable= [-1,-1,-1,-1,2,4,6,8]
stepsizeTable = [7, 8, 9, 10, 11, 12, 13, 14, 16, 17,
                   19, 21, 23, 25, 28, 31, 34, 37, 41, 45,
                   50, 55, 60, 66, 73, 80, 88, 97, 107, 118,
                   130, 143, 157, 173, 190, 209, 230, 253,
                   279, 307, 337, 371, 408, 449, 494, 544,
                   598, 658, 724, 796, 876, 963, 1060, 1166,
                   1282, 1411, 1552, 1707, 1878, 2066, 2272, 2499, 2749,
                   3024, 3327, 3660, 4026, 4428, 4871, 5358, 5894, 6484,
                   7132, 7845, 8630, 9493, 10442, 11487, 12635, 13899, 15289,
                   16818, 18500, 20350, 22385, 24623, 27086, 29794, 32767]

index = 0
cur_sample = 0

#input code 4bit, return output 16 bit sample
def adpcm2pcm(code):
    global index
    global cur_sample
    global indexTable
    global stepsizeTable

    if ((code & 8) != 0):
        fg = 1
    else:
        fg = 0

    code &= 7
    diff = int((stepsizeTable[index]*code/4) + stepsizeTable[index]/8)

    if fg:
        diff = -diff

    cur_sample += diff
    #check overflow
    if cur_sample > 32767:
        cur_sample = 32767
    elif cur_sample < -32768:
        cur_sample = -32768

    index += indexTable[code]
    # check overflow
    if index < 0:
        index = 0
    elif index > 88:
        index = 88

    return struct.pack('h',cur_sample)

if __name__ == '__main__':
    try:
        f = open('adpcm','rb')
        s = open('pcm','wb')
        tmp = f.read(1)
        while tmp:
            sample=ord(tmp) #transfer to int
            high_bit = sample >> 4
            low_bit = (high_bit << 4)^sample
            s.write(adpcm2pcm(high_bit))
            s.write(adpcm2pcm(low_bit))
            tmp = f.read(1)
        f.close()
        s.close()
    except:
        print("fail")
    print("done")