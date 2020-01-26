from . import op_codes


class seq(op_codes.Op_code):
    @staticmethod
    def execute_a(core, ins_reg, src_reg, dst_reg):
        if src_reg.ins.a == dst_reg.ins.a:
            op_codes.increment_pointer(core, ins_reg)

    @staticmethod
    def execute_b(core, ins_reg, src_reg, dst_reg):
        if src_reg.ins.b == dst_reg.ins.b:
            op_codes.increment_pointer(core, ins_reg)

    @staticmethod
    def execute_ab(core, ins_reg, src_reg, dst_reg):
        if src_reg.ins.a == dst_reg.ins.b:
            op_codes.increment_pointer(core, ins_reg)

    @staticmethod
    def execute_ba(core, ins_reg, src_reg, dst_reg):
        seq.execute_ab(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_f(core, ins_reg, src_reg, dst_reg):
        if src_reg.ins.a == dst_reg.ins.a and src_reg.ins.b == dst_reg.ins.b:
            op_codes.increment_pointer(core, ins_reg)

    @staticmethod
    def execute_x(core, ins_reg, src_reg, dst_reg):
        seq.execute_ab(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_i(core, ins_reg, src_reg, dst_reg):
        src_ins = src_reg.ins
        dst_ins = dst_reg.ins
        if (src_ins.a == dst_ins.a
                and src_ins.b == dst_ins.b
                and src_ins.op_code == dst_ins.op_code
                and src_ins.modifier == dst_ins.modifier
                and src_ins.a_mode == dst_ins.a_mode
                and src_ins.b_mode == dst_ins.b_mode):
            op_codes.increment_pointer(core, ins_reg)

    @staticmethod
    def execute_after(core, ins_reg, src_reg, dst_reg):
        pass
