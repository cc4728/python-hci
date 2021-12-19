from enum import IntEnum
"""
    refs:BLUETOOTH CORE SPECIFICATION Version 5.3 | Vol 4, Part E
"""


class OpCode(IntEnum):
    LE_SET_EVENT_MASK = 0x2001
    LE_READ_BUFFER_SIZE = 0x2002
    LE_READ_LOCAL_SUPPORTED_FEATURES = 0x2003
    LE_SET_RANDOM_ADDRESS = 0x2005
    LE_SET_ADVERTISING_PARAMETERS = 0x2006
    LE_READ_ADVERTISING_CHANNEL_TX_POWER = 0x2007
    LE_SET_ADVERTISING_DATA = 0x2008
    LE_SET_SCAN_RESPONSE_DATA = 0x2009
    LE_SET_ADVERTISE_ENABLE = 0x200A
    LE_SET_SCAN_PARAMETERS = 0x200B
    LE_SET_SCAN_ENABLE = 0x200C
    LE_CREATE_CONNECTION = 0x200D
    LE_CREATE_CONNECTION_CANCEL = 0x200E
    LE_READ_WHITE_LIST_SIZE = 0x200F
    LE_CLEAR_WHITE_LIST = 0x2010
    LE_ADD_DEVICE_TO_WHITE_LIST = 0x2011
    LE_REMOVE_DEVICE_FROM_WHITE_LIST = 0x2012
    LE_CONNECTION_UPDATE = 0x2013
    LE_SET_HOST_CHANNEL_CLASSIFICATION = 0x2014
    LE_READ_CHANNEL_MAP = 0x2015
    LE_READ_REMOTE_USED_FEATURES = 0x2016
    LE_ENCRYPT = 0x2017
    LE_RAND = 0x2018
    LE_START_ENCRYPTION = 0x2019
    LE_LONG_TERM_KEY_REQUESTED_REPLY = 0x201A
    LE_LONG_TERM_KEY_REQUESTED_NEGATIVE_REPLY = 0x201B
    LE_READ_SUPPORTED_STATES = 0x201C
    LE_RECEIVER_TEST = 0x201D
    LE_TRANSMITTER_TEST = 0x201E
    LE_TEST_END_COMMAND = 0x201F
    LE_REMOTE_CONNECTION_PARAMETER_REQUEST_REPLY = 0x2020
    LE_REMOTE_CONNECTION_PARAMETER_REQUEST_NEGATIVE_REPLY = 0x2021
    LE_SET_DATA_LENGTH = 0x2022
    LE_READ_SUGGESTED_DEFAULT_DATA_LENGTH = 0x2023
    LE_WRITE_SUGGESTED_DEFAULT_DATA_LENGTH = 0x2024
    LE_READ_LOCAL_P256_PUBLIC_KEY = 0x2025
    LE_GENERATE_DHKEY = 0x2026
    LE_ADD_DEVICE_TO_RESOLVING_LIST = 0x2027
    LE_REMOVE_DEVICE_FROM_RESOLVING_LIST = 0x2028
    LE_CLEAR_RESOLVING_LIST = 0x2029
    LE_READ_RESOLVING_LIST_SIZE = 0x202A
    LE_READ_PEER_RESOLVABLE_ADDRESS = 0x202B
    LE_READ_LOCAL_RESOLVABLE_ADDRESS = 0x202C
    LE_SET_ADDRESS_RESOLUTION_ENABLE = 0x202D
    LE_SET_RESOLVABLE_PRIVATE_ADDRESS_TIMEOUT = 0x202E
    LE_READ_MAXIMUM_DATA_LENGTH = 0x202F
    LE_SET_DEFAULT_PHY = 0x2031
    LE_SET_PHY = 0x2032
    LE_EXTENDED_CREATE_CONNECTION = 0x2043

    DISCONNECT = 0x0406
    READ_REMOTE_VERSION_INFORMATION = 0x041D
    SET_EVENT_MASK = 0x0C01
    HCI_RESET = 0x0C03
    READ_TRANSMIT_POWER_LEVEL = 0x0C2D
    SET_CONTROLLER_TO_HOST_FLOW_CONTROL = 0x0C31
    HOST_BUFFER_SIZE = 0x0C33
    HOST_NUMBER_OF_COMPLETED_PACKETS = 0x0C35
    SET_EVENT_MASK_PAGE_2 = 0x0C63
    READ_AUTHENTICATED_PAYLOAD_TIMEOUT = 0x0C7B
    WRITE_AUTHENTICATED_PAYLOAD_TIMEOUT = 0x0C7C
    READ_LOCAL_VERSION_INFORMATION = 0x1001
    READ_LOCAL_SUPPORTED_COMMANDS = 0x1002
    READ_LOCAL_SUPPORTED_FEATURES = 0x1003
    READ_BD_ADDR = 0x1009
    READ_RSSI = 0x1405
    READ_BUFFER_SIZE = 0x1005
    READ_LOCAL_EXTENDED_FEATURE = 0x1004
    WRITE_SIMPLE_PAIRING_MODE = 0x0c56
    WRITE_LE_HOST_SUPPORT = 0x0C6D
    WRITE_SECURE_CONNECTIONS_HOST_SUPPORT = 0x0C7A

    HCI_EXTENSION_SET_RX_GAIN = 0xFC00
    HCI_EXTENSION_SET_TX_POWER = 0xFC01
    HCI_EXTENSION_ONE_PACKET_PER_EVENT = 0xFC02
    HCI_EXTENSION_CLOCK_DIVIDE_ON_HALT = 0xFC03
    HCI_EXTENSION_DECLARE_NV_USAGE = 0xFC04
    HCI_EXTENSION_DECRYPT = 0xFC05
    HCI_EXTENSION_SET_LOCAL_SUPPORTED_FEATURES = 0xFC06
    HCI_EXTENSION_SET_FAST_TX_RESPONSE_TIME = 0xFC07
    HCI_EXTENSION_MODEM_TEST_TX = 0xFC08
    HCI_EXTENSION_MODEM_HOP_TEST_TX = 0xFC09
    HCI_EXTENSION_MODEM_TEST_RX = 0xFC0A
    HCI_EXTENSION_END_MODEM_TEST = 0xFC0B
    HCI_EXTENSION_SET_BDADDR = 0xFC0C
    HCI_EXTENSION_SET_SCA = 0xFC0D
    HCI_EXTENSION_ENABLE_PTM1 = 0xFC0E
    HCI_EXTENSION_SET_FREQUENCY_TUNING = 0xFC0F
    HCI_EXTENSION_SAVE_FREQUENCY_TUNING = 0xFC10
    HCI_EXTENSION_SET_MAX_DTM_TX_POWER = 0xFC11
    HCI_EXTENSION_MAP_PM_IO_PORT = 0xFC12
    HCI_EXTENSION_DISCONNECT_IMMEDIATE = 0xFC13
    HCI_EXTENSION_PACKET_ERROR_RATE = 0xFC14
    HCI_EXTENSION_PACKET_ERROR_RATE_BY_CHANNEL1 = 0xFC15
    HCI_EXTENSION_EXTEND_RF_RANGE = 0xFC16
    HCI_EXTENSION_ADVERTISER_EVENT_NOTICE = 0xFC17
    HCI_EXTENSION_CONNECTION_EVENT_NOTICE = 0xFC18
    HCI_EXTENSION_HALT_DURING_RF = 0xFC19
    HCI_EXTENSION_SET_SLAVE_LATENCY_OVERRIDE = 0xFC1A
    HCI_EXTENSION_BUILD_REVISION = 0xFC1B
    HCI_EXTENSION_DELAY_SLEEP = 0xFC1C
    HCI_EXTENSION_RESET_SYSTEM = 0xFC1D
    HCI_EXTENSION_OVERLAPPED_PROCESSING = 0xFC1E
    HCI_EXTENSION_NUMBER_COMPLETED_PACKETS_LIMIT = 0xFC1F
    HCI_EXTENSION_GET_CONNECTION_INFORMATION = 0xFC20
    HCI_EXTENSION_SET_MAX_DATA_LENGTH = 0xFC21
    HCI_EXTENSION_SCAN_EVENT_NOTICE = 0xFC22
    HCI_EXTENSION_SCAN_REQUEST_REPORT = 0xFC23

    L2CAP_DISCONNECTION_REQUEST = 0xFC86
    L2CAP_CONNECTION_PARAMETER_UPDATE_REQUEST = 0xFC92
    L2CAP_CONNECTION_REQUEST = 0xFC94
    L2CAP_CONNECTION_RESPONSE = 0xFC95
    L2CAP_FLOW_CONTROL_CREDIT = 0xFC96
    L2CAP_DATA = 0xFCF0
    L2CAP_REGISTER_PSM = 0xFCF1
    L2CAP_DEREGISTER_PSM = 0xFCF2
    L2CAP_PSM_INFO = 0xFCF3
    L2CAP_PSM_CHANNELS = 0xFCF4
    L2CAP_CHANNEL_INFO = 0xFCF5

    ATT_ERROR_RESPONSE = 0xFD01
    ATT_EXCHANGE_MTU_REQUEST = 0xFD02
    ATT_EXCHANGE_MTU_RESPONSE = 0xFD03
    ATT_FIND_INFORMATION_REQUEST = 0xFD04
    ATT_FIND_INFORMATION_RESPONSE = 0xFD05
    ATT_FIND_BY_TYPE_VALUE_REQUEST = 0xFD06
    ATT_FIND_BY_TYPE_VALUE_RESPONSE = 0xFD07
    ATT_READ_BY_TYPE_REQUEST = 0xFD08
    ATT_READ_BY_TYPE_RESPONSE = 0xFD09
    ATT_READ_REQUEST = 0xFD0A
    ATT_READ_RESPONSE = 0xFD0B
    ATT_READ_BLOB_REQUEST = 0xFD0C
    ATT_READ_BLOB_RESPONSE = 0xFD0D
    ATT_READ_MULTIPLE_REQUEST = 0xFD0E
    ATT_READ_MULTIPLE_RESPONSE = 0xFD0F
    ATT_READ_BY_GROUP_TYPE_REQUEST = 0xFD10
    ATT_READ_BY_GROUP_TYPE_RESPONSE = 0xFD11
    ATT_WRITE_REQUEST = 0xFD12
    ATT_WRITE_RESPONSE = 0xFD13
    ATT_PREPARE_WRITE_REQUEST = 0xFD16
    ATT_PREPARE_WRITE_RESPONSE = 0xFD17
    ATT_EXECUTE_WRITE_REQUEST = 0xFD18
    ATT_EXECUTE_WRITE_RESPONSE = 0xFD19
    ATT_HANDLE_VALUE_NOTIFICATION = 0xFD1B
    ATT_HANDLE_VALUE_INDICATION = 0xFD1D
    ATT_HANDLE_VALUE_CONFIRMATION = 0xFD1E

    GATT_DISC_ALL_CHAR_DESCS = 0xFD84
    GATT_DISCOVER_CHARACTERISTICS_BY_UUID = 0xFD88
    GATT_READ = 0xFD8A
    GATT_WRITE = 0xFD92
    GATT_WRITE_LONG = 0xFD96

    GAP_DEVICE_INITIALIZATION = 0xFE00
    GAP_CONFIGURE_DEVICE_ADDRESS = 0xFE03
    GAP_DEVICE_DISCOVERY_REQUEST = 0xFE04
    GAP_DEVICE_DISCOVERY_CANCEL = 0xFE05
    GAP_MAKE_DISCOVERABLE = 0xFE06
    GAP_UPDATE_ADVERTISING_DATA = 0xFE07
    GAP_END_DISCOVERABLE = 0xFE08
    GAP_ESTABLISH_LINK_REQUEST = 0xFE09
    GAP_TERMINATE_LINK_REQUEST = 0xFE0A
    GAP_AUTHENTICATE = 0xFE0B
    GAP_PASSKEY_UPDATE = 0xFE0C
    GAP_SLAVE_SECURITY_REQUEST = 0xFE0D
    GAP_SIGNABLE = 0xFE0E
    GAP_BOND = 0xFE0F
    GAP_TERMINATE_AUTH = 0xFE10
    GAP_UPDATE_LINK_PARAMETER_REQUEST = 0xFE11
    GAP_UPDATE_LINK_PARAMETER_REQUEST_REPLY = 0xFE12
    GAP_SET_PARAMETER = 0xFE30
    GAP_GET_PARAMETER = 0xFE31
    GAP_RESOLVE_PRIVATE_ADDRESS = 0xFE32
    GAP_SET_ADVERTISEMENT_TOKEN = 0xFE33
    GAP_REMOVE_ADVERTISEMENT_TOKEN = 0xFE34
    GAP_UPDATE_ADVERTISEMENT_TOKENS = 0xFE35
    GAP_BOND_SET_PARAMETER = 0xFE36
    GAP_BOND_GET_PARAMETER = 0xFE37

    UTIL_RESERVED = 0xFE80
    UTIL_NV_READ = 0xFE81
    UTIL_NV_WRITE = 0xFE82
    UTIL_FORCE_BOOT = 0xFE83
    UTIL_BUILD_REVISION = 0xFE84

    RESERVED = 0xFF00

    USER_PROFILES = 0xFF80


