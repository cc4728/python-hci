from ..command_packet import CommandPacket
from struct import pack, unpack

class HCI_LE_Set_Resolvable_Private_Address_Timeout(CommandPacket):

    class APCF_Opcode(IntEnum):
        Set_Filtering_parameters  = 0x01
        Enable = 0x00
        Local_Name = 0x05



    def __init__(self):
        # TODO generate cmd
        super().__init__()

    def __str__(self):
        return super().__str__()