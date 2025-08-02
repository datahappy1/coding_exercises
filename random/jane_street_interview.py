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
from typing import Tuple, Optional, Dict
from enum import Enum
import re
from dataclasses import dataclass


class CrawlDirection(Enum):
    UP = "UP"
    DOWN = "DOWN"


@dataclass
class Fact:
    name: str
    child: Optional[str]
    child_multiplier: Optional[float]
    parent: Optional[str] = None
    parent_multiplier: Optional[float] = None


class Facts:
    def __init__(self):
        self._facts: Dict[str, Fact] = dict()

    def register_fact(self, fact: Fact):
        self._facts[fact.name] = fact

    def double_link_facts(self):
        for attr_name, attr_value in self._facts.items():
            _child = self._facts.get(attr_value.child)
            if not _child:  # fact without a child ( mm, sec. etc )
                continue
            if attr_value.child_multiplier == 0:
                raise ValueError(f"Invalid child multiplier for {attr_name}")

            _child.parent = attr_name
            _child.parent_multiplier = 1 / attr_value.child_multiplier

    @staticmethod
    def _check_crawl_step_validity(direction: CrawlDirection, anchor_fact: Fact):
        if (direction == CrawlDirection.UP and anchor_fact.parent is None) or (
            direction == CrawlDirection.DOWN and anchor_fact.child is None
        ):
            # no need to crawl up if we're at the top fact in the hierarchy and vice versa
            return False
        return True

    def _crawl(
        self, from_unit: str, to_unit: str, source_value: int, direction: CrawlDirection
    ):
        anchor_fact = self._facts.get(from_unit)
        result = source_value

        while anchor_fact.name != to_unit:
            if self._check_crawl_step_validity(direction, anchor_fact) is False:
                return None

            if direction == CrawlDirection.UP:
                result *= anchor_fact.parent_multiplier
                anchor_fact = self._facts.get(anchor_fact.parent)

            if direction == CrawlDirection.DOWN:
                result *= anchor_fact.child_multiplier
                try:
                    anchor_fact = self._facts.get(anchor_fact.child)
                except AttributeError:
                    # if we ever reach child that is not declared in the facts
                    return None

        return result

    def crawl(self, from_unit, to_unit, value):
        return self._crawl(
            from_unit, to_unit, value, direction=CrawlDirection.UP
        ) or self._crawl(from_unit, to_unit, value, direction=CrawlDirection.DOWN)


def parse_query(query_param: str) -> Tuple[str, str, float]:
    pattern = r"^\s*(\d+(?:\.\d+)?)\s+(\w+)\s*=\s*\?\s+(\w+)\s*$"
    match = re.match(pattern, query_param)
    if not match:
        raise ValueError(f"Cannot parse query: '{query_param}'")

    value, from_unit, to_unit = match.groups()
    return from_unit, to_unit, float(value)


if __name__ == "__main__":
    facts = Facts()
    facts.register_fact(Fact(name="m", child="ft", child_multiplier=3.28))
    facts.register_fact(Fact(name="ft", child="in", child_multiplier=12))
    facts.register_fact(Fact(name="in", child="mm", child_multiplier=25))
    facts.register_fact(Fact(name="mm", child=None, child_multiplier=None))
    facts.register_fact(Fact(name="sec", child=None, child_multiplier=None))
    facts.register_fact(Fact(name="km", child="m", child_multiplier=1000))
    facts.register_fact(Fact(name="hr", child="min", child_multiplier=60))
    facts.register_fact(Fact(name="min", child="sec", child_multiplier=60))
    facts.double_link_facts()

    queries = ["1 hr = ? sec", "2 m = ? in", "13 in = ? m", "13 in = ? hr"]
    for query in queries:
        start, end, parsed_source_value = parse_query(query)
        query_result = facts.crawl(start, end, parsed_source_value)
        if query_result is None:
            print(f"{query} not convertible")
        else:
            print(f"{query} => {query_result}")
