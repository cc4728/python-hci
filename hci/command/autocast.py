from .opcode import *
from .commands import *
import inspect


def _autocast(pkt):
    opcode_name, ogf_name = pkt.name
    try:
        if pkt.needParse and inspect.isclass(globals()[opcode_name]):
            pkt.__class__ = eval(opcode_name)
    except KeyError:
        pass
    return pkt