class LinkControlCommands(IntEnum):
    """
    LINK CONTROL COMMANDS
    OGF:0X01
    """
    HCI_Inquiry = 0x0001
    HCI_Inquiry_Cancel = 0x0002
    HCI_Periodic_Inquiry_Mode = 0x0003
    HCI_Exit_Periodic_Inquiry_Mode = 0x0004
    HCI_Create_Connection = 0x0005
    HCI_Disconnect = 0x0006
    HCI_Create_Connection_Cancel = 0x0008
    HCI_Accept_Connection_Request = 0x0009
    HCI_Reject_Connection_Request = 0x000A
    HCI_Link_Key_Request_Reply = 0x000B
    HCI_Link_Key_Request_Negative_Reply = 0x000C
    HCI_PIN_Code_Request_Reply = 0x000D
    HCI_PIN_Code_Request_Negative_Reply = 0x000E
    HCI_Change_Connection_Packet_Type = 0x000F
    HCI_Authentication_Requested = 0x0011
    HCI_Set_Connection_Encryption = 0x0013
    HCI_Change_Connection_Link_Key = 0x0015
    HCI_Link_Key_Selection = 0x0017
    HCI_Remote_Name_Request = 0x0019
    HCI_Remote_Name_Request_Cancel = 0x001A
    HCI_Read_Remote_Supported_Features = 0x001B
    HCI_Read_Remote_Extended_Features = 0x001C
    HCI_Read_Remote_Version_Information = 0x001D
    HCI_Read_Clock_Offset = 0x001F
    HCI_Read_LMP_Handle = 0x0020
    HCI_Setup_Synchronous_Connection = 0x0028
    HCI_Accept_Synchronous_Connection_Request = 0x0029
    HCI_Reject_Synchronous_Connection_Request = 0x002A
    HCI_IO_Capability_Request_Reply = 0x002B
    HCI_User_Confirmation_Request_Reply = 0x002C
    HCI_User_Confirmation_Request_Negative_Reply = 0x002D
    HCI_User_Passkey_Request_Reply = 0x002E
    HCI_User_Passkey_Request_Negative_Reply = 0x002F
    HCI_Remote_OOB_Data_Request_Reply = 0x0030
    HCI_Remote_OOB_Data_Request_Negative_Reply = 0x0033
    HCI_IO_Capability_Request_Negative_Reply = 0x0034
    HCI_Enhanced_Setup_Synchronous_Connection = 0x003D
    HCI_Enhanced_Accept_Synchronous_Connection_Request = 0x003E
    HCI_Truncated_Page = 0x003F
    HCI_Truncated_Page_Cancel = 0x0040
    HCI_Set_Connectionless_Peripheral_Broadcast = 0x0041
    HCI_Set_Connectionless_Peripheral_Broadcast_Receive = 0x0042
    HCI_Start_Synchronization_Train = 0x0043
    HCI_Receive_Synchronization_Train = 0x0044
    HCI_Remote_OOB_Extended_Data_Request_Reply = 0x0045


