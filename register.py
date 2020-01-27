class Register():

    def __init__(self):
        self.ins = None  # instruction
        self.adr = None  # absolute address of the instruction

    # fetch an instruction from core at an ABSOLUTE adr and save it to the register
    def fetch(self, core, adr):
        self.adr = adr
        # set ins to an instruction from core at adr
        self.ins = core.get_at(adr)
