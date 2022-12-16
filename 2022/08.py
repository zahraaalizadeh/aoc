import math

import aocd

import utils


def is_only_tallest_tree(item: utils.Item, tree_list: list) -> bool:
    tree_list = sorted(tree_list)
    if max(tree_list) == item:
        tree_list.pop()
        next_tree = tree_list.pop()
        if next_tree != item:
            return True
    return False


def number_of_visible_trees(item: utils.Item, tree_list: list | None) -> int:
    """Assumes the first tree in the list is the item"""
    result = 0
    # print(f"{item=} - {tree_list=}")
    if tree_list:
        for tree in tree_list[1:]:
            if item > tree:
                result += 1
            if item < tree or item == tree:
                result += 1
                break
    return result


def get_edge_trees(data: utils.Data) -> int:
    return 2 * data.count() + 2 * (data.first().count() - 2)


def get_interior_visible_trees(data: utils.Data) -> int:
    interior_visible_trees = 0
    for i_row, group in enumerate(data.groups[1:-1]):
        for i_col, item in enumerate(group.items[1:-1]):
            left = data.groups[i_row + 1].items[: i_col + 2]
            right = data.groups[i_row + 1].items[i_col + 1 :]
            top = [group.items[i_col + 1] for group in data.groups[: i_row + 2]]
            down = [group.items[i_col + 1] for group in data.groups[i_row + 1 :]]
            result = [
                is_only_tallest_tree(item, tree_list)
                for tree_list in [right, left, top, down]
            ]
            # print(f"{i_row + 1} - {i_col+1} - {item=} - {result=}")
            if any(result):
                # it's visible in the row
                interior_visible_trees += 1
                continue
    return interior_visible_trees


def part_one(data: utils.Data) -> int:
    trees_on_edge = get_edge_trees(data)
    interior_visible_trees = get_interior_visible_trees(data)
    return trees_on_edge + interior_visible_trees


def part_two(data: utils.Data):
    highest_scenic_score = 0
    for i_row, group in enumerate(data.groups[1:-1]):
        for i_col, item in enumerate(group.items[1:-1]):
            left = data.groups[i_row + 1].items[: i_col + 2]
            left.reverse()
            right = data.groups[i_row + 1].items[i_col + 1 :]
            top = [group.items[i_col + 1] for group in data.groups[: i_row + 2]]
            top.reverse()
            down = [group.items[i_col + 1] for group in data.groups[i_row + 1 :]]
            visible_trees = [
                number_of_visible_trees(item, tree_list)
                for tree_list in [right, left, top, down]
            ]
            # print(f"{i_row + 1} - {i_col+1} - {item=} - {visible_trees=}")
            result = math.prod(visible_trees)
            if result > highest_scenic_score:
                highest_scenic_score = result
    return highest_scenic_score


def test(sample):
    data = utils.Data(sample, level2_separator="")
    assert get_edge_trees(data) == 16
    assert part_one(data) == 21
    print(part_two(data))
    assert part_two(data) == 8


sample = """30373
25512
65332
33549
35390"""
test(sample)

input = aocd.get_data(day=8, year=2022)
data = utils.Data(input, level2_separator="")
print(f"part one: {part_one(data)}")
print(f"part two: {part_two(data)}")