class LinkPolicyCommands(IntEnum):
    """
    LINK POLICY COMMANDS
    OGF:0X02
    """
    HCI_Hold_Mode = 0x0001
    HCI_Sniff_Mode = 0x0003
    HCI_Exit_Sniff_Mode = 0x0004
    HCI_QoS_Setup = 0x0007
    HCI_Role_Discovery = 0x0009
    HCI_Switch_Role = 0x000B
    HCI_Read_Link_Policy_Settings = 0x000C
    HCI_Write_Link_Policy_Settings = 0x000D
    HCI_Read_Default_Link_Policy_Settings = 0x000E
    HCI_Write_Default_Link_Policy_Settings = 0x000F
    HCI_Flow_Specification = 0x0010
    HCI_Sniff_Subrating = 0x0011


class ControllerAndBasebandCommands(IntEnum):
    """
    CONTROLLER & BASEBAND COMMANDS
    OGF:0X03
    """
    HCI_Set_Event_Mask = 0x0001
    HCI_Reset = 0x0003
    HCI_Set_Event_Filter = 0x0005
    HCI_Flush = 0x0008
    HCI_Read_PIN_Type = 0x0009
    HCI_Write_PIN_Type = 0x000A
    HCI_Read_Stored_Link_Key = 0x000D
    HCI_Write_Stored_Link_Key = 0x0011
    HCI_Delete_Stored_Link_Key = 0x0012
    HCI_Write_Local_Name = 0x0013
    HCI_Read_Local_Name = 0x0014
    HCI_Read_Connection_Accept_Timeout = 0x0015
    HCI_Write_Connection_Accept_Timeout = 0x0016
    HCI_Read_Page_Timeout = 0x0017
    HCI_Write_Page_Timeout = 0x0018
    HCI_Read_Scan_Enable = 0x0019
    HCI_Write_Scan_Enable = 0x001A
    HCI_Read_Page_Scan_Activity = 0x001B
    HCI_Write_Page_Scan_Activity = 0x001C
    HCI_Read_Inquiry_Scan_Activity = 0x001D
    HCI_Write_Inquiry_Scan_Activity = 0x001E
    HCI_Read_Authentication_Enable = 0x001F
    HCI_Write_Authentication_Enable = 0x0020
    HCI_Read_Class_Of_Device = 0x0023
    HCI_Write_Class_Of_Device = 0x0024
    HCI_Read_Voice_Setting = 0x0025
    HCI_Write_Voice_Setting = 0x0026
    HCI_Read_Automatic_Flush_Timeout = 0x0027
    HCI_Write_Automatic_Flush_Timeout = 0x0028
    HCI_Read_Num_Broadcast_Retransmissions = 0x0029
    HCI_Write_Num_Broadcast_Retransmissions = 0x002A
    HCI_Read_Hold_Mode_Activity = 0x002B
    HCI_Write_Hold_Mode_Activity = 0x002C
    HCI_Read_Transmit_Power_Level = 0x002D
    HCI_Read_Synchronous_Flow_Control_Enable = 0x002E
    HCI_Write_Synchronous_Flow_Control_Enable = 0x002F
    HCI_Set_Controller_To_Host_Flow_Control = 0x0031
    HCI_Host_Buffer_Size = 0x0033
    HCI_Host_Number_Of_Completed_Packets = 0x0035
    HCI_Read_Link_Supervision_Timeout = 0x0036
    HCI_Write_Link_Supervision_Timeout = 0x0037
    HCI_Read_Number_Of_Supported_IAC = 0x0038
    HCI_Read_Current_IAC_LAP = 0x0039
    HCI_Write_Current_IAC_LAP = 0x003A
    HCI_Set_AFH_Host_Channel_Classification = 0x003F
    HCI_Read_Inquiry_Scan_Type = 0x0042
    HCI_Write_Inquiry_Scan_Type = 0x0043
    HCI_Read_Inquiry_Mode = 0x0044
    HCI_Write_Inquiry_Mode = 0x0045
    HCI_Read_Page_Scan_Type = 0x0046
    HCI_Write_Page_Scan_Type = 0x0047
    HCI_Read_AFH_Channel_Assessment_Mode = 0x0048
    HCI_Write_AFH_Channel_Assessment_Mode = 0x0049
    HCI_Read_Extended_Inquiry_Response = 0x0051
    HCI_Write_Extended_Inquiry_Response = 0x0052
    HCI_Refresh_Encryption_Key = 0x0053
    HCI_Read_Simple_Pairing_Mode = 0x0055
    HCI_Write_Simple_Pairing_Mode = 0x0056
    HCI_Read_Local_OOB_Data = 0x0057
    HCI_Read_Inquiry_Response_Transmit_Power_Level = 0x0058
    HCI_Write_Inquiry_Transmit_Power_Leve = 0x0059
    HCI_Send_Keypress_Notification = 0x0060
    HCI_Read_Default_Erroneous_Data_Reporting = 0x005A
    HCI_Write_Default_Erroneous_Data_Reporting = 0x005B
    HCI_Enhanced_Flush = 0x005F
    HCI_Set_Event_Mask_Page_2 = 0x0063
    HCI_Read_Flow_Control_Mode = 0x0066
    HCI_Write_Flow_Control_Mode = 0x0067
    HCI_Read_Enhanced_Transmit_Power_Level = 0x0068
    HCI_Read_LE_Host_Support = 0x006C
    HCI_Write_LE_Host_Support = 0x006D
    HCI_Set_MWS_Channel_Parameters = 0x006E
    HCI_Set_External_Frame_Configuration = 0x006F
    HCI_Set_MWS_Signaling = 0x0070
    HCI_Set_MWS_Transport_Layer = 0x0071
    HCI_Set_MWS_Scan_Frequency_Table = 0x0072
    HCI_Set_MWS_PATTERN_Configuration = 0x0073
    HCI_Set_Reserved_LT_ADDR = 0x0074
    HCI_Delete_Reserved_LT_ADDR = 0x0075
    HCI_Set_Connectionless_Peripheral_Broadcast_Data = 0x0076
    HCI_Read_Synchronization_Train_Parameters = 0x0077
    HCI_Write_Synchronization_Train_Parameters = 0x0078
    HCI_Read_Secure_Connections_Host_Support = 0x0079
    HCI_Write_Secure_Connections_Host_Support = 0x007A
    HCI_Read_Authenticated_Payload_Timeout = 0x007B
    HCI_Write_Authenticated_Payload_Timeout = 0x007C
    HCI_Read_Local_OOB_Extended_Data = 0x007D
    HCI_Read_Extended_Page_Timeout = 0x007E
    HCI_Write_Extended_Page_Timeout = 0x007F
    HCI_Read_Extended_Inquiry_Length = 0x0080
    HCI_Write_Extended_Inquiry_Length = 0x0081
    HCI_Set_Ecosystem_Base_Interval = 0x0082
    HCI_Configure_Data_Path = 0x0083
    HCI_Set_Min_Encryption_Key_Size = 0x0084


