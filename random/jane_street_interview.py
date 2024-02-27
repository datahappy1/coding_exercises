"""
example facts:
m = 3.28 ft
ft = 12 in
hr = 60 min
min = 60 sec
example queries:
2 m = ? in --> answer = 78.72
13 in = ? m --> answer = 0.330 (roughly)
13 in = ? hr --> "not convertible"
"""
from typing import List, Optional, Tuple


class Fact:
    def __init__(self, name, child_fact, child_multiplier):
        self.name = name
        self.child_fact = child_fact
        self.child_multiplier = child_multiplier

    def __repr__(self):
        return str(self.__dict__)


class DoubleLinkedFact(Fact):
    def __init__(self, name, parent_fact, parent_divider, child_fact, child_multiplier):
        super().__init__(name, child_fact, child_multiplier)
        self.parent_fact = parent_fact
        self.parent_divider = parent_divider


class LinkedFactsList:
    def __init__(self, facts_list: List[Fact]):
        self._facts_keyed_by_childs = {
            fact.child_fact: fact for fact in facts_list if fact.child_fact
        }
        self._facts_list = [self._double_link_fact(fact) for fact in facts_list]

    def _double_link_fact(self, fact: Fact) -> DoubleLinkedFact:
        parent_fact = self._facts_keyed_by_childs.get(fact.name)
        return DoubleLinkedFact(
            name=fact.name,
            parent_fact=parent_fact.name if parent_fact else None,
            parent_divider=1 / parent_fact.child_multiplier if parent_fact else None,
            child_fact=fact.child_fact if fact else None,
            child_multiplier=fact.child_multiplier,
        )

    def _crawl_up(self, __from: str, __to: str, val: int) -> Optional[float]:
        for el in self._facts_list:
            if el.name == __from and el.name != __to:
                val *= el.parent_divider if el.parent_divider else 1
                return self._crawl_up(el.parent_fact, __to, val)
            elif el.name == __from == __to:
                return val

    def _crawl_down(self, __from: str, __to: str, val: int) -> Optional[float]:
        for el in self._facts_list:
            if el.name == __from and el.name != __to:
                val *= el.child_multiplier if el.child_multiplier else 1
                return self._crawl_down(el.child_fact, __to, val)
            elif el.name == __from == __to:
                return val

    def crawl(self, __from: str, __to: str, val: int) -> Optional[float]:
        return self._crawl_up(__from, __to, val) or self._crawl_down(__from, __to, val)


def parse_query(query_param: str) -> Tuple[str, str, int]:
    _qs = query_param.split(" ")
    return _qs[1], _qs[4], int(_qs[0])


if __name__ == "__main__":
    query = "13 in = ? hr"
    start, end, m = parse_query(query)
    linked_facts_list = LinkedFactsList(
        facts_list=[
            Fact("m", "ft", 3.28),
            Fact("ft", "in", 12),
            Fact("in", "mm", 25),
            Fact("mm", None, None),
            Fact("km", "m", 1000),
            Fact("hr", "min", 60),
            Fact("min", "sec", 60)
        ]
    )
    result = linked_facts_list.crawl(start, end, m) or "not convertible"
    print(f"{query} => {result}")
