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


class mov(Op_code):
    @staticmethod
    def execute_a(ins_reg, src_reg, dst_reg):
        dst_reg.ins.a=src_reg.ins.a

    @staticmethod
    def execute_b(ins_reg, src_reg, dst_reg):
        dst_reg.ins.b=src_reg.ins.b

    @staticmethod
    def execute_ab(ins_reg, src_reg, dst_reg):
        dst_reg.ins.b=src_reg.ins.a

    @staticmethod
    def execute_ba(ins_reg, src_reg, dst_reg):
        dst_reg.ins.a=src_reg.ins.b

    @staticmethod
    def execute_f(ins_reg, src_reg, dst_reg):
        mov.execute_a(ins_reg,src_reg,dst_reg)
        mov.execute_b(ins_reg,src_reg,dst_reg)

    @staticmethod
    def execute_x(ins_reg, src_reg, dst_reg):
        mov.execute_ab(ins_reg,src_reg,dst_reg)
        mov.execute_ba(ins_reg,src_reg,dst_reg)

    @staticmethod
    def execute_i(ins_reg, src_reg, dst_reg):
        dst_reg.ins = src_reg.ins
