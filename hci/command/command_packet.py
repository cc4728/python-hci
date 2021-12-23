from struct import pack, unpack
from enum import IntEnum

from ..hci_packet import HciPacket
from .opcode import OpCode

"""
Description in bluetooth core spec v5.3:
    The HCI Command packet header is the first 3 octets of the packet.
    Each command is assigned a 2 byte Opcode used to uniquely identify different types of commands. 
    The Opcode parameter is divided into two fields, called the Opcode Group Field (OGF) and Opcode Command Field (OCF). 
    The OGF occupies the upper 6 bits of the Opcode, while the OCF occupies the remaining 10 bits. 
    Any opcode not mentioned in this Part is reserved for future use.
    The OGF value 0x3E is reserved for future use (used for specification development purposes).
    The OGF of 0x3F is reserved for vendor-specific debug commands
    +---------------------------------+----------------+----------------+
    |            opcode(2byte)        |                |                |
    +--------------------+------------+  length(1byte) |      data      |
    |      0CF(10bit)    | OGF(6bit)  |                |                |
    +--------------------+-----------------------------+----------------+
"""

class CommandPacket(HciPacket):
    OFFSET_DATA_LENGTH = 3
    DATA_LENGTH_OCTET = 1

    def __init__(self, opcode, parameters=b''):
        super().__init__(
            HciPacket.PacketType.COMMAND,
            CommandPacket._params_to_binary(opcode, parameters)
        )

    @staticmethod
    def _params_to_binary(opcode, parameters):
        fmt = '<HB%ds' % len(parameters)
        return pack(fmt, opcode, len(parameters), parameters)

    @property
    def opcode(self):
        OFFSET, SIZE_OCTETS = 1, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def parameter_total_length(self):
        OFFSET, SIZE_OCTETS = 3, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    def __str__(self):
        opCode = OpCode(self.opcode)
        if opCode.has():
            a = 1
        opcode_name ,ogf_name = opCode.name()

        return super().__str__() + '\n'.join(['{} {}']).format(opcode_name.ljust(50),ogf_name.ljust(10),)
