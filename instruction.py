
VALID_OP_CODES = ["DAT", "MOV", "ADD", "SUB", "MUL", "DIV", "MOD", "JMP",
                  "JMZ", "JMN", "DJN", "SPL", "CMP", "SEQ", "SNE", "SLT", "LDP", "STP", "NOP"]
VALID_MODIFIERS = ["A", "B", "AB", "BA", "F", "X", "I"]


class Instruction():

    def __init__(self, last_warior, core_size, op_code, modifier, a_mode, a, b_mode, b):
        self.last_warior = last_warior  # stores which warior modified the block last
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

    @classmethod
    def from_line(cls, line, warior, core_size):
        # print(line)
        line = line.split(";")[0].strip()  # "SUB.F  $    12, $     1"
        instr_name = line[:3]  # "SUB"
        if instr_name not in VALID_OP_CODES:
            print("unknown instruction")
        line = line[3:]  # ".F  $    12, $     1"
        if line[0] == ".":
            line = line[1:]  # "F  $    12, $     1"
            if line.upper()[0] in ["A", "B", "F", "X", "I"]:
                if line.upper().startswith(("AB", "BA")):
                    modifier = line[:2]
                    line = line[1:]
                else:
                    modifier = line[0]  # "F"
            else:
                print("unknown modifier")
        else:
            modifier = None
        line = line[1:].strip()  # "$    12, $     1"
        ab_mods = ["#", "$", "*", "@", "{", "<", "}", ">"]
        a_mod = line[0]  # "$"
        if a_mod in ab_mods:
            line = line[1:].strip()  # "12, $     1"
        else:
            a_mod = "$"
        line = line.split(",")  # ["12", " $     1"]
        a = line[0].strip()  # "12"
        if not represents_int(a):
            print("a is not an integer")
        a = int(a)
        if len(line) == 1:
            b_mod = None
            b = None
        else:
            line[1] = line[1].strip()
            b_mod = line[1][0]  # "$"
            if b_mod in ab_mods:
                line[1] = line[1][1:].strip()  # "1"
            else:
                b_mod = "$"
            b = line[1].strip()  # "1"
            if not represents_int(b):
                print("b is not an integer")  # TODO: raise exceptions
            b = int(b)
        return cls(warior, core_size, instr_name, modifier, a_mod, a, b_mod, b)


def represents_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
    return False
