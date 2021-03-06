from . import op_codes


class mov(op_codes.Op_code):  # czy nazwać inaczej, aby w każdym op_code klasa nazywała się tak samo?
    @staticmethod
    def execute_a(core, ins_reg, src_reg, dst_reg):
        dst_reg.ins.a = src_reg.ins.a

    @staticmethod
    def execute_b(core, ins_reg, src_reg, dst_reg):
        dst_reg.ins.b = src_reg.ins.b

    @staticmethod
    def execute_ab(core, ins_reg, src_reg, dst_reg):
        dst_reg.ins.b = src_reg.ins.a

    @staticmethod
    def execute_ba(core, ins_reg, src_reg, dst_reg):
        dst_reg.ins.a = src_reg.ins.b

    @staticmethod
    def execute_f(core, ins_reg, src_reg, dst_reg):
        mov.execute_a(core, ins_reg, src_reg, dst_reg)
        mov.execute_b(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_x(core, ins_reg, src_reg, dst_reg):
        mov.execute_ab(core, ins_reg, src_reg, dst_reg)
        mov.execute_ba(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_i(core, ins_reg, src_reg, dst_reg):
        dst_reg.ins = src_reg.ins

    @staticmethod
    def execute_after(core, ins_reg, src_reg, dst_reg):
        pass
