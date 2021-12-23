from .event_codes import EventCodes
from . import events


def _autocast(pkt):
    return pkt

    _event_code_to_class = {
        EventCodes.VENDOR_SPECIFIC_EVENT: events.VendorSpecificEvent,
        EventCodes.HCI_COMMAND_COMPLETE: events.HCI_CommandComplete
    }
    _class_to_autocast_func = {
        events.VendorSpecificEvent: events.vendor_specific._autocast,
        events.HCI_CommandComplete: events.hci_commands_complete._autocast,
    }
    try:
        if pkt.event_code in _event_code_to_class.keys():
            pkt.__class__ = _event_code_to_class[pkt.event_code]
        if type(pkt) in _class_to_autocast_func.keys():
            pkt = _class_to_autocast_func[type(pkt)](pkt)
    except KeyError:
        pass

    return pkt
