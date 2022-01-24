from .events import *
from hci.event.events.autocast import __autocast
import inspect


def _autocast(pkt):

    _subclass_to_autocast_func = [
        # need parse subEvent class
        "LE_Meta_Events",
    ]
    event_name = pkt.name
    try:
        if pkt.needParse and inspect.isclass(globals()[event_name]):
            pkt.__class__ = eval(event_name)
        if event_name in _subclass_to_autocast_func:
            pkt = __autocast(pkt)
    except KeyError:
        pass
    return pkt
