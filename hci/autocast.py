from . import asynchronous
from . import command
from . import event
from . import HciPacket


def _autocast(pkt):
    _packet_type_to_class = {
        HciPacket.PacketType.ASYNCHRONOUS_DATA:
            asynchronous.AsynchronousDataPacket,
        HciPacket.PacketType.COMMAND: command.CommandPacket,
        HciPacket.PacketType.EVENT: event.EventPacket,
    }

    _class_to_autocast_func = {
        asynchronous.AsynchronousDataPacket: asynchronous._autocast,
        command.CommandPacket: command._autocast,
        event.EventPacket: event._autocast,
    }

    try:
        if pkt.packet_type in _packet_type_to_class.keys():
            pkt.__class__ = _packet_type_to_class[pkt.packet_type]
        if type(pkt) in _class_to_autocast_func.keys():
            pkt = _class_to_autocast_func[type(pkt)](pkt)
    except KeyError:
        pass

    return pkt
