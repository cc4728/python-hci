from enum import IntEnum
from struct import unpack_from

from hci.event import EventPacket

class LE_Meta_Events(EventPacket):
    SubCodeName = None

    class LE_META_EVENTS(IntEnum):
        HCI_LE_Connection_Complete = 0x01
        HCI_LE_Advertising_Report = 0x02
        HCI_LE_Connection_Update_Complete = 0x03
        HCI_LE_Read_Remote_Features_Complete = 0x04
        HCI_LE_Long_Term_Key_Request = 0x05
        HCI_LE_Remote_Connection_Parameter_Request = 0x06
        HCI_LE_Data_Length_Change = 0x07
        HCI_LE_Read_Local_P256_Public_Key = 0x08
        HCI_LE_Generate_DHKey_Complete = 0x09
        HCI_LE_En_Connection_Complete = 0x0A
        HCI_LE_Directed_Advertising_Report = 0x0B
        HCI_LE_PHY_Update_Complete = 0x0C
        HCI_LE_Extended_Advertising_Report = 0x0D
        HCI_LE_PA_Sync_Established = 0x0E
        HCI_LE_PA_Report = 0x0F
        HCI_LE_PA_Sync_Lost = 0x10
        HCI_LE_Scan_Timeout = 0x11
        HCI_LE_Advertising_Set_Terminated = 0x12
        HCI_LE_Scan_Request_Received = 0x13
        HCI_LE_Channel_Selection_Algorithm = 0x14
        HCI_LE_Connectionless_IQ_Report = 0x15
        HCI_LE_Connection_IQ_Report = 0x16
        HCI_LE_CTE_Request_Failed = 0x17
        HCI_LE_PA_Sync_Transfer_Received = 0x18
        HCI_LE_CIS_Established = 0x19
        HCI_LE_CIS_Request = 0x1A
        HCI_LE_Create_BIG_Complete = 0x1B
        HCI_LE_Terminate_BIG_Complete = 0x1C
        HCI_LE_BIG_Sync_Established = 0x1D
        HCI_LE_BIG_Sync_Lost = 0x1E
        HCI_LE_Request_Peer_SCA_Complete = 0x1F
        HCI_LE_Path_Loss_Threshold = 0x20
        HCI_LE_Transmit_Power_Reporting = 0x21
        HCI_LE_BIGInfo_Advertising_Report = 0x22
        HCI_LE_Subrate_Change = 0x23

    @property
    def sub_event(self):
        OFFSET, SIZE_OCTETS = 3, 1
        event = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', event)[0]

    @property
    def sub_name(self):
        if not self.SubCodeName:
            self.SubCodeName = self.LE_META_EVENTS(self.sub_event).name
        return self.SubCodeName

    @property
    def status(self):
        OFFSET, SIZE_OCTETS = 5, 1
        status = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', status)[0]

    def __str__(self):
        return super().__str__() + ''.join(['{}']).format(self.sub_name.ljust(30))

