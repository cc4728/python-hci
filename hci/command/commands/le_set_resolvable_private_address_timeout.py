from ..command_packet import CommandPacket
from struct import pack, unpack

class HCI_LE_Set_Resolvable_Private_Address_Timeout(CommandPacket):
    def __init__(self):
        # TODO generate cmd
        super().__init__()

    @property
    def rpa_timeout(self):
        OFFSET, SIZE_OCTETS = 4, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    def __str__(self):
        return super().__str__() + '\n'.join(['RPA_Timeout:{}s']).format(self.rpa_timeout)

