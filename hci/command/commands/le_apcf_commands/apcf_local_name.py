from ..le_apcf_command_pkt import LE_APCF_Command
from struct import pack, unpack
from enum import IntEnum

"""
This pare base on spec <<Android BT HCI Requirement for BLE feature>> v0.52
Advertisement Package Content filter
"""


class APCF_Local_Name(LE_APCF_Command):

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
    def local_name(self):
        OFFSET = 7
        data = self._get_data(OFFSET)
        return data.decode()

    def __str__(self):
        return super().__str__()+''.join(['{}index:{}name:{}']).format(
            LE_APCF_Command.Action(self.action).name.ljust(10),
            str(self.index).ljust(8),
            self.local_name,)
