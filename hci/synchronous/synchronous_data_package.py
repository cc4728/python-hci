from ..hci_packet import HciPacket

"""
Description in bluetooth core spec v5.3:
    The HCI Synchronous Data packet header is the first 3 octets of the packet
    The Packet_Status_Flag bits consist of two bits, which are located from bit 4 to 5 in the second octet of the HCI Synchronous Data packet.
    
    0                       12   14   16                                31                   
    +------------------------+----+----+--------------------------------+----------------+
    |     Connection_Handle  | PS | RFU|        Length                  |      Data      |                
    +------------------------+----+----+--------------------------------+----------------+
"""

class eSCOPackage(HciPacket):
    OFFSET_DATA_LENGTH = 4