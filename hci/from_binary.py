from struct import unpack_from, error

from .hci_packet import HciPacket
from .asynchronous import AsynchronousDataPacket
from .command import CommandPacket
from .event import EventPacket
from .ISO import ISOPackage
from .synchronous import eSCOPackage
from .autocast import _autocast


def _parse_pkt_length(buf, pkt_type, pkt_offset):
    if pkt_type == HciPacket.PacketType.COMMAND:
        offset_data_length = CommandPacket.OFFSET_DATA_LENGTH
        offset = pkt_offset + offset_data_length
        data_length = unpack_from('<B', buf, offset=offset)[0]
        pkt_length = CommandPacket.DATA_LENGTH_OCTET + offset_data_length + data_length
    elif pkt_type == HciPacket.PacketType.EVENT:
        offset_data_length = EventPacket.OFFSET_DATA_LENGTH
        offset = pkt_offset + offset_data_length
        data_length = unpack_from('<B', buf, offset=offset)[0]
        pkt_length = EventPacket.DATA_LENGTH_OCTET + offset_data_length + data_length
    elif pkt_type == HciPacket.PacketType.ASYNCHRONOUS_DATA:
        offset_data_length = AsynchronousDataPacket.OFFSET_DATA_LENGTH
        offset = pkt_offset + offset_data_length
        data_length = unpack_from('<H', buf, offset=offset)[0]
        pkt_length = AsynchronousDataPacket.DATA_LENGTH_OCTET + offset_data_length + data_length
    elif pkt_type == HciPacket.PacketType.ISO_DATA:
        offset_data_length = ISOPackage.OFFSET_DATA_LENGTH
        offset = pkt_offset + offset_data_length
        data_length = unpack_from('<H', buf, offset=offset)[0]
        pkt_length = ISOPackage.DATA_LENGTH_OCTET + offset_data_length + data_length
    elif pkt_type == HciPacket.PacketType.SYNCHRONOUS_DATA:
        offset_data_length = eSCOPackage.OFFSET_DATA_LENGTH
        offset = pkt_offset + offset_data_length
        data_length = unpack_from('<H', buf, offset=offset)[0]
        pkt_length = eSCOPackage.DATA_LENGTH_OCTET + offset_data_length + data_length
    else:
        raise NotImplementedError(pkt_type)

    return pkt_length


def _parse_pkt_type(buf, pkt_offset):
    return unpack_from('<B', buf, offset=pkt_offset)[0]

pre_h = 0

def _parse_date(buf):
    global pre_h
    time = unpack_from('>Q', buf, offset=16)[0]
    us = time - int(time / 1000000) * 1000000
    tmp = int((time - us) / 1000000)  #s
    s = tmp - int((tmp / 60)) * 60
    tmp = int((tmp-s) / 60)           #m
    m = tmp - int(tmp / 60) * 60
    tmp = int((tmp - s) / 60)         #h
    d = int(tmp / 24)
    h = tmp - d * 24

    # fix btsnoop log bug
    if pre_h > h:
        h = pre_h
    pre_h = h
    us_str = str(us)
    us_str = us_str[:4]
    time_s = str(h).zfill(2) + ":" + str(m).zfill(2)+":"+str(s).zfill(2)+"."+us_str
    return time_s


def from_binary(buf):
    PACKET_TYPE_SIZE_OCTETS = 1
    PACKET_HEADER_SIZE_OCTETS = 24
    pkts = []
    pkt_offset = 0
    incomplete_pkt_data = b''

    while (pkt_offset < len(buf) and len(buf) > PACKET_HEADER_SIZE_OCTETS):
        try:
            pkt_offset += PACKET_HEADER_SIZE_OCTETS
            pkt_type = _parse_pkt_type(buf, pkt_offset)
            pkt_length = _parse_pkt_length(buf, pkt_type, pkt_offset)
        except error:
            incomplete_pkt_data = buf[pkt_offset:]
            break

        pkt_data = buf[pkt_offset:pkt_offset + pkt_length]
        pkt_timestamp = _parse_date(buf[pkt_offset-PACKET_HEADER_SIZE_OCTETS:pkt_offset])

        if (len(pkt_data) < pkt_length):
            incomplete_pkt_data = pkt_data
            break

        pkt = HciPacket(pkt_type, pkt_data[PACKET_TYPE_SIZE_OCTETS:],pkt_timestamp)
        pkt = _autocast(pkt)
        pkts.append(pkt)
        #if pkt_type == 4:
        #    print(pkt)
        pkt_offset += pkt_length
    return pkts, incomplete_pkt_data
