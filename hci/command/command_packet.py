from struct import pack, unpack
from enum import IntEnum

from ..hci_packet import HciPacket
from .opcode import OpCode,Vendor_Specific,LeControlCommands,LinkPolicyCommands,LinkControlCommands,\
    ControllerAndBasebandCommands,TestingCommands,StatusParameters,InformationalParameters

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
    OpCode = OpCode
    OpCodeName = 'UnKnow'
    OfgName = 'UnKnow'

    class Ogf(IntEnum):
        LINK_CONTROL = 1
        LINK_POLICY = 2
        CONTROLLER_AND_BASEBAND = 3
        INFORMATIONAL_PARAMETERS = 4
        STATUS_PARAMETERS = 5
        TESTING = 6
        LE_CONTROLLER = 8
        VENDOR_SPECIFIC = 63

    Ogf2Class = {
        Ogf.LINK_CONTROL:LinkControlCommands,
        Ogf.LINK_POLICY:LinkPolicyCommands,
        Ogf.CONTROLLER_AND_BASEBAND:ControllerAndBasebandCommands,
        Ogf.INFORMATIONAL_PARAMETERS:InformationalParameters,
        Ogf.STATUS_PARAMETERS:StatusParameters,
        Ogf.TESTING:TestingCommands,
        Ogf.LE_CONTROLLER:LeControlCommands,
        Ogf.VENDOR_SPECIFIC:Vendor_Specific,
    }

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
    def ogf(self):
        return (self.opcode >> 10)

    @property
    def ogf_name(self):
        if self.ogf in CommandPacket.Ogf._value2member_map_:
            self.OfgName = CommandPacket.Ogf(self.ogf).name
        return self.OfgName

    @property
    def ocf(self):
        return self.opcode & 0x3FF

    @property
    def opcode_name(self):
        if self.ogf in CommandPacket.Ogf._value2member_map_:
            if self.ocf in CommandPacket.Ogf2Class[self.ogf]._value2member_map_:
                self.OpCodeName = CommandPacket.Ogf2Class[self.ogf](self.ocf).name
        return self.OpCodeName

    @property
    def parameter_total_length(self):
        OFFSET, SIZE_OCTETS = 3, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            '   OpCode: {} ({})',
            '   OGF: {} ({})    OCF: {} ({})    Length: {} ({})'
        ]).format(
            hex(self.opcode),
            self.opcode_name,
            hex(self.ogf),
            self.ogf_name,
            hex(self.ocf),
            int(self.ocf),
            hex(self.parameter_total_length),
            int(self.parameter_total_length),
        )
