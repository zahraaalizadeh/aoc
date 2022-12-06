import re
from dataclasses import dataclass

import aocd

INSTRUCTION_REGEX = r"move (\d+) from (\d+) to (\d+)"

@dataclass
class Instruction:
    number: int
    from_stack: str
    to_stack: str

def read_row(row:str, number_of_stacks:int=9) -> list:
    result = []
    for i in range(0, number_of_stacks):
        result.append(row[i*4+1].strip())
    return result

def read_stack_drawing(stack_drawing: list, number_of_stacks:int=9) -> dict[list]:
    result = {}
    # reverse the list to ultimately retrun a stack.
    for r in reversed(stack_drawing):
        row =read_row(r, number_of_stacks)
        for index, item in enumerate(row):
            if item:
                key = str(index+1)
                l = result.get(key, [])
                l.append(item)
                result[key] = l
    return result

def read_instructon(string:str) -> Instruction:
    """Return Number of crates from one crate to another"""
    result = re.search(INSTRUCTION_REGEX, string)
    return Instruction(
        number= int(result.group(1)),
        from_stack= result.group(2),
        to_stack= result.group(3),
    )

def get_result(stack_drawing: dict[str, list]) -> str:
    result = []
    for key in stack_drawing:
        tmp = stack_drawing[key].pop()
        result.append(tmp)
    return "".join(result)

def part_one(input: str, number_of_stacks:int=9, initial_max_crates:int=8) -> str:
    lines = input.split("\n")
    stack_drawing = read_stack_drawing(lines[0:initial_max_crates], number_of_stacks)
    # apply the instruction to the stack drawing
    for line in lines[initial_max_crates+2:]:
        instruction = read_instructon(line)
        for _ in range(0, instruction.number):
            tmp = stack_drawing[instruction.from_stack].pop()
            stack_drawing[instruction.to_stack].append(tmp)
    # get the result
    return get_result(stack_drawing)


def part_two(input: str, number_of_stacks:int=9, initial_max_crates:int=8) -> str:
    lines = input.split("\n")
    stack_drawing = read_stack_drawing(lines[0:initial_max_crates], number_of_stacks)
    # apply the instruction to the stack drawing
    for line in lines[initial_max_crates+2:]:
        instruction = read_instructon(line)
        tmp = stack_drawing[instruction.from_stack][-instruction.number:]
        stack_drawing[instruction.from_stack] = stack_drawing[instruction.from_stack][:-instruction.number]
        stack_drawing[instruction.to_stack].extend(tmp)
    # get the result
    return get_result(stack_drawing)


def test(sample):
    sample_one = part_one(sample, number_of_stacks=3, initial_max_crates=3)
    assert sample_one == "CMZ"
    sample_two = part_two(sample, number_of_stacks=3, initial_max_crates=3)
    assert sample_two == "MCD"

sample = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
test(sample)

input = aocd.get_data(day=5, year=2022)

print(f"Part 1: {part_one(input)}")
print(f"Part 2: {part_two(input)}")