from . import op_codes


class sne(op_codes.Op_code):
    @staticmethod
    def execute_a(core, ins_reg, src_reg, dst_reg):
        if src_reg.ins.a != dst_reg.ins.a:
            op_codes.increment_pointer(core, ins_reg)

    @staticmethod
    def execute_b(core, ins_reg, src_reg, dst_reg):
        if src_reg.ins.b != dst_reg.ins.b:
            op_codes.increment_pointer(core, ins_reg)

    @staticmethod
    def execute_ab(core, ins_reg, src_reg, dst_reg):
        if src_reg.ins.a != dst_reg.ins.b:
            op_codes.increment_pointer(core, ins_reg)

    @staticmethod
    def execute_ba(core, ins_reg, src_reg, dst_reg):
        sne.execute_ab(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_f(core, ins_reg, src_reg, dst_reg):
        if src_reg.ins.a != dst_reg.ins.a or src_reg.ins.b != dst_reg.ins.b:
            op_codes.increment_pointer(core, ins_reg)

    @staticmethod
    def execute_x(core, ins_reg, src_reg, dst_reg):
        sne.execute_ab(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_i(core, ins_reg, src_reg, dst_reg):
        src_ins = src_reg.ins
        dst_ins = dst_reg.ins
        if (src_ins.a != dst_ins.a
                or src_ins.b != dst_ins.b
                or src_ins.op_code != dst_ins.op_code
                or src_ins.modifier != dst_ins.modifier
                or src_ins.a_mode != dst_ins.a_mode
                or src_ins.b_mode != dst_ins.b_mode):
            op_codes.increment_pointer(core, ins_reg)

    @staticmethod
    def execute_after(core, ins_reg, src_reg, dst_reg):
        pass
