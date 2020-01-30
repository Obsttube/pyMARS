import pytest
import core
import instruction
import warior


def test_a():
    '''
    Initialize core with 100 blocks.
    Core is automatically initialized with DAT.F $0, $0.
    Only 3 blocks are required, but MOD core_size is being applied to some operations,
    so core_size must be greater.
    '''
    test_core = core.Core(100)
    test_warior = warior.Warior("test_warior", "#ff0000")
    test_warior.add_process(3)
    test_core.add_warior(test_warior)
    # add instruction to core
    test_core.set_at(3, instruction.Instruction(
        test_warior, test_core.size, "JMP", "A", "$", 5, "$", 0))
    # execute only the first instruction
    test_core.execute_current_ins()
    # check if warior address has been changed properly
    assert test_warior.processes[test_warior.curr_proc_index] == 8
