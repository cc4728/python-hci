from ..command_packet import CommandPacket
from struct import pack, unpack
from enum import IntEnum

class HCI_LE_Set_Extended_Scan_Enable(CommandPacket):

    class Enable(IntEnum):
        Disable = 0
        Enable = 1

    def __init__(self):
        # TODO generate cmd
        super().__init__()

    @property
    def _enable(self):
        OFFSET, SIZE_OCTETS = 4, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]


    def __str__(self):
        return super().__str__()+''.join(['{}']).format(HCI_LE_Set_Extended_Scan_Enable.Enable(self._enable).name)


