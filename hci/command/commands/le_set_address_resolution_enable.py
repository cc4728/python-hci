from struct import pack, unpack
from enum import IntEnum

from ..command_packet import CommandPacket


class HCI_LE_Set_Address_Resolution_Enable(CommandPacket):

    class EnableStatus(IntEnum):
        Disable = 0
        Enable = 1

    def __init__(self):
        # TODO generate cmd
        super().__init__()

    @property
    def status(self):
        OFFSET, SIZE_OCTETS = 4, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    def __str__(self):
        return super().__str__()+''.join(['{}']).\
            format(HCI_LE_Set_Address_Resolution_Enable.EnableStatus(self.status).name,)




