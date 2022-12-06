import aocd


def is_start_of_packet_marker(text: str) -> bool:
    for c in text:
        if text.count(c) > 1:
            return False
    return True


def part_one(input: str, number_of_distinct_chars: int = 4) -> int:
    input_len = len(input)
    for i in range(number_of_distinct_chars, input_len):
        tmp = input[i - number_of_distinct_chars : i]
        if is_start_of_packet_marker(tmp):
            return i


def part_two(input: str) -> int:
    number_of_distinct_chars = 14
    return part_one(input, number_of_distinct_chars)


def test(sample: dict[str, int]) -> None:
    for key, value in sample.items():
        assert (part_one(key), part_two(key)) == value


sample = {
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb": (7, 19),
    "bvwbjplbgvbhsrlpgdmjqwftvncz": (5, 23),
    "nppdvjthqldpwncqszvftbrmjlhg": (6, 23),
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": (10, 29),
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": (11, 26),
}

test(sample)
input = aocd.get_data(day=6, year=2022)
print(part_one(input))
print(part_two(input))
