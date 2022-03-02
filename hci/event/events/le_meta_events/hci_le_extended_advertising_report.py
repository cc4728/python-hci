from enum import IntEnum
from struct import unpack_from

import construct

from ..le_meta_event_pkt import LE_Meta_Events
from hci.transforms import _bytes_to_hex_string
from hci.const.gap_assigned_number import GAP_Assigned_Numbers


class HCI_LE_Extended_Advertising_Report(LE_Meta_Events):
    ADV_DATA_OFFSET = 29
    SubCodeName = None

    class Event_Type(IntEnum):
        ADV_IND = 0x13
        ADV_DIRECT_IND = 0x15
        ADV_SCAN_IND =0x12
        ADV_NONCONN_IND = 0x10
        SCAN_RSP_to_ADV_IND = 0x1b
        SCAN_RSP_to_ADV_SCAN_IND = 0x1a

    class DeviceType(IntEnum):
        Public = 0
        Random = 1
        PublicIdentify = 2
        RandomIdentify = 3

    @property
    def num_report(self):
        OFFSET, SIZE_OCTETS = 4, 1
        event = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', event)[0]

    @property
    def sub_name(self):
        if not self.SubCodeName:
            self.SubCodeName = self.LE_META_EVENTS(self.sub_event).name
        return self.SubCodeName

    @property
    def event_type(self):
        OFFSET, SIZE_OCTETS = 5, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', data)[0]

    @property
    def addr_type(self):
        OFFSET, SIZE_OCTETS = 7, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', data)[0]

    @property
    def addr(self):
        OFFSET, SIZE_OCTETS = 8, 6
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return data[::-1]

    @property
    def rssi(self):
        OFFSET, SIZE_OCTETS = 18, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', data)[0]

    @property
    def adv_len_total(self):
        OFFSET, SIZE_OCTETS = 28, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', data)[0]

    @property
    def type_name(self,code):
        if code in GAP_Assigned_Numbers._value2member_map_:
            type = GAP_Assigned_Numbers(code).name
        else:
            type = str(hex(code))
        return type


    @property
    def get_adv_data(self):
        OFFSET, SIZE_OCTETS = HCI_LE_Extended_Advertising_Report.ADV_DATA_OFFSET, self.adv_len_total
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return data

    def parse_adv(self,data,length):
        msg = ""
        offset = 0
        while length > offset:
            L = unpack_from('<B', data[offset:offset+1])[0]
            if not L :
                break
            T = unpack_from('<B', data[offset+1:offset+2])[0]
            V = data[offset+2:offset+L+1]
            offset = offset+L+1
            if T == GAP_Assigned_Numbers.Complete_local_name or T == GAP_Assigned_Numbers.Short_Local_Name:
                msg += " Name:"+V.decode()
        return msg


    def __str__(self):
        return super().__str__() + ''.join([' Num:{}\t{}\t{}({})\tRssi:{}dBm {}']).format(
            self.num_report,
            HCI_LE_Extended_Advertising_Report.Event_Type(self.event_type).name.ljust(18),
            _bytes_to_hex_string(self.addr),
            HCI_LE_Extended_Advertising_Report.DeviceType(self.addr_type).name,
            self.rssi,
            self.parse_adv(self.get_adv_data, self.adv_len_total),
        )
