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
