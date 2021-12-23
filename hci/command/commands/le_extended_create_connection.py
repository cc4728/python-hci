from struct import pack, unpack
from enum import IntEnum

from ..command_packet import CommandPacket
from hci.transforms import _hex_string_to_bytes
from hci.transforms import _bytes_to_hex_string

class HCI_LE_Extended_Create_Connection(CommandPacket):

    CONN_PARAMS_LENGTH = 16

    class InitFilter(IntEnum):
        UnUsed = 0
        Used = 1

    class DeviceType(IntEnum):
        Public = 0
        Random = 1
        PublicIdentify = 2
        RandomIdentify = 3

    def __init__(self, params):
        # TODO generate cmd
        super().__init__()

    @staticmethod
    def _params_to_binary(params):
        return params

    @property
    def addr_type_peer(self):
        OFFSET, SIZE_OCTETS = 6, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def peer_addr(self):
        OFFSET, SIZE_OCTETS = 7, 6
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return data[::-1]

    def parse_conn_params(self,offset):
        msg = ''
        scan_interval = unpack('<H', self._get_data(offset, 2))[0]
        offset += 2
        scan_win = unpack('<H', self._get_data(offset, 2))[0]
        offset += 2
        conn_interval_max = unpack('<H', self._get_data(offset, 2))[0]
        offset += 2
        conn_interval_min = unpack('<H', self._get_data(offset, 2))[0]
        offset += 2
        latency = unpack('<H', self._get_data(offset, 2))[0]
        offset += 2
        timeout = unpack('<H', self._get_data(offset, 2))[0]
        offset += 2
        min_ce = unpack('<H', self._get_data(offset, 2))[0]
        offset += 2
        max_ce = unpack('<H', self._get_data(offset, 2))[0]
        msg += 'scan_interval:{} ms\n\t\t' \
               'scan_win:{} ms\n\t\t' \
               'conn_interval_max:{} ms\n\t\t' \
               'conn_interval_min:{} ms\n\t\t' \
               'latency:{}\n\t\t' \
               'timeout:{} ms\n\t\t' \
               'min_ce:{} ms\n\t\t' \
               'max_ce:{} ms\n\t'.format(
                int(scan_interval)*0.625,
                int(scan_win)*0.625,
                int(conn_interval_max)*1.25,
                int(conn_interval_min)*1.25,
                int(latency),
                int(timeout)*10,
                int(min_ce)*0.625,
                int(max_ce)*0.625,)
        return msg

    @property
    def conn_params(self):
        msg = '\t'
        OFFSET, SIZE_OCTETS = 13, 1
        status = unpack('<B', self._get_data(OFFSET, SIZE_OCTETS))[0]
        OFFSET += 1
        if status & 4:
            msg += "Codec\n\t\t"
            msg += self.parse_conn_params(OFFSET)
            OFFSET += HCI_LE_Extended_Create_Connection.CONN_PARAMS_LENGTH
        if status & 2:
            msg += "Phy_1m\n\t\t"
            msg += self.parse_conn_params(OFFSET)
            OFFSET += HCI_LE_Extended_Create_Connection.CONN_PARAMS_LENGTH
        if status & 1:
            msg += "Phy_2m\n\t\t"
            msg += self.parse_conn_params(OFFSET)
        return msg

    def __str__(self):
        return super().__str__() + '\n'.join([
            '{} ({})',
            '   {}'
        ]).format(
            _bytes_to_hex_string(self.peer_addr),
            HCI_LE_Extended_Create_Connection.DeviceType(self.addr_type_peer).name,
            self.conn_params,
        )
