import instruction
import register
from operators import op_codes


class Core():

    def __init__(self, size):
        self.size = size
        self.__core = []
        for _ in range(size):
            def_ins = instruction.Instruction(
                self.size, "DAT", "F", "$", 0, "$", 0)
            self.__core.append(def_ins)  # fill core with DAT instructions
        self.ins_reg = register.Register()  # instruction register
        self.src_reg = register.Register()  # source register
        self.dst_reg = register.Register()  # destination register

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

    def __str__(self):
        output = ""
        for ins in self.__core:
            output += str(ins)+"\n"
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
