import pytest
import core
import instruction


def chech_for_modifier(modifier):
    '''
    Initialize core with 100 blocks.
    Core is automatically initialized with DAT.F $0, $0.
    Only 3 blocks are required, but MOD core_size is being applied to some operations,
    so core_size must be greater.
    '''
    test_core = core.Core(100)
    # add instructions to core
    test_core.set_at(0, instruction.Instruction(
        test_core.size, "NOP", modifier, "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        test_core.size, "ADD", "B", "#", 3, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        test_core.size, "MOV", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute(0)
    # check if it was executed correctly (if no blocks have been changed)
    assert test_core.get_at(0) == instruction.Instruction(
        test_core.size, "NOP", modifier, "$", 1, "$", 2)
    assert test_core.get_at(1) == instruction.Instruction(
        test_core.size, "ADD", "B", "#", 3, "*", 4)
    assert test_core.get_at(2) == instruction.Instruction(
        test_core.size, "MOV", "AB", "{", 5, "}", 7)
    for i in range(3, 100):
        assert test_core.get_at(i) == instruction.Instruction(
            test_core.size, "DAT", "F", "$", 0, "$", 0)


def test_a():
    chech_for_modifier("A")


def test_b():
    chech_for_modifier("B")


def test_ab():
    chech_for_modifier("AB")


def test_ba():
    chech_for_modifier("BA")


def test_f():
    chech_for_modifier("F")


def test_x():
    chech_for_modifier("X")


def test_i():
    chech_for_modifier("I")
