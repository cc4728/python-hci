from ..command_packet import CommandPacket
from struct import pack, unpack
from enum import IntEnum

"""
This pare base on spec <<Android BT HCI Requirement for BLE feature>> v0.52
Advertisement Package Content filter
"""


class LE_APCF_Command(CommandPacket):
    subOpcodeName = None

    class SubOpcode(IntEnum):
        APCF_Enable = 0
        APCF_Set_Filter_parameters = 1
        APCF_Broadcaster_Address = 2
        APCF_Service_UUID = 3
        APCF_Service_Solicitation_UUID = 4
        APCF_Local_Name = 5
        APCF_Manufacturer_Data = 6
        APCF_Service_Data = 7

    class Action(IntEnum):
        Add = 0
        Delete = 1
        Clear = 2

    def __init__(self):
        # TODO generate cmd
        super().__init__()

    @property
    def get_sub_opcode(self):
        OFFSET, SIZE_OCTETS = 4, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    @property
    def sub_name(self):
        if not self.subOpcodeName:
            self.subOpcodeName = LE_APCF_Command.SubOpcode(self.get_sub_opcode).name
        return self.subOpcodeName

    def __str__(self):
        return super().__str__()+''.join(['{}']).format(self.sub_name.ljust(28))
