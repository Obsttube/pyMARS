from operators import op_codes
import core
import instruction
import register
import warior
import loader


if __name__ == "__main__":
    core_size = 20
    main_core = core.Core(core_size)
    main_loader = loader.Loader(main_core)
    # load instructions
    first_warior = warior.Warior("first_warior", "#ff0000", 0)
    main_core.add_warior(first_warior)
    main_loader.load_file_at(first_warior, "agony3.1.txt", 0, core_size)
    second_warior = warior.Warior("second_warior", "#00ff00", 4)
    main_core.add_warior(second_warior)
    '''main_core.set_at(0, instruction.Instruction(
        first_warior, main_core.size, "ADD", "B", "$", 0, "$", 1))
    main_core.set_at(4, instruction.Instruction(
        second_warior, main_core.size, "ADD", "B", "$", 0, "$", 1))'''

    while True:
        main_core.execute_current_ins()
        print(main_core)
        # break
        if main_core.wariors_alive() < 2:
            print(f"{main_core.get_winning_warior().name} won!")
            break
