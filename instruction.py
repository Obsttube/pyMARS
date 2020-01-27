class Instruction():

    def __init__(self, core_size, op_code, modifier, a_mode, a, b_mode, b):
        self.op_code = op_code  # e.g. "MOV"
        self.modifier = modifier  # e.g. "I"
        self.a_mode = a_mode  # e.g. "#"
        self.a = a % core_size  # e.g. 5
        self.b_mode = b_mode  # e.g. "$"
        self.b = b % core_size  # e.g. 1

    def __str__(self):
        return (f"op_code: {self.op_code}"
                f", modifier: {self.modifier}, a_mode: {self.a_mode}"
                f", a: {self.a}, b_mode: {self.b_mode}, b: {self.b}")

    def __eq__(self, other):
        if not isinstance(other, Instruction):
            raise NotImplementedError
        if (self.op_code == other.op_code
                and self.modifier == other.modifier
                and self.a_mode == other.a_mode
                and self.a == other.a
                and self.b_mode == other.b_mode
                and self.b == other.b):
            return True
        return False
