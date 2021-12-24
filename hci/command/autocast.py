from .commands import *
from hci.command.commands.autocast import __autocast
import inspect


def _autocast(pkt):

    _subclass_to_autocast_func = [
        # need parse subcmd class
        "LE_APCF_Command",
    ]
    opcode_name, ogf_name = pkt.name
    try:
        if pkt.needParse and inspect.isclass(globals()[opcode_name]):
            pkt.__class__ = eval(opcode_name)
        if opcode_name in _subclass_to_autocast_func:
            pkt = __autocast(pkt)
    except KeyError:
        pass
    return pkt



