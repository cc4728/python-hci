from ..command_packet import CommandPacket
from struct import pack, unpack
from hci.transforms import _bytes_to_hex_string


class HCI_Delete_Stored_Link_Key(CommandPacket):
    def __init__(self):
        # TODO generate cmd
        super().__init__()

    @property
    def peer_addr(self):
        OFFSET, SIZE_OCTETS = 4, 6
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return data[::-1]

    def __str__(self):
        return super().__str__() + '\n'.join(["{}"]).\
            format(_bytes_to_hex_string(self.peer_addr))