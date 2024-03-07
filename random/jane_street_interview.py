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
        for attr_name, attr_value in self.__dict__.items():
            child_attr = self.__dict__.get(attr_value["child"])
            if not child_attr:  # fact without a child ( mm, sec. etc )
                continue
            child_attr["parent"] = attr_name
            child_attr["parent_divider"] = 1 / attr_value["child_multiplier"]
            self.__dict__[attr_value["child"]].update(child_attr)

    def _crawl_up(self, __from, __to, __source_value):
        anchor_fact = self.__getattribute__(__from)
        return_value = __source_value

        if anchor_fact.get("parent") is None:
            return None  # no need to loop to crawl up if we're at the top fact in the hierarchy

        while anchor_fact["name"] != __to:
            if anchor_fact.get("parent") is None:
                # reached the top fact in hierarchy without reaching the __to
                return None

            return_value *= anchor_fact["parent_divider"]
            anchor_fact = self.__getattribute__(anchor_fact["parent"])

        return return_value

    def _crawl_down(self, __from, __to, __source_value):
        anchor_fact = self.__getattribute__(__from)
        return_value = __source_value

        if anchor_fact.get("child") is None:
            # no need to loop to crawl down if we're at the bottom fact in the hierarchy
            return None

        while anchor_fact["name"] != __to:
            if anchor_fact.get("child") is None:
                # reached the bottom fact in hierarchy without reaching the __to
                return None

            return_value *= anchor_fact["child_multiplier"]
            try:
                anchor_fact = self.__getattribute__(anchor_fact["child"])
            except AttributeError:
                # if we reach child that is not declared in the facts (sec.)
                return None

        return return_value

    def crawl(self, __from, __to, val):
        return self._crawl_up(__from, __to, val) or self._crawl_down(__from, __to, val) or "not convertible"


def parse_query(query_param: str) -> Tuple[str, str, int]:
    try:
        _value, query_from, _, _, query_to = query_param.split(" ")
        value_numeric = int(_value)
    except Exception as e:
        raise ValueError(f"Cannot parse query - {e}")
    return query_from, query_to, value_numeric


if __name__ == "__main__":
    facts = Facts()
    facts.register_fact({"name": "m", "child": "ft", "child_multiplier": 3.28}),
    facts.register_fact({"name": "ft", "child": "in", "child_multiplier": 12}),
    facts.register_fact({"name": "in", "child": "mm", "child_multiplier": 25}),
    facts.register_fact({"name": "mm", "child": None, "child_multiplier": None}),
    facts.register_fact({"name": "sec", "child": None, "child_multiplier": None}),
    facts.register_fact({"name": "km", "child": "m", "child_multiplier": 1000}),
    facts.register_fact({"name": "hr", "child": "min", "child_multiplier": 60}),
    facts.register_fact({"name": "min", "child": "sec", "child_multiplier": 60}),
    facts.double_link_facts()
    # print(facts.__dict__)

    queries = [
        "1 hr = ? sec",
        "2 m = ? in",
        "13 in = ? m",
        "13 in = ? hr"
    ]
    for query in queries:
        start, end, source_value = parse_query(query)
        result = facts.crawl(start, end, source_value)
        print(f"{query} => {result}")
