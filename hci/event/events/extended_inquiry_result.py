from enum import IntEnum
from struct import unpack_from

import construct
from hci.event import EventPacket
from hci.transforms import _bytes_to_hex_string
from hci.const.gap_assigned_number import GAP_Assigned_Numbers

class HCI_Extended_Inquiry_Result(EventPacket):
    REPORT_DATA_OFFSET = 18

    @property
    def addr(self):
        OFFSET, SIZE_OCTETS = 4, 6
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return data[::-1]

    @property
    def rssi(self):
        OFFSET, SIZE_OCTETS = 17, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', data)[0]

    @property
    def adv_len_total(self):
        OFFSET, SIZE_OCTETS = 2, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', data)[0]

    @property
    def parse_eir(self):
        msg = ""
        offset = HCI_Extended_Inquiry_Result.REPORT_DATA_OFFSET
        total_len = self.adv_len_total
        data = self._get_data(0, total_len)
        while total_len > offset:
            L = unpack_from('<B', data[offset:offset+1])[0]
            if not L:
                break
            T = unpack_from('<B', data[offset+1:offset+2])[0]
            V = data[offset+2:offset+L+1]
            offset = offset+L+1
            if T == GAP_Assigned_Numbers.Complete_local_name or T == GAP_Assigned_Numbers.Short_Local_Name:
                msg += " Name:"+V.decode()
        return msg

    def __str__(self):
        return super().__str__() + ''.join(['\t{}\tRssi:{}dBm \t{}']).format(
            _bytes_to_hex_string(self.addr),
            self.rssi,
            self.parse_eir
        )
