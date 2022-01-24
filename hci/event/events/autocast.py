import inspect
from .le_meta_event_pkt import LE_Meta_Events
from .le_meta_events import *


def __autocast(pkt):
    try:
        if pkt.sub_name and inspect.isclass(globals()[pkt.sub_name]):
            pkt.__class__ = eval(pkt.sub_name)
    except KeyError:
        pass
    return pkt
