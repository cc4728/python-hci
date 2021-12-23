from .opcode import *
from .commands import *



def _autocast(pkt):

    return pkt

   # try:


    #    if pkt.opcode in _opcode_to_class.keys():
    #        pkt.__class__ = _opcode_to_class[pkt.opcode]
    #except KeyError:
    #    pass


