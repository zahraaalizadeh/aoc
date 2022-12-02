import dataclasses


@dataclasses.dataclass
class Data:
    def __init__(self, data) -> None:
        self.data = data
        self.rows: list = self.get_rows()

    def get_rows(self) -> list:
        return [Row(line) for line in self.data.split("\n")]


@dataclasses.dataclass
class Row:
    def __init__(self, row) -> None:
        self.row = row
        self.columns = self.get_columns()

    def get_columns(self) -> list:
        return self.row.split(" ")