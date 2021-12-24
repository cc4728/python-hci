from ..le_apcf_command_pkt import LE_APCF_Command
from struct import pack, unpack
from enum import IntEnum

"""
This pare base on spec <<Android BT HCI Requirement for BLE feature>> v0.52
Advertisement Package Content filter
"""


class APCF_Broadcaster_Address(LE_APCF_Command):
    def __init__(self):
        # TODO generate cmd
        super().__init__()

    def __str__(self):
        return super().__str__()+''.join(['{}']).format("")