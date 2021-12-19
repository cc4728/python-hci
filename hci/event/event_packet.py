from struct import unpack_from

from hci import HciPacket
from hci.event.event_codes import EventCodes

"""
Description in bluetooth core spec v5.3:
    The HCI Event packet header is the first 2 octets of the packet.
    The event code 0xFE is reserved for future use (used for specification development purposes). 
    The event code 0xFF is reserved for vendor-specific debugging events.
    0                  8                16                   
    +------------------+----------------+-------------------------------+
    |  Event Code      |   Length       |               Data            |                
    +------------------+----------------+-------------------------------+
"""


class EventPacket(HciPacket):
    OFFSET_DATA_LENGTH = 2
    DATA_LENGTH_OCTET = 1
    EventCodeName = 'UnKnow'

    @property
    def event_code(self):
        OFFSET, SIZE_OCTETS = 1, 1
        event_code = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', event_code)[0]

    @property
    def event_code_name(self):
        if self.event_code in EventCodes._value2member_map_:
            self.EventCodeName = EventCodes(self.event_code).name
        return self.EventCodeName

    @property
    def data_length(self):
        OFFSET, SIZE_OCTETS = 2, 1
        data_length = self._get_data(OFFSET, SIZE_OCTETS)
        return unpack_from('<B', data_length)[0]

    def __str__(self):
        return super().__str__() + '\n' + '\n'.join([
            '   Event Code: {} ({})   Length: {} ({})',
        ]).format(
            hex(self.event_code),
            self.event_code_name,
            hex(self.data_length),
            int(self.data_length),
        )
