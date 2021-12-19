from struct import pack, unpack
from ..hci_packet import HciPacket

"""
Description in bluetooth core spec v5.3:
    The HCI ACL Data packet header is the first 4 octets of the packet
    The Flag Bits consist of the Packet_Boundary_Flag and Broadcast_Flag.
    The Packet_Boundary_Flag is located in bit 4 and bit 5, 
    and the Broadcast_Flag is located in bit 6 and bit 7 in the second octet of the HCI ACL Data packet
    0                       12   14   16                                31                   
    +------------------------+----+----+--------------------------------+----------------+
    |     Handle             | PB | BC |        Length                  |      Data      |                
    +------------------------+----+----+--------------------------------+----------------+
"""


class AsynchronousDataPacket(HciPacket):
    OFFSET_DATA_LENGTH = 3

    @property
    def data_length(self):
        OFFSET, SIZE_OCTETS = 3, 2
        data_length = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data_length)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            '   Acl Length: {} ({})',
        ]).format(
            hex(self.data_length),
            int(self.data_length),
        )