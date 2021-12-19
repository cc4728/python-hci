from ..hci_packet import HciPacket

"""
Description in bluetooth core spec v5.3:
    The first 4 octets of every HCI ISO Data packet contain a 4-octet Header field
    The Header field consists of the least significant bits 0 to 11 (12 bits) as the Connection_Handle parameter, 
    bits 12 to 13 as the PB_Flag parameter, bit 14 as the TS_Flag parameter, bit 15 as an RFU bit, 
    bits 16 to 29 (14 bits) as the ISO_Data_Load_Length parameter, and bits 30 to 31 as RFU bits
    0                       12   14 15   16                       29   31                   
    +------------------------+----+--+---+------------------------+----+--------------------+
    |     Connection_Handle  | PB |TS|RFU|        Length          | RFU|   ISO_Data_Load    |                
    +------------------------+----+--+---+------------------------+----+--------------------+
"""


class ISOPackage(HciPacket):
    OFFSET_DATA_LENGTH = 4