from enum import IntEnum

"""
Bluetooth Assigned Numbers:Generic Access Profile
"""


class GAP_Assigned_Numbers(IntEnum):
    Flags = 0x01
    Incomplete_16bit_Service = 0x02
    Complete_16bit_Service = 0x03
    InComplete_32bit_Service = 0x04
    Complete_32bit_Service = 0x05
    InComplete_128bit_Service = 0x06
    Complete_128bit_Service = 0x07
    Short_Local_Name = 0x08
    Complete_local_name = 0x09
    TX_power_level = 0x0a
    Class_of_device = 0x0d
    Simple_paring_Hash_C = 0x0e
    Device_ID = 0x10
    Service_Data = 0x16
    Public_target_address = 0x17
    Random_target_address = 0x18
    Appearance = 0x19
    Adv_interval = 0x1a
    LE_role = 0x1c
    Simple_paring_Hash_C_256 = 0x1d
    LE_Supported_Feature = 0x27
    Channel_Map_Updata_Ind = 0x28
    PB_ADV = 0x29
    Mesh_message = 0x2a
    Mesh_Beacon = 0x2b
    BIGInfo = 0x2c
    Broadcast_Code = 0x2d