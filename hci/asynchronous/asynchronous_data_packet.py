from struct import pack, unpack
from ..hci_packet import HciPacket


class AsynchronousDataPacket(HciPacket):
    OFFSET_DATA_LENGTH = 0x03

    @property
    def data_length(self):
        OFFSET, SIZE_OCTETS = 3, 2
        data_length = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data_length)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            'Acl Data Length: {} ({})',
        ]).format(
            hex(self.data_length),
            int(self.data_length),
        )