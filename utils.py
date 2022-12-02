import dataclasses


@dataclasses.dataclass
class Data:
    raw_data: str

    def __init__(
        self, raw_data, level1_separator: str = "\n", level2_separator: str = " "
    ) -> None:
        self.raw_data = raw_data
        self.level1_separator = level1_separator
        self.level2_separator = level2_separator
        self.groups = self._read_data()

    def _read_data(self) -> list["Group"]:
        return [
            Group(raw_data=line, level2_separator=self.level2_separator)
            for line in self.raw_data.split(self.level1_separator)
        ]

    def count(self) -> int:
        return len(self.groups)

    def first(self) -> "Group":
        return self.groups[0]

    def last(self) -> "Group":
        return self.groups[-1]

    def print(self) -> None:
        for group in self.groups:
            for item in group.items:
                print(item)


@dataclasses.dataclass
class Group:
    raw_data: str

    def __init__(self, raw_data: str, level2_separator: str = " ") -> None:
        self.raw_data = raw_data
        self.level2_separator = level2_separator
        self.items = self._read_data()

    def _read_data(self) -> list["Item"]:
        return [
            Item(raw_data=item) for item in self.raw_data.split(self.level2_separator)
        ]

    def first(self) -> "Item":
        return self.items[0]

    def last(self) -> "Item":
        return self.items[-1]

    def count(self) -> int:
        return len(self.items)

    def print(self) -> None:
        for item in self.items:
            print(item)


@dataclasses.dataclass
class Item:
    raw_data: str
