import itertools
import json
import os
from typing import List, Optional

from src.schemes.scheme import Scheme


class SchemesLoader:
    def __init__(self, additional_directories: Optional[List[str]] = None):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "schemes", "status.json"), "r") as f:
            self.status = json.load(f)

        self.dimension2schemes = dict()
        self.rings = {"ZT": ["ZT"], "Z": ["ZT", "Z"], "Q": ["ZT", "Z", "Q"]}
        self.additional_directories = additional_directories if additional_directories else []

    def load(self, n1: int, n2: int, n3: int, target_ring: str, max_schemes: int = 500) -> List[Scheme]:
        if (n1, n2, n3) in self.dimension2schemes:
            return self.dimension2schemes[(n1, n2, n3)]

        if min(n1, n2, n3) == 1:
            return [Scheme.naive(n1=n1, n2=n2, n3=n3)]

        size = "x".join(map(str, sorted([n1, n2, n3])))
        rank = self.status[size]["ranks"][target_ring]

        schemes = self.__load_from_status(n1=n1, n2=n2, n3=n3, target_ring=target_ring, rank=rank)

        for additional_directory in self.additional_directories:
            schemes.extend(self.__load_from_directory(f"{additional_directory}/{size}/rank{rank}", n1=n1, n2=n2, n3=n3))

        print(f"loader read {len(schemes)} schemes ({n1}x{n2}x{n3}: {rank})")
        schemes = sorted(schemes, key=lambda s: s.complexity())[:max_schemes]

        for nn1, nn2, nn3 in itertools.permutations([n1, n2, n3], r=3):
            self.dimension2schemes[(nn1, nn2, nn3)] = [scheme.copy().set_sizes(nn1, nn2, nn3) for scheme in schemes]

        return self.dimension2schemes[(n1, n2, n3)]

    def __load_from_status(self, n1: int, n2: int, n3: int, rank: int, target_ring: str) -> List[Scheme]:
        size = "x".join(map(str, sorted([n1, n2, n3])))

        schemes = []
        for ring in self.rings[target_ring]:
            for scheme_data in self.status[size]["schemes"].get(ring, []):
                if scheme_data["rank"] == rank:
                    schemes.append(Scheme.load("../" + scheme_data["path"], validate=False).set_sizes(n1, n2, n3))

        return schemes

    def __load_from_directory(self, path: str, n1: int, n2: int, n3: int) -> List[Scheme]:
        if not os.path.exists(path) or not os.path.isdir(path):
            return []

        filenames = [f"{path}/{filename}" for filename in os.listdir(path)][:5000]
        schemes = [Scheme.load(filename, validate=False).set_sizes(n1, n2, n3) for filename in filenames]
        return schemes
