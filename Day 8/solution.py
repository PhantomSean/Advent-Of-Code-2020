from copy import deepcopy


def valAfterOneIter(program: list) -> (int, bool):
    i, val = 0, 0
    seen = set()
    while i < len(program):
        operation, arg = program[i][0], int(program[i][1])
        if i not in seen:
            seen.add(i)
            if operation == 'nop':
                i += 1
            elif operation == 'acc':
                i += 1
                val += arg
            elif operation == 'jmp':
                i += arg
        else:
            return (val, True)
    return (val, False)

def finalVal(program: list) -> int:
    i = 0
    val, loop = valAfterOneIter(program)
    while loop:
        copy = deepcopy(program)
        op, arg = program[i][0], int(program[i][1])
        if op == 'nop' and arg != 0:
            copy[i][0] = 'jmp'
        elif op == 'jmp':
            copy[i][0] = 'nop'
        val, loop = valAfterOneIter(copy)
        i += 1
    return val

with open('Day 8/input.txt') as file:
    program = [operation.strip().split() for operation in file.readlines()]


print(f"Part 1 = {valAfterOneIter(program)}")
print(f"Part 2 = {finalVal(program)}")