class InformationalParameters (IntEnum):
    """
    INFORMATIONAL PARAMETERS
    OGF:0X04
    """
    HCI_Read_Local_Version_Information = 0x0001
    HCI_Read_Local_Supported_Commands = 0x0002
    HCI_Read_Local_Supported_Features = 0x0003
    HCI_Read_Local_Extended_Features = 0x0004
    HCI_Read_Buffer_Size = 0x0005
    HCI_Read_BD_ADDR = 0x0009
    HCI_Read_Data_Block_Size = 0x000A
    HCI_Read_Local_Supported_Codecs_v2 = 0x000D
    HCI_Read_Local_Supported_Codecs_v1 = 0x000B
    HCI_Read_Local_Simple_Pairing_Options = 0x000C
    HCI_Read_Local_Supported_Codec_Capabilities = 0x000E
    HCI_Read_Local_Supported_Controller_Delay = 0x000F


class StatusParameters (IntEnum):
    """
    STATUS PARAMETERS
    OGF:0X05
    """
    HCI_Read_Failed_Contact_Counter = 0x0001
    HCI_Reset_Failed_Contact_Counter = 0x0002
    HCI_Read_Link_Quality = 0x0003
    HCI_Read_RSSI = 0x0005
    HCI_Read_AFH_Channel_Map = 0x0006
    HCI_Read_Clock = 0x0007
    HCI_Read_Encryption_Key_Size = 0x0008
    HCI_Get_MWS_Transport_Layer_Configuration = 0x000C
    HCI_Set_Triggered_Clock_Capture = 0x000D


