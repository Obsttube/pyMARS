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
        if src_reg.ins != dst_reg.ins:
            op_codes.increment_pointer(core, ins_reg)

    @staticmethod
    def execute_after(core, ins_reg, src_reg, dst_reg):
        pass
