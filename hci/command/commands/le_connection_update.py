from ..command_packet import CommandPacket
from struct import pack, unpack

class HCI_LE_Connection_Update(CommandPacket):
    def __init__(self):
        # TODO generate cmd
        super().__init__()

    @property
    def handle(self):
        OFFSET, SIZE_OCTETS = 4, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def conn_params(self):
        offset = 6
        msg = ''
        conn_interval_min = unpack('<H', self._get_data(offset, 2))[0]
        offset += 2
        conn_interval_max = unpack('<H', self._get_data(offset, 2))[0]
        offset += 2
        latency = unpack('<H', self._get_data(offset, 2))[0]
        offset += 2
        timeout = unpack('<H', self._get_data(offset, 2))[0]
        offset += 2
        min_ce = unpack('<H', self._get_data(offset, 2))[0]
        offset += 2
        max_ce = unpack('<H', self._get_data(offset, 2))[0]
        msg += 'conn_interval_max:{} ms\n\t\t' \
               'conn_interval_min:{} ms\n\t\t' \
               'latency:{}\n\t\t' \
               'timeout:{} ms\n\t\t' \
               'min_ce:{} ms\n\t\t' \
               'max_ce:{} ms\n\t'.format(
                int(conn_interval_max)*1.25,
                int(conn_interval_min)*1.25,
                int(latency),
                int(timeout)*10,
                int(min_ce)*0.625,
                int(max_ce)*0.625,)
        return msg

    def __str__(self):
        return super().__str__() + '\n'.join([
            'handle:{}',
            '\t\t{}'
        ]).format(
            hex(self.handle),
            self.conn_params,
        )


