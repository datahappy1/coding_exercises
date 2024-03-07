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
from typing import Tuple


class Facts:
    def register_fact(self, fact):
        self.__setattr__(fact["name"], fact)

    def double_link_facts(self):
        for attr_name, attr_val in self.__dict__.items():
            try:
                _updated_attr = self.__dict__.get(attr_val["child"])
                _updated_attr["parent"] = attr_name
                _updated_attr["parent_divider"] = 1 / attr_val["child_multiplier"]
                self.__dict__[attr_val["child"]].update(_updated_attr)
            except TypeError:
                pass

    def _crawl_up(self, __from, __to, __source_value):
        _anchor_fact = self.__getattribute__(__from)
        _val = __source_value

        if _anchor_fact.get("parent") is None:
            return None

        while _anchor_fact.get("parent") != _anchor_fact["name"] and _anchor_fact["name"] != __to:
            if _anchor_fact.get("parent_divider") is None:
                return None
            _val *= _anchor_fact["parent_divider"]
            _anchor_fact = self.__getattribute__(_anchor_fact["parent"])
            if _val > __source_value:
                # the value increased, so clearly crawling the wrong direction
                return None
        return _val

    def _crawl_down(self, __from, __to, __source_value):
        _anchor_fact = self.__getattribute__(__from)
        _val = __source_value

        if _anchor_fact.get("child") is None:
            return None

        while _anchor_fact.get("child") != _anchor_fact["name"] and _anchor_fact["name"] != __to:
            if _anchor_fact.get("child_multiplier") is None:
                return None
            _val *= _anchor_fact["child_multiplier"]
            try:
                _anchor_fact = self.__getattribute__(_anchor_fact["child"])
            except AttributeError:
                return None
        return _val

    def crawl(self, __from, __to, val):
        return self._crawl_up(__from, __to, val) or self._crawl_down(__from, __to, val) or "not compatible"


def parse_query(query_param: str) -> Tuple[str, str, int]:
    try:
        _value, _query_from, _, _, _query_to = query_param.split(" ")
        _value_numeric = int(_value)
    except Exception as e:
        raise ValueError(f"Cannot parse query - {e}")
    return _query_from, _query_to, _value_numeric


if __name__ == "__main__":
    query = "10 m = ? mm"
    start, end, source_value = parse_query(query)
    facts = Facts()
    facts.register_fact({"name": "m", "child": "ft", "child_multiplier": 3.28}),
    facts.register_fact({"name": "ft", "child": "in", "child_multiplier": 12}),
    facts.register_fact({"name": "in", "child": "mm", "child_multiplier": 25}),
    facts.register_fact({"name": "mm", "child": None, "child_multiplier": None}),
    facts.register_fact({"name": "km", "child": "m", "child_multiplier": 1000}),
    facts.register_fact({"name": "hr", "child": "min", "child_multiplier": 60}),
    facts.register_fact({"name": "min", "child": "sec", "child_multiplier": 60}),
    facts.double_link_facts()

    # print(facts.__dict__)

    result = facts.crawl(start, end, source_value) or "not convertible"
    print(f"{query} => {result}")
