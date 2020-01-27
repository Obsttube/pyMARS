import pytest
import core
import instruction


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
        None, test_core.size, "MUL", "A", "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        None, test_core.size, "ADD", "B", "#", 3, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute(0)
    # check if it was executed correctly (if third block was updated with correct values)
    assert test_core.get_at(2) == instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 15, "}", 7)


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
        None, test_core.size, "MUL", "B", "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        None, test_core.size, "ADD", "B", "#", 3, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute(0)
    # check if it was executed correctly (if third block was updated with correct values)
    assert test_core.get_at(2) == instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 28)


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
        None, test_core.size, "MUL", "AB", "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        None, test_core.size, "ADD", "B", "#", 3, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute(0)
    # check if it was executed correctly (if third block was updated with correct values)
    assert test_core.get_at(2) == instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 21)


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
        None, test_core.size, "MUL", "BA", "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        None, test_core.size, "ADD", "B", "#", 3, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute(0)
    # check if it was executed correctly (if third block was updated with correct values)
    assert test_core.get_at(2) == instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 20, "}", 7)


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
        None, test_core.size, "MUL", "F", "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        None, test_core.size, "ADD", "B", "#", 3, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute(0)
    # check if it was executed correctly (if third block was updated with correct values)
    assert test_core.get_at(2) == instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 15, "}", 28)


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
        None, test_core.size, "MUL", "X", "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        None, test_core.size, "ADD", "B", "#", 3, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute(0)
    # check if it was executed correctly (if third block was updated with correct values)
    assert test_core.get_at(2) == instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 20, "}", 21)


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
        None, test_core.size, "MUL", "I", "$", 1, "$", 2))
    test_core.set_at(1, instruction.Instruction(
        None, test_core.size, "ADD", "B", "#", 3, "*", 4))
    test_core.set_at(2, instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 5, "}", 7))
    # execute only the first instruction
    test_core.execute(0)
    # check if it was executed correctly (if third block was updated with correct values)
    assert test_core.get_at(2) == instruction.Instruction(
        None, test_core.size, "SUB", "AB", "{", 15, "}", 28)
