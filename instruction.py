class Instruction():

    def __init__(self, op_code, modifier, a_mode, a, b_mode, b):
        self.op_code = op_code  # e.g. "MOV"
        self.modifier = modifier  # e.g. "I"
        self.a_mode = a_mode  # e.g. "#"
        self.a = a  # e.g. 5
        self.b_mode = b_mode  # e.g. "$"
        self.b = b  # e.g. 1

    def __str__(self):
        return (f"op_code: {self.op_code}"
                f", modifier: {self.modifier}, a_mode: {self.a_mode}"
                f", a: {self.a}, b_mode: {self.b_mode}, b: {self.b}")
