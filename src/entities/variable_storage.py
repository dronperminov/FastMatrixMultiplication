from typing import List, Optional


class VariableStorage:
    def __init__(self) -> None:
        self.name2index = dict()
        self.index2name = dict()
        self.index2value = dict()
        self.fresh = set()
        self.real = set()

    def get(self, name: str = "") -> int:
        if name == "":
            name = f"t_{len(self.fresh) + 1}"
            self.fresh.add(name)
        else:
            self.real.add(name)

        if name not in self.name2index:
            index = len(self.name2index) + 1
            self.name2index[name] = index
            self.index2name[index] = name

        return self.name2index[name]

    def set_value(self, index: int, value: bool) -> None:
        self.index2value[index] = value

    def get_value(self, index: int) -> Optional[bool]:
        return self.index2value.get(index, None)

    def get_known(self) -> List[int]:
        return [index if value else -index for index, value in self.index2value.items()]

    def get_real(self) -> List[int]:
        return [self.name2index[name] for name in self.real]

    def __len__(self) -> int:
        return len(self.name2index)

    def fresh_count(self) -> int:
        return len(self.fresh)

    def real_count(self) -> int:
        return len(self.real)
