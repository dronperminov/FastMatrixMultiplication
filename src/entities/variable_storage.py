from typing import Set


class VariableStorage:
    def __init__(self) -> None:
        self.name2index = dict()
        self.index2name = dict()
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

    def get_real(self) -> Set[int]:
        return {self.name2index[name] for name in self.real}

    def __len__(self) -> int:
        return len(self.name2index)
