import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file_path = os.path.join(__location__, "input.txt")


def format_line(string: str) -> str:
    return string.replace("\n", "")


def read_input() -> dict:
    input = {}
    elf_number = 1
    try:
        with open(file_path, "r") as f:
            elf_calories = []
            content = f.readlines()
            for line in content:
                line = format_line(line)
                if line:
                    elf_calories.append(int(line))
                else:
                    # Heading to the next elf calories so add the sum calories of the last elf
                    elf_sum_calories = sum(elf_calories)
                    input[elf_number] = elf_sum_calories
                    # reset calories and go to next elf
                    elf_calories = []
                    elf_number += 1
    except Exception as e:
        print(f"Error: {str(e)}")
    return input


def get_max_elf_key(input: dict) -> int:
    return max(input, key=input.get)


def get_top_calories(input: dict, n=3) -> list:
    result = []
    for i in range(1, n + 1):
        max_elf = get_max_elf_key(input)
        max_calories = input.pop(max_elf)
        result.append(max_calories)
        print(f"{i} - Elf {max_elf}: {max_calories}")
    return result


input = read_input()

top_calories = get_top_calories(input)
print(f"SUM: {sum(top_calories)}")
