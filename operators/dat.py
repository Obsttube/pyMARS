from . import op_codes


class dat(op_codes.Op_code):
    @staticmethod
    def execute_a(core, ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    def execute_b(core, ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    def execute_ab(core, ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    def execute_ba(core, ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    def execute_f(core, ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    def execute_x(core, ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    def execute_i(core, ins_reg, src_reg, dst_reg):
        pass

    @staticmethod
    def execute_after(core, ins_reg, src_reg, dst_reg):
        op_codes.terminate_process(core, ins_reg)
