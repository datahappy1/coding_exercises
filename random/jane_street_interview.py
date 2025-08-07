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


class TraversalDirection(Enum):
    UP = "UP"
    DOWN = "DOWN"


@dataclass
class UnitNode:
    name: str
    child: Optional["UnitNode"]
    child_multiplier: Optional[float]
    parent: Optional["UnitNode"] = None
    parent_multiplier: Optional[float] = None


class UnitConverter:
    def __init__(self):
        self._unit_nodes: Dict[UnitNode.name, UnitNode] = dict()

    def register_unit_node(self, unit_node: UnitNode):
        self._unit_nodes[unit_node.name] = unit_node

    def add_parents(self):
        for attr_name, attr_value in self._unit_nodes.items():
            _child = self._unit_nodes.get(attr_value.child.name if attr_value.child else None)
            if not _child:  # unit node without a child ( mm, sec. etc )
                continue
            if attr_value.child_multiplier == 0:
                raise ValueError(f"Invalid child multiplier for {attr_name}")

            _child.parent = attr_value
            _child.parent_multiplier = 1 / attr_value.child_multiplier

    @staticmethod
    def _check_traversal_step_validity(
        direction: TraversalDirection, anchor_unit_node: UnitNode
    ):
        if (direction == TraversalDirection.UP and anchor_unit_node.parent is None) or (
                direction == TraversalDirection.DOWN and anchor_unit_node.child is None
        ):
            # no need to traverse up if we're at the top unit node in the hierarchy and vice versa
            return False
        return True

    def _traverse(
        self, from_unit: str, to_unit: str, source_value: float, direction: TraversalDirection
    ):
        current_node = self._unit_nodes.get(from_unit)
        result = source_value

        while current_node.name != to_unit:
            if not self._check_traversal_step_validity(direction, current_node):
                return None

            if direction == TraversalDirection.UP:
                result *= current_node.parent_multiplier
                current_node = self._unit_nodes.get(current_node.parent.name)
            elif direction == TraversalDirection.DOWN:
                result *= current_node.child_multiplier
                try:
                    current_node = self._unit_nodes.get(current_node.child.name)
                except AttributeError:
                    # if we ever reach child that is not declared in the unit nodes
                    return None

        return result

    def traverse(self, from_unit: str, to_unit: str, value: float) -> Optional[float]:
        traverse_up_result = self._traverse(
            from_unit, to_unit, value, direction=TraversalDirection.UP
        )
        traverse_down_result = self._traverse(
            from_unit, to_unit, value, direction=TraversalDirection.DOWN
        )
        return traverse_up_result or traverse_down_result


def parse_query(query_param: str) -> Tuple[str, str, float]:
    pattern = r"^\s*(\d+(?:\.\d+)?)\s+(\w+)\s*=\s*\?\s+(\w+)\s*$"
    match = re.match(pattern, query_param)
    if not match:
        raise ValueError(f"Cannot parse query: '{query_param}'")

    value, from_unit, to_unit = match.groups()
    return from_unit, to_unit, float(value)


if __name__ == "__main__":
    unit_converter = UnitConverter()

    mm_node = UnitNode(name="mm", child=None, child_multiplier=None)
    unit_converter.register_unit_node(mm_node)

    inch_node = UnitNode(name="in", child=mm_node, child_multiplier=25)
    unit_converter.register_unit_node(inch_node)

    ft_node = UnitNode(name="ft", child=inch_node, child_multiplier=12)
    unit_converter.register_unit_node(ft_node)

    meter_node = UnitNode(name="m", child=ft_node, child_multiplier=3.28)
    unit_converter.register_unit_node(meter_node)

    km_node = UnitNode(name="km", child=meter_node, child_multiplier=1000)
    unit_converter.register_unit_node(km_node)

    second_node = UnitNode(name="sec", child=None, child_multiplier=None)
    unit_converter.register_unit_node(second_node)

    minute_node = UnitNode(name="min", child=second_node, child_multiplier=60)
    unit_converter.register_unit_node(minute_node)

    hr_node = UnitNode(name="hr", child=minute_node, child_multiplier=60)
    unit_converter.register_unit_node(hr_node)

    unit_converter.add_parents()

    queries = ["1 hr = ? sec", "2 m = ? in", "13 in = ? m", "13 in = ? hr"]
    for query in queries:
        print(f"Solving query {query}")
        start, end, parsed_source_value = parse_query(query)
        query_result = unit_converter.traverse(start, end, parsed_source_value)
        if query_result is None:
            print(f"{query} not convertible")
        else:
            print(f"{query} => {query_result:.3f}")
