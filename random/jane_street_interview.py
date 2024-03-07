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
from typing import Tuple, Optional


class Fact:
    def __init__(
        self,
        name: str,
        child: Optional[str],
        child_multiplier: Optional[float],
        parent: Optional[str] = None,
        parent_divider: Optional[float] = None,
    ):
        self.name: str = name
        self.child: str = child
        self.child_multiplier: float = child_multiplier
        self.parent: Optional[str] = parent
        self.parent_divider: Optional[float] = parent_divider

    def __repr__(self):
        return str(self.__dict__)


class Facts:
    def register_fact(self, fact: Fact):
        self.__setattr__(fact.name, fact)

    def double_link_facts(self):
        for attr_name, attr_value in self.__dict__.items():
            _child = self.__dict__.get(attr_value.child)
            if not _child:  # fact without a child ( mm, sec. etc )
                continue

            _child.parent = attr_name
            _child.parent_divider = 1 / attr_value.child_multiplier
            self.__dict__[attr_value.child] = _child

    def _crawl_up(self, __from: str, __to: str, __source_value: int):
        anchor_fact = self.__getattribute__(__from)
        return_value = __source_value

        if anchor_fact.parent is None:
            return None  # no need to loop to crawl up if we're at the top fact in the hierarchy

        while anchor_fact.name != __to:
            if anchor_fact.parent is None:
                # reached the top fact in hierarchy without reaching the __to
                return None

            return_value *= anchor_fact.parent_divider
            anchor_fact = self.__getattribute__(anchor_fact.parent)

        return return_value

    def _crawl_down(self, __from: str, __to: str, __source_value: int):
        anchor_fact = self.__getattribute__(__from)
        return_value = __source_value

        if anchor_fact.child is None:
            # no need to loop to crawl down if we're at the bottom fact in the hierarchy
            return None

        while anchor_fact.name != __to:
            if anchor_fact.child is None:
                # reached the bottom fact in hierarchy without reaching the __to
                return None

            return_value *= anchor_fact.child_multiplier
            try:
                anchor_fact = self.__getattribute__(anchor_fact.child)
            except AttributeError:
                # if we ever reach child that is not declared in the facts
                return None

        return return_value

    def crawl(self, __from, __to, val):
        return (
            self._crawl_up(__from, __to, val)
            or self._crawl_down(__from, __to, val)
            or "not convertible"
        )


def parse_query(query_param: str) -> Tuple[str, str, int]:
    try:
        _value, query_from, _, _, query_to = query_param.split(" ")
        value_numeric = int(_value)
    except Exception as e:
        raise ValueError(f"Cannot parse query - {e}")
    return query_from, query_to, value_numeric


if __name__ == "__main__":
    facts = Facts()
    facts.register_fact(Fact(name="m", child="ft", child_multiplier=3.28)),
    facts.register_fact(Fact(name="ft", child="in", child_multiplier=12)),
    facts.register_fact(Fact(name="in", child="mm", child_multiplier=25)),
    facts.register_fact(Fact(name="mm", child=None, child_multiplier=None)),
    facts.register_fact(Fact(name="sec", child=None, child_multiplier=None)),
    facts.register_fact(Fact(name="km", child="m", child_multiplier=1000)),
    facts.register_fact(Fact(name="hr", child="min", child_multiplier=60)),
    facts.register_fact(Fact(name="min", child="sec", child_multiplier=60)),
    facts.double_link_facts()
    # print(facts.__dict__)

    queries = ["1 hr = ? sec", "2 m = ? in", "13 in = ? m", "13 in = ? hr"]
    for query in queries:
        start, end, source_value = parse_query(query)
        result = facts.crawl(start, end, source_value)
        print(f"{query} => {result}")
