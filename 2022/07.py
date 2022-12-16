import dataclasses
import enum
import re
from typing import TypeVar

import aocd

Node = TypeVar("Node")

COMMAND_CD_REGEX = r"\$ cd ([\w/.]+)"
COMMAND_LS_REGEX = r"\$ ls"
DIR_REGEX = r"dir (\w+)"
FILE_REGEX = r"(\d+) ([\w.]+)"


class FileType(enum.Enum):
    DIR = "DIR"
    FILE = "FILE"


@dataclasses.dataclass
class Node:
    name: str
    filename: str
    file_type: FileType
    parent_directory: Node | None
    size: int = 0


file_system = {}


def reset_file_system() -> None:
    root = Node(name="/", filename="/", file_type=FileType.DIR, parent_directory=None)
    file_system = {"/": root}


def get_filename(current_path: str, name: str) -> str:
    filename = current_path + "/" + name
    filename = filename.replace("//", "/")
    return filename


def get_new_current_path(current_path: str, new_path: str) -> str:
    if new_path == "/":
        current_path = "/"
    elif new_path == "..":
        if current_path == "/":
            pass
        else:
            tmp = current_path.split("/")
            tmp.pop()
            current_path = "/".join(tmp)
    else:
        current_path = current_path + "/" + new_path
    current_path = current_path.replace("//", "/")
    if not current_path:
        return "/"
    return current_path


def update_from_command(current_path: str, new_path: str) -> str:
    updated_current_path = get_new_current_path(current_path, new_path)
    if updated_current_path not in file_system:
        add_new_directory(current_path, updated_current_path)
    return updated_current_path


def add_new_directory(current_path: str, updated_current_path: str) -> Node:
    name = updated_current_path.split("/").pop()
    node = Node(
        name=name,
        filename=updated_current_path,
        file_type=FileType.DIR,
        parent_directory=current_path,
    )
    file_system[updated_current_path] = node


def add_new_file(current_path: str, filename: str, name: str, size: int) -> Node:
    node = Node(
        name=name,
        filename=filename,
        file_type=FileType.FILE,
        parent_directory=current_path,
        size=size,
    )
    file_system[filename] = node


def update_file_details(current_path: str, name: str, size: int) -> None:
    filename = get_filename(current_path, name)
    if filename not in file_system:
        add_new_file(current_path, filename, name, size)


def read_input(input: str) -> None:
    current_path = "/"
    lines = input.split("\n")
    for line in lines:
        if line == "$ ls":
            # Go to the next line
            continue
        match = re.match(COMMAND_CD_REGEX, line)
        if match:
            current_path = update_from_command(current_path, new_path=match.group(1))
        match = re.match(DIR_REGEX, line)
        if match:
            dir_path = get_filename(current_path, match.group(1))
            if dir_path not in file_system:
                add_new_directory(current_path, dir_path)
        match = re.match(FILE_REGEX, line)
        if match:
            size = int(match.group(1))
            name = match.group(2)
            update_file_details(current_path, name, size)


def calculate_dir_size() -> None:
    for filename, node in file_system.items():
        if node.file_type == FileType.FILE:
            # Add the file size to all parent directories
            parents = filename.split("/")[:-1]
            while parents:
                dir_filename = "/".join(parents)
                if not dir_filename:
                    dir_filename = "/"
                dir_node = file_system[dir_filename]
                dir_node.size = dir_node.size + node.size
                file_system[dir_filename] = dir_node
                parents.pop()
                if dir_filename == "/":
                    # we have applied the size up to the root directory
                    break


def part_one(input: str) -> int:
    reset_file_system()
    read_input(input)
    calculate_dir_size()
    result = 0
    for node in file_system.values():
        if node.file_type == FileType.DIR:
            if node.size <= 100000:
                result = result + node.size
    return result


def part_two() -> int:
    root = file_system["/"]
    available_space = 70000000 - root.size
    required_space = 30000000 - available_space
    result = root.size
    for node in file_system.values():
        if node.file_type == FileType.DIR and result > node.size >= required_space:
            result = node.size
    return result


def print_file_system():
    for key, node in sorted(file_system.items(), key=lambda x: x[0]):
        print(f"{key} : {node.file_type} - {node.size}")


def test(input: str) -> None:
    assert part_one(input) == 95437
    assert part_two() == 24933642


sample_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
# test(sample_input)

input = aocd.get_data(day=7, year=2022)
print(f"part one: {part_one(input)}")
print(f"part two: {part_two()}")
print_file_system()
