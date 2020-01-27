import abc
import instruction


class Op_code(abc.ABC):

    def __init__(self):
        super().__init__()

    @staticmethod
    @abc.abstractmethod
    def execute_a(core, ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    @abc.abstractmethod
    def execute_b(core, ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    @abc.abstractmethod
    def execute_ab(core, ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    @abc.abstractmethod
    def execute_ba(core, ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    @abc.abstractmethod
    def execute_f(core, ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    @abc.abstractmethod
    def execute_x(core, ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    @abc.abstractmethod
    def execute_i(core, ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    @abc.abstractmethod
    def execute_after(core, ins_reg, src_reg, dst_reg):
        pass


def terminate_process(core, ins_reg):
    print("terminate process")  # TODO
    warior = ins_reg.ins.last_warior
    warior.remove_curr_process()


def jump_adr(core, ins_reg, adr):
    # print(f"jump to {adr}")  # TODO
    warior = ins_reg.ins.last_warior
    warior.set_next_instruction(adr)


# def increment_pointer(core, ins_reg):
#    print("increment pointer")  # TODO
    # warior=ins_reg.ins.warior
    # increment warior address


def jump_reg(core, ins_reg):
    jump_adr(core, ins_reg, (ins_reg.adr+ins_reg.ins.a)%core.size)


def execute(core, ins_reg, src_reg, dst_reg):
    ins = ins_reg.ins
    op_code = ins.op_code
    modifier = ins.modifier
    if op_code in instruction.VALID_OP_CODES:
        if modifier in instruction.VALID_MODIFIERS:
            module = __import__(op_code.lower(), globals=globals(), level=1)
            # print(module)
            class_ = getattr(module, op_code.lower())
            #increment_pointer(core, ins_reg)
            execute_modifier = getattr(class_, 'execute_'+modifier.lower())
            execute_modifier(core, ins_reg, src_reg, dst_reg)
            execute_after = getattr(class_, 'execute_after')
            execute_after(core, ins_reg, src_reg, dst_reg)
            if core.get_at(dst_reg.adr) != dst_reg.ins:
                this_warior=dst_reg.ins.last_warior
                this_warior.gui.update_block_color(dst_reg.adr,this_warior.color)
            core.set_at(dst_reg.adr, dst_reg.ins)
        else:
            print("unsuported modifier")  # TODO
    else:
        print("unsupported op_code")  # TODO throw exception
