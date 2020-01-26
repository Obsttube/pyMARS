from . import op_codes


class jmn(op_codes.Op_code):
    @staticmethod
    def execute_a(core, ins_reg, src_reg, dst_reg):
        if dst_reg.ins.a != 0:
            op_codes.jump_reg(core, ins_reg)

    @staticmethod
    def execute_b(core, ins_reg, src_reg, dst_reg):
        if dst_reg.ins.b != 0:
            op_codes.jump_reg(core, ins_reg)

    @staticmethod
    def execute_ab(core, ins_reg, src_reg, dst_reg):
        jmn.execute_b(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_ba(core, ins_reg, src_reg, dst_reg):
        jmn.execute_a(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_f(core, ins_reg, src_reg, dst_reg):
        if dst_reg.ins.a != 0 and dst_reg.ins.b != 0:
            op_codes.jump_reg(core, ins_reg)

    @staticmethod
    def execute_x(core, ins_reg, src_reg, dst_reg):
        jmn.execute_f(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_i(core, ins_reg, src_reg, dst_reg):
        jmn.execute_f(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_after(core, ins_reg, src_reg, dst_reg):
        pass
