import instruction
import register
from operators import op_codes


class Core():

    def __init__(self, size):
        self.size = size
        self.__core = []
        for _ in range(size):
            def_ins = instruction.Instruction(
                None, self.size, "DAT", "F", "$", 0, "$", 0)
            self.__core.append(def_ins)  # fill core with DAT instructions
        self.ins_reg = register.Register()  # instruction register
        self.src_reg = register.Register()  # source register
        self.dst_reg = register.Register()  # destination register
        self.wariors = []
        self.curr_warior_index = 0
        self.gui = None

    def set_gui_callback(self, gui):
        self.gui = gui

    def add_warior(self, warior):
        self.wariors.append(warior)

    def next_warior(self):
        self.curr_warior_index += 1
        if self.curr_warior_index >= len(self.wariors):
            self.curr_warior_index = 0

    def get_current_warior(self):
        return self.wariors[self.curr_warior_index]

    def get_at(self, adr):  # get instruction at address
        return self.__core[adr]

    def set_at(self, adr, ins):  # set instruction at address
        self.__core[adr] = ins

    def execute(self, index):
        # fetch
        self.ins_reg.fetch(self, index)  # fetch instruction at index
        # decode
        self.src_reg.fetch(self, decode_field(self, self.ins_reg.adr, "a"))
        self.dst_reg.fetch(self, decode_field(self, self.ins_reg.adr, "b"))
        # execute
        op_codes.execute(self, self.ins_reg, self.src_reg, self.dst_reg)

    def wariors_alive(self):
        alive = 0
        for warior in self.wariors:
            if len(warior.processes) > 0:
                alive += 1
        return alive

    def set_last_warior(self, ins_idx, warior):
        self.__core[ins_idx].last_warior = warior

    def get_winning_warior(self):
        for warior in self.wariors:
            if len(warior.processes) > 0:
                return warior

    def execute_current_ins(self):
        curr_warior = self.get_current_warior()
        if len(curr_warior.processes) == 0:
            if self.wariors_alive() > 0:
                while len(self.get_current_warior().processes) == 0:
                    self.next_warior()
            else:
                return
        curr_ins_idx = curr_warior.get_instruction_index()
        print(curr_ins_idx)
        self.set_last_warior(curr_ins_idx, curr_warior)
        curr_warior.next_instruction(self.size)
        self.execute(curr_ins_idx)
        curr_warior.next_process()
        self.next_warior()

    def __str__(self):
        output = ""
        index=0
        for ins in self.__core:
            output += str(index)+". "+str(ins)+"\n"
            index+=1
        return output


def decode_field(core, adr, field_type):  # get address from field
    # field_type "a" or "b"
    field = None
    field_mode = None
    ins = core.get_at(adr)
    if field_type == "a":
        field = ins.a
        field_mode = ins.a_mode
    elif field_type == "b":
        field = ins.b
        field_mode = ins.b_mode
    else:
        return  # TODO throw exception

    if field_mode == "#":
        pass
    elif field_mode == "$":
        adr += field
    elif field_mode == "*":
        adr += field
        adr += core.get_at(adr).a
    elif field_mode == "@":
        adr += field
        adr += core.get_at(adr).b
    elif field_mode == "{":
        adr += field
        intermed = core.get_at(adr)
        intermed.a -= 1
        intermed.a %= core.size
        core.set_at(adr, intermed)
        adr += intermed.a
    elif field_mode == "}":
        adr += field
        intermed = core.get_at(adr)
        adr += intermed.a
        intermed.a -= 1
        intermed.a %= core.size
        core.set_at(adr, intermed)
    elif field_mode == "<":
        adr += field
        intermed = core.get_at(adr)
        intermed.b -= 1
        intermed.b %= core.size
        core.set_at(adr, intermed)
        adr += intermed.b
    elif field_mode == ">":
        adr += field
        intermed = core.get_at(adr)
        adr += intermed.b
        intermed.b -= 1
        intermed.b %= core.size
        core.set_at(adr, intermed)
    else:
        return  # TODO change to throwing exception
    adr %= core.size
    return adr
