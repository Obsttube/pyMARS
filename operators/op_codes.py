import abc


class Op_code(abc.ABC):

    def __init__(self):
        super().__init__()

    @staticmethod
    @abc.abstractmethod
    def execute_a(ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    @abc.abstractmethod
    def execute_b(ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    @abc.abstractmethod
    def execute_ab(ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    @abc.abstractmethod
    def execute_ba(ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    @abc.abstractmethod
    def execute_f(ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    @abc.abstractmethod
    def execute_x(ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    @abc.abstractmethod
    def execute_i(ins_reg, src_reg, dst_reg):
        pass


def execute(ins_reg, src_reg, dst_reg):
    ins = ins_reg.ins
    op_code = ins.op_code
    modifier = ins.modifier
    valid_op_codes = ["DAT", "MOV", "ADD", "SUB", "MUL", "DIV", "MOD", "JMP",
                      "JMZ", "JMN", "DJN", "SPL", "CMP", "SEQ", "SNE", "SLT", "LDP", "STP", "NOP"]
    valid_modifiers = ["A", "B", "AB", "BA", "F", "X", "I"]
    if op_code in valid_op_codes:
        if modifier in valid_modifiers:
            module = __import__(op_code.lower(), globals=globals(), level=1)
            print(module)
            class_ = getattr(module, op_code.lower())
            func = getattr(class_, 'execute_'+modifier.lower())
            func(ins_reg, src_reg, dst_reg)
        else:
            print("unsuported modifier")  # TODO
    else:
        print("unsupported op_code")  # TODO throw exception
