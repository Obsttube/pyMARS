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
    # add instructions to core
    test_core.set_at(0, instruction.Instruction(
        None, test_core.size, "DIV", "A", "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        None, test_core.size, "ADD", "B", "#", 3, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute(0)
    # check if it was executed correctly (if third block was updated with correct values)
    assert test_core.get_at(2) == instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 1, "}", 7)


def test_a_zero():
    '''
    Initialize core with 100 blocks.
    Core is automatically initialized with DAT.F $0, $0.
    Only 3 blocks are required, but MOD core_size is being applied to some operations,
    so core_size must be greater.
    '''
    test_core = core.Core(100)
    test_warior = warior.Warior("test_warior", "#ff0000")
    test_core.add_warior(test_warior)
    # add instructions to core
    test_core.set_at(0, instruction.Instruction(
        test_warior, test_core.size, "DIV", "A", "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        None, test_core.size, "ADD", "B", "#", 0, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute_current_ins()
    # check if it was executed correctly (if process has been terminated)
    assert len(test_warior.processes) == 0


def test_b():
    '''
    Initialize core with 100 blocks.
    Core is automatically initialized with DAT.F $0, $0.
    Only 3 blocks are required, but MOD core_size is being applied to some operations,
    so core_size must be greater.
    '''
    test_core = core.Core(100)
    # add instructions to core
    test_core.set_at(0, instruction.Instruction(
        None, test_core.size, "DIV", "B", "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        None, test_core.size, "ADD", "B", "#", 3, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute(0)
    # check if it was executed correctly (if third block was updated with correct values)
    assert test_core.get_at(2) == instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 1)


def test_ab():
    '''
    Initialize core with 100 blocks.
    Core is automatically initialized with DAT.F $0, $0.
    Only 3 blocks are required, but MOD core_size is being applied to some operations,
    so core_size must be greater.
    '''
    test_core = core.Core(100)
    # add instructions to core
    test_core.set_at(0, instruction.Instruction(
        None, test_core.size, "DIV", "AB", "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        None, test_core.size, "ADD", "B", "#", 3, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute(0)
    # check if it was executed correctly (if third block was updated with correct values)
    assert test_core.get_at(2) == instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 2)


def test_ba():
    '''
    Initialize core with 100 blocks.
    Core is automatically initialized with DAT.F $0, $0.
    Only 3 blocks are required, but MOD core_size is being applied to some operations,
    so core_size must be greater.
    '''
    test_core = core.Core(100)
    # add instructions to core
    test_core.set_at(0, instruction.Instruction(
        None, test_core.size, "DIV", "BA", "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        None, test_core.size, "ADD", "B", "#", 3, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute(0)
    # check if it was executed correctly (if third block was updated with correct values)
    assert test_core.get_at(2) == instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 1, "}", 7)


def test_f():
    '''
    Initialize core with 100 blocks.
    Core is automatically initialized with DAT.F $0, $0.
    Only 3 blocks are required, but MOD core_size is being applied to some operations,
    so core_size must be greater.
    '''
    test_core = core.Core(100)
    # add instructions to core
    test_core.set_at(0, instruction.Instruction(
        None, test_core.size, "DIV", "F", "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        None, test_core.size, "ADD", "B", "#", 3, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute(0)
    # check if it was executed correctly (if third block was updated with correct values)
    assert test_core.get_at(2) == instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 1, "}", 1)


def test_x():
    '''
    Initialize core with 100 blocks.
    Core is automatically initialized with DAT.F $0, $0.
    Only 3 blocks are required, but MOD core_size is being applied to some operations,
    so core_size must be greater.
    '''
    test_core = core.Core(100)
    # add instructions to core
    test_core.set_at(0, instruction.Instruction(
        None, test_core.size, "DIV", "X", "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        None, test_core.size, "ADD", "B", "#", 3, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute(0)
    # check if it was executed correctly (if third block was updated with correct values)
    assert test_core.get_at(2) == instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 1, "}", 2)


def test_i():
    '''
    Initialize core with 100 blocks.
    Core is automatically initialized with DAT.F $0, $0.
    Only 3 blocks are required, but MOD core_size is being applied to some operations,
    so core_size must be greater.
    '''
    test_core = core.Core(100)
    # add instructions to core
    test_core.set_at(0, instruction.Instruction(
        None, test_core.size, "DIV", "I", "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        None, test_core.size, "ADD", "B", "#", 3, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute(0)
    # check if it was executed correctly (if third block was updated with correct values)
    assert test_core.get_at(2) == instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 1, "}", 1)
