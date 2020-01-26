from . import op_codes


class sub(op_codes.Op_code):
    @staticmethod
    def execute_a(core, ins_reg, src_reg, dst_reg):
        dst_reg.ins.a -= src_reg.ins.a
        dst_reg.ins.a %= core.size

    @staticmethod
    def execute_b(core, ins_reg, src_reg, dst_reg):
        dst_reg.ins.b -= src_reg.ins.b
        dst_reg.ins.b %= core.size

    @staticmethod
    def execute_ab(core, ins_reg, src_reg, dst_reg):
        dst_reg.ins.b -= src_reg.ins.a
        dst_reg.ins.b %= core.size

    @staticmethod
    def execute_ba(core, ins_reg, src_reg, dst_reg):
        dst_reg.ins.a -= src_reg.ins.b
        dst_reg.ins.a %= core.size

    @staticmethod
    def execute_f(core, ins_reg, src_reg, dst_reg):
        sub.execute_a(core, ins_reg, src_reg, dst_reg)
        sub.execute_b(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_x(core, ins_reg, src_reg, dst_reg):
        sub.execute_ab(core, ins_reg, src_reg, dst_reg)
        sub.execute_ba(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_i(core, ins_reg, src_reg, dst_reg):
        sub.execute_f(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_after(core, ins_reg, src_reg, dst_reg):
        pass
