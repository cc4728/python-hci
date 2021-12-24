from ..le_apcf_command_pkt import LE_APCF_Command
from struct import pack, unpack
from enum import IntEnum

"""
This pare base on spec <<Android BT HCI Requirement for BLE feature>> v0.52
Advertisement Package Content filter
"""


class APCF_Set_Filter_parameters(LE_APCF_Command):
    class Logic_Type(IntEnum):
        OR = 0
        AND = 1

    class Delivery_Mode(IntEnum):
        immediate = 0
        on_found = 1
        batched = 2

    class APCF_Feature_Selection(IntEnum):
        enable_Broadcast_Address_filter = 0
        enable_Service_Data_Change_filter =2
        enable_Service_UUID_check = 4
        enable_Service_Solicitation_UUID_check = 8
        enable_Local_Name_check = 16
        enable_Manufacturer_Data_check = 32
        enable_Service_Data_check = 64

    def __init__(self):
        # TODO generate cmd
        super().__init__()

    @property
    def action(self):
        OFFSET, SIZE_OCTETS = 5, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def index(self):
        OFFSET, SIZE_OCTETS = 6, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def selection(self):
        OFFSET, SIZE_OCTETS = 7, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def logic(self):
        OFFSET, SIZE_OCTETS = 9, 2
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<H', data)[0]

    @property
    def filter_logic(self):
        OFFSET, SIZE_OCTETS = 11, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def rssi_high_threshold(self):
        OFFSET, SIZE_OCTETS = 12, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def deliver_mode(self):
        OFFSET, SIZE_OCTETS = 13, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def msg(self):
        msg = ''
        if self.action == 0:
            msg += APCF_Set_Filter_parameters.APCF_Feature_Selection(self.selection).name.ljust(20)
        else:
            pass
        return msg

    def __str__(self):
        return super().__str__()+''.join(['{}index:{}{}']).format(
            LE_APCF_Command.Action(self.action).name.ljust(10),
            str(self.index).ljust(8),
            self.msg,)
