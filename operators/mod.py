from . import op_codes
import math


class mod(op_codes.Op_code):
    @staticmethod
    def execute_a(core, ins_reg, src_reg, dst_reg):
        if src_reg.ins.a == 0:
            op_codes.terminate_process(core, ins_reg)
            return
        dst_reg.ins.a %= src_reg.ins.a
        dst_reg.ins.a %= core.size

    @staticmethod
    def execute_b(core, ins_reg, src_reg, dst_reg):
        if src_reg.ins.b == 0:
            op_codes.terminate_process(core, ins_reg)
            return
        dst_reg.ins.b %= src_reg.ins.b
        dst_reg.ins.b %= core.size

    @staticmethod
    def execute_ab(core, ins_reg, src_reg, dst_reg):
        if src_reg.ins.a == 0:
            op_codes.terminate_process(core, ins_reg)
            return
        dst_reg.ins.b %= src_reg.ins.a
        dst_reg.ins.b %= core.size

    @staticmethod
    def execute_ba(core, ins_reg, src_reg, dst_reg):
        if src_reg.ins.b == 0:
            op_codes.terminate_process(core, ins_reg)
            return
        dst_reg.ins.a %= src_reg.ins.b
        dst_reg.ins.a %= core.size

    @staticmethod
    def execute_f(core, ins_reg, src_reg, dst_reg):
        mod.execute_a(core, ins_reg, src_reg, dst_reg)
        mod.execute_b(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_x(core, ins_reg, src_reg, dst_reg):
        mod.execute_ab(core, ins_reg, src_reg, dst_reg)
        mod.execute_ba(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_i(core, ins_reg, src_reg, dst_reg):
        mod.execute_f(core, ins_reg, src_reg, dst_reg)

    @staticmethod
    def execute_after(core, ins_reg, src_reg, dst_reg):
        pass
