from op_codes import op_codes


class Instruction():

    def __init__(self, op_code, modifier, a_mode, a, b_mode, b):
        self.op_code = op_code  # e.g. "MOV"
        self.modifier = modifier  # e.g. "I"
        self.a_mode = a_mode  # e.g. "#"
        self.a = a  # e.g. 5
        self.b_mode = b_mode  # e.g. "$"
        self.b = b  # e.g. 1

    def __str__(self):
        return (f"op_code: {self.op_code}"
                f", modifier: {self.modifier}, a_mode: {self.a_mode}"
                f", a: {self.a}, b_mode: {self.b_mode}, b: {self.b}")


class Register():

    def __init__(self):
        self.ins = None  # instruction
        self.adr = None  # absolute address of the instruction

    # fetch an instruction from core at an ABSOLUTE adr and save it to the register
    def fetch(self, core, adr):
        self.adr = adr
        # set ins to an instruction from core at adr
        self.ins = core.get_at(adr)


class Core():

    def __init__(self, size):
        self.size = size
        self.__core = []
        for _ in range(size):
            def_ins = Instruction("DAT", "F", "$", 0, "$", 0)
            self.__core.append(def_ins)  # fill core with DAT instructions

    def get_at(self, adr):  # get instruction at address
        return self.__core[adr]

    def set_at(self, adr, ins):  # set instruction at address
        self.__core[adr] = ins

    def __str__(self):
        output = ""
        for ins in self.__core:
            output += str(ins)+"\n"
        return output


def __decode_field(core, adr, field_type):  # get address from field
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
        intermed %= core.size
        core.set_at(adr, intermed)
        adr += intermed.a
    elif field_mode == "}":
        adr += field
        intermed = core.get_at(adr)
        intermed.b -= 1
        intermed %= core.size
        core.set_at(adr, intermed)
        adr += intermed.b
    elif field_mode == "<":
        adr += field
        intermed = core.get_at(adr)
        adr += intermed.a
        intermed.a -= 1
        intermed %= core.size
        core.set_at(adr, intermed)
    elif field_mode == ">":
        adr += field
        intermed = core.get_at(adr)
        adr += intermed.b
        intermed.b -= 1
        intermed %= core.size
        core.set_at(adr, intermed)
    else:
        return  # TODO change to throwing exception
    adr %= core.size
    return adr


if __name__ == "__main__":
    ins_reg = Register()  # instruction register
    src_reg = Register()  # source register
    dst_reg = Register()  # destination register
    core = Core(7)
    mov = Instruction("MOV", "I", "$", 0, "$", 1)
    core.set_at(0, mov)  # load mov instruction at 0
    # execution
    # fetch
    ins_reg.fetch(core, 0)  # fetch instruction at 0
    # decode
    field = ins_reg.ins.a
    field_mode = ins_reg.ins.a_mode
    src_reg.fetch(core, __decode_field(core, ins_reg.adr, "a"))
    dst_reg.fetch(core, __decode_field(core, ins_reg.adr, "b"))
    print(core)
    # execute
    # ins_reg.ins.modifier
    print(dst_reg.ins)
    op_codes.mov.execute_i(ins_reg, src_reg, dst_reg)
    print(dst_reg.ins)
    print()
    core.set_at(dst_reg.adr, dst_reg.ins)
    print(core)
