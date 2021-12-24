import inspect
from .le_apcf_command_pkt import LE_APCF_Command
from .le_apcf_commands import *


def __autocast(pkt):
    try:
        if pkt.sub_name and inspect.isclass(globals()[pkt.sub_name]):
            pkt.__class__ = eval(pkt.sub_name)
    except KeyError:
        pass
    return pkt
