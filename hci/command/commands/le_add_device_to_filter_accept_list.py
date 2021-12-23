from struct import pack, unpack
from enum import IntEnum
from ..command_packet import CommandPacket
from hci.transforms import _bytes_to_hex_string

class HCI_LE_Add_Device_To_Filter_Accept_List(CommandPacket):

    class DeviceType(IntEnum):
        Public = 0
        Random = 1
        PublicIdentify = 2
        RandomIdentify = 3

    def __init__(self):
        # TODO generate cmd
        super().__init__()

    @property
    def peer_addr(self):
        OFFSET, SIZE_OCTETS = 5, 6
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return data[::-1]

    @property
    def addr_type_peer(self):
        OFFSET, SIZE_OCTETS = 4, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    def __str__(self):
        return super().__str__() + '\n'.join(['{}({})'])\
            .format(_bytes_to_hex_string(self.peer_addr),
            HCI_LE_Add_Device_To_Filter_Accept_List.DeviceType(self.addr_type_peer).name)