class TestingCommands(IntEnum):
    """
    TESTING COMMANDS
    OGF:0X06
    """
    HCI_Read_Loopback_Mode = 0x0001
    HCI_Write_Loopback_Mode = 0x0002
    HCI_Enable_Device_Under_Test_Mode = 0x0003
    HCI_Write_Simple_Pairing_Debug_Mode = 0x0004
    HCI_Write_Secure_Connections_Test_Mode = 0x000A


class LeControlCommands(IntEnum):
    """
    LE CONTROLLER COMMANDS
    OGF:0X08
    """
    HCI_LE_Set_Event_Mask = 0x0001
    HCI_LE_Read_Buffer_Size_v2 = 0x0060
    HCI_LE_Read_Buffer_Size_v1 = 0x0002
    HCI_LE_Read_Local_Supported_Features = 0x0003
    HCI_LE_Set_Random_Address = 0x0005
    HCI_LE_Set_Advertising_Parameters = 0x0006
    HCI_LE_Read_Advertising_Channel_Tx_Power = 0x0007
    HCI_LE_Set_Advertising_Data = 0x0008
    HCI_LE_Set_Scan_Response_Data = 0x0009
    HCI_LE_Set_Advertising_Enable = 0x000A
    HCI_LE_Set_Scan_Parameters = 0x000B
    HCI_LE_Set_Scan_Enable = 0x000C
    HCI_LE_Create_Connection = 0x000D
    HCI_LE_Create_Connection_Cancel = 0x000E
    HCI_LE_Read_Filter_Accept_List_Size = 0x000F
    HCI_LE_Clear_Filter_Accept_List = 0x0010
    HCI_LE_Add_Device_To_Filter_Accept_List = 0x0011
    HCI_LE_Remove_Device_From_Filter_Accept_List = 0x0012
    HCI_LE_Connection_Update = 0x0013
    HCI_LE_Set_Host_Channel_Classification = 0x0014
    HCI_LE_Read_Channel_Map = 0x0015
    HCI_LE_Read_Remote_Features = 0x0016
    HCI_LE_Encrypt = 0x0017
    HCI_LE_Rand = 0x0018
    HCI_LE_Enable_Encryption = 0x0019
    HCI_LE_Long_Term_Key_Request_Reply = 0x001A
    HCI_LE_Long_Term_Key_Request_Negative_Reply = 0x001B
    HCI_LE_Read_Supported_States = 0x001C
    HCI_LE_Receiver_Test_v3 = 0x004F
    HCI_LE_Receiver_Test_v2 = 0x0033
    HCI_LE_Receiver_Test_v1 = 0x001D
    HCI_LE_Transmitter_Test_v4 = 0x007B
    HCI_LE_Transmitter_Test_v3 = 0x0050
    HCI_LE_Transmitter_Test_v2 = 0x0034
    HCI_LE_Transmitter_Test_v1 = 0x001E
    HCI_LE_Test_End = 0x001F
    HCI_LE_Remote_Connection_Parameter_Request_Reply = 0x0020
    HCI_LE_Remote_Connection_Parameter_Request_Negative_Reply = 0x0021
    HCI_LE_Set_Data_Length = 0x0022
    HCI_LE_Read_Suggested_Default_Data_Length = 0x0023
    HCI_LE_Write_Suggested_Default_Data_Length = 0x0024
    HCI_LE_Read_Local_P256_Public_Key = 0x0025
    HCI_LE_Generate_DHKey_v2 = 0x005E
    HCI_LE_Generate_DHKey_v1 = 0x0026
    HCI_LE_Add_Device_To_Resolving_List = 0x0027
    HCI_LE_Remove_Device_From_Resolving_List = 0x0028
    HCI_LE_Clear_Resolving_List = 0x0029
    HCI_LE_Read_Resolving_List_Size = 0x002A
    HCI_LE_Read_Peer_Resolvable_Address = 0x002B
    HCI_LE_Read_Local_Resolvable_Address = 0x002C
    HCI_LE_Set_Address_Resolution_Enable = 0x002D
    HCI_LE_Set_Resolvable_Private_Address_Timeout = 0x002E
    HCI_LE_Read_Maximum_Data_Length = 0x002F
    HCI_LE_Read_PHY = 0x0030
    HCI_LE_Set_Default_PHY = 0x0031
    HCI_LE_Set_PHY = 0x0032
    HCI_LE_Set_Advertising_Set_Random_Address = 0x0035
    HCI_LE_Set_Extended_Advertising_Parameters = 0x0036
    HCI_LE_Set_Extended_Advertising_Data = 0x0037
    HCI_LE_Set_Extended_Scan_Response_Data = 0x0038
    HCI_LE_Set_Extended_Advertising_Enable = 0x0039
    HCI_LE_Read_Maximum_Advertising_Data_Length = 0x003A
    HCI_LE_Read_Number_of_Supported_Advertising_Sets = 0x003B
    HCI_LE_Remove_Advertising_Set = 0x003C
    HCI_LE_Clear_Advertising_Sets = 0x003D
    HCI_LE_Set_Periodic_Advertising_Parameters = 0x003E
    HCI_LE_Set_Periodic_Advertising_Data = 0x003F
    HCI_LE_Set_Periodic_Advertising_Enable = 0x0040
    HCI_LE_Set_Extended_Scan_Parameters = 0x0041
    HCI_LE_Set_Extended_Scan_Enable = 0x0042
    HCI_LE_Extended_Create_Connection = 0x0043
    HCI_LE_Periodic_Advertising_Create_Sync = 0x0044
    HCI_LE_Periodic_Advertising_Create_Sync_Cancel = 0x0045
    HCI_LE_Periodic_Advertising_Terminate_Sync = 0x0046
    HCI_LE_Add_Device_To_Periodic_Advertiser_List = 0x0047
    HCI_LE_Remove_Device_From_Periodic_Advertiser_List = 0x0048
    HCI_LE_Clear_Periodic_Advertiser_List = 0x0049
    HCI_LE_Read_Periodic_Advertiser_List_Size = 0x004A
    HCI_LE_Read_Transmit_Power = 0x004B
    HCI_LE_Read_RF_Path_Compensation = 0x004C
    HCI_LE_Write_RF_Path_Compensation = 0x004D
    HCI_LE_Set_Privacy_Mode = 0x004E
    HCI_LE_Set_Connectionless_CTE_Transmit_Parameters = 0x0051
    HCI_LE_Set_Connectionless_CTE_Transmit_Enable = 0x0052
    HCI_LE_Set_Connectionless_IQ_Sampling_Enable = 0x0053
    HCI_LE_Set_Connection_CTE_Receive_Parameters = 0x0054
    HCI_LE_Set_Connection_CTE_Transmit_Parameters = 0x0055
    HCI_LE_Connection_CTE_Request_Enable = 0x0056
    HCI_LE_Connection_CTE_Response_Enable = 0x0057
    HCI_LE_Read_Antenna_Information = 0x0058
    HCI_LE_Set_Periodic_Advertising_Receive_Enable = 0x0059
    HCI_LE_Periodic_Advertising_Sync_Transfer = 0x005A
    HCI_LE_Periodic_Advertising_Set_Info_Transfer = 0x005B
    HCI_LE_Set_Periodic_Advertising_Sync_Transfer_Parameters = 0x005C
    HCI_LE_Set_Default_Periodic_Advertising_Sync_Transfer_Parameters = 0x005D
    HCI_LE_Modify_Sleep_Clock_Accuracy = 0x005F
    HCI_LE_Read_ISO_TX_Sync = 0x0061
    HCI_LE_Set_CIG_Parameters = 0x0062
    HCI_LE_Set_CIG_Parameters_Test = 0x0063
    HCI_LE_Create_CIS = 0x0064
    HCI_LE_Remove_CIG = 0x0065
    HCI_LE_Accept_CIS_Request = 0x0066
    HCI_LE_Reject_CIS_Request = 0x0067
    HCI_LE_Create_BIG = 0x0068
    HCI_LE_Create_BIG_Test = 0x0069
    HCI_LE_Terminate_BIG = 0x006A
    HCI_LE_BIG_Create_Sync = 0x006B
    HCI_LE_BIG_Terminate_Sync = 0x006C
    HCI_LE_Request_Peer_SCA = 0x006D
    HCI_LE_Setup_ISO_Data_Path = 0x006E
    HCI_LE_Remove_ISO_Data_Path = 0x006F
    HCI_LE_ISO_Transmit_Test = 0x0070
    HCI_LE_ISO_Receive_Test = 0x0071
    HCI_LE_ISO_Read_Test_Counters = 0x0072
    HCI_LE_ISO_Test_End = 0x0073
    HCI_LE_Set_Host_Feature = 0x0074
    HCI_LE_Read_ISO_Link_Quality = 0x0075
    HCI_LE_Enhanced_Read_Transmit_Power_Level = 0x0076
    HCI_LE_Read_Remote_Transmit_Power_Level = 0x0077
    HCI_LE_Set_Path_Loss_Reporting_Parameters = 0x0078
    HCI_LE_Set_Path_Loss_Reporting_Enable = 0x0079
    HCI_LE_Set_Transmit_Power_Reporting_Enable = 0x007A
    HCI_LE_Set_Data_Related_Address_Changes = 0x7C
    HCI_LE_Set_Default_Subrate = 0x007D
    HCI_LE_Subrate_Request = 0x007E


class Vendor_Specific(IntEnum):
    """
    VENDOR SPECIFIC
    OGF:0XFE
    """