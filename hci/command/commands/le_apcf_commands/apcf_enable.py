from ..le_apcf_command_pkt import LE_APCF_Command
from struct import pack, unpack
from enum import IntEnum

"""
This pare base on spec <<Android BT HCI Requirement for BLE feature>> v0.52
Advertisement Package Content filter
"""


class APCF_Enable(LE_APCF_Command):

    class Enable_Status(IntEnum):
        Enabled = 1
        Disabled = 0

    def __init__(self):
        # TODO generate cmd
        super().__init__()

    @property
    def status(self):
        OFFSET, SIZE_OCTETS = 5, 1
        data = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack('<B', data)[0]

    def __str__(self):
        return super().__str__()+''.join(['{}']).format(APCF_Enable.Enable_Status(self.status).name)
