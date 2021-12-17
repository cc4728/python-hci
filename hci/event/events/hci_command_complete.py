from enum import IntEnum
from struct import unpack_from

from .. import EventPacket
from hci.command.opcode import OpCode


class HCI_CommandComplete(EventPacket):
    OpCodeName = 'UnKnow'

    class Status(IntEnum):
        HCI_SUCCESS = 0x00
        HCI_FAILURE = 0x01
        HCI_ERROR_CODE_UNKNOWN_CONN_ID = 0x02
        HCI_ERROR_CODE_CMD_DISALLOWED = 0x0C
        HCI_ERROR_CODE_INVALID_HCI_CMD_PARAMS = 0x12
        HCI_ERROR_CODE_ROLE_CHANGE_NOT_ALLOWED = 0x21
        HCI_ERROR_CODE_MEM_CAP_EXCEEDED = 0x07
        HCI_ERROR_CODE_UNSUPPORTED_FEATURE_PARAM_VALUE = 0x11

    @property
    def packets(self):
        OFFSET, SIZE_OCTETS = 3, 1
        packets = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', packets)[0]

    @property
    def opcode(self):
        OFFSET, SIZE_OCTETS = 4, 2
        opcode = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<H', opcode)[0]

    @property
    def opcode_name(self):
        if self.opcode in OpCode._value2member_map_:
            self.OpCodeName = OpCode(self.opcode).name
        return self.OpCodeName

    @property
    def status(self):
        OFFSET, SIZE_OCTETS = 6, 1
        status = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', status)[0]

    @property
    def status_name(self):
        name = 'UnKnow'
        if self.status in HCI_CommandComplete.Status._value2member_map_:
            name = HCI_CommandComplete.Status(self.status).name
        return name

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            '   OpCode: {} ({})     Status: {} ({})']).format(
            hex(self.opcode),
            self.opcode_name,
            hex(self.status),
            self.status_name)
