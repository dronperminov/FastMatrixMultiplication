import os
import random
from typing import Callable, List, Optional


class PathChecker:
    def __init__(self, checked_path: str = "checked.txt", buffer_size: int = 1024) -> None:
        self.checked_path = checked_path
        self.buffer_size = buffer_size
        self.checked = set()

        if os.path.exists(checked_path):
            with open(checked_path, "r") as f:
                self.checked = set(f.read().splitlines())
            print(f"Already checked {len(self.checked)} paths")

    def get_paths(self, path: str, validate: Optional[Callable[[str], bool]] = None, shuffle: bool = False) -> List[str]:
        if os.path.isfile(path):
            return [path]

        paths = []
        for path, _, filenames in os.walk(path):
            for filename in sorted(filenames):
                if validate is None or validate(filename):
                    paths.append(os.path.join(path, filename).replace("\\", "/"))

        paths = [path for path in paths if path not in self.checked]
        if shuffle:
            random.shuffle(paths)

        return paths

    def add_checked(self, path: str):
        self.checked.add(path)
        if len(self.checked) % self.buffer_size == 0:
            self.save()

    def save(self) -> None:
        with open(self.checked_path, "w") as f:
            f.write("\n".join(self.checked))
