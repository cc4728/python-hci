from ..command_packet import CommandPacket
from struct import pack, unpack
from hci.transforms import revert_byte_to_hex_str

class HCI_LE_Enable_Encryption(CommandPacket):
    def __init__(self):
        # TODO generate cmd
        super().__init__()

    @property
    def handle(self):
        OFFSET, SIZE_OCTETS = 4, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def long_term_key(self):
        OFFSET, SIZE_OCTETS = 16, 16
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return revert_byte_to_hex_str(unpack('<16B', data))

    def __str__(self):
        return super().__str__() + ''.join([
            'handle:{}',
            'LTK:{}'
        ]).format(
            hex(self.handle).ljust(10),
            self.long_term_key,
        )

