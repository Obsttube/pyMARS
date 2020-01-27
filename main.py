from operators import op_codes
import core
import instruction
import register


if __name__ == "__main__":
    main_core = core.Core(7)
    # load instructions
    main_core.set_at(0, instruction.Instruction("ADD", "I", "$", 1, "$", 2))
    main_core.set_at(1, instruction.Instruction("DAT", "A", "$", 1, "$", 2))
    main_core.set_at(2, instruction.Instruction("DAT", "A", "$", 3, "$", 4))

    print(main_core.dst_reg.ins)
    main_core.execute(0)
    print(main_core.dst_reg.ins)
    print()
    print(main_core)
