from ..command_packet import CommandPacket


class HCI_Reset(CommandPacket):
    def __init__(self):
        super().__init__(CommandPacket.OpCode.HCI_RESET)

    def __str__(self):
        return super().__str__() + '\n'.join(['{}']).format("Test".ljust(10))
