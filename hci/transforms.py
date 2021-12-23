import binascii


def _hex_string_to_bytes(addr, revert=True):
    b = binascii.unhexlify(addr.replace(':', ''))

    if (revert):
        b = b[::-1]

    return b


def _bytes_to_hex_string(data):
    return ':'.join('{:02X}'.format(byte) for byte in data)


def revert_byte_to_hex_str(data):
    # 45 E1 70 E5  ->  "0xe570e145"
    _str = '0x'
    index = len(data)
    for i in range(len(data)):
        index -= 1
        _str += hex(data[index])[2:]
    return _str
