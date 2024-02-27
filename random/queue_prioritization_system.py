from enum import Enum
from typing import List, Any, Optional
from queue import Queue, LifoQueue


class Item:
    def __init__(self, item: Any):
        self._item: Any = item

    def __str__(self):
        return str(self._item)


class Priority(Enum):
    Low = 10
    High = 20


class QueueType(Enum):
    queue = Queue
    lifo = LifoQueue


class QueuePrioritizationSystem:
    @staticmethod
    def priority_to_queue_name(priority_name: str) -> str:
        return f"{priority_name}_data".lower()

    @staticmethod
    def get_sorted_priorities(priorities: List[Priority]) -> List[Priority]:
        return sorted(priorities, key=lambda x: x.value, reverse=True)

    def __init__(self, priorities: List[Priority], queue_type: QueueType):
        self._sorted_priorities = QueuePrioritizationSystem.get_sorted_priorities(
            priorities=priorities
        )
        for priority in self._sorted_priorities:
            self._set_queue(priority=priority, queue_type=queue_type)

    def _set_queue(self, priority: Priority, queue_type: QueueType) -> None:
        self.__setattr__(
            QueuePrioritizationSystem.priority_to_queue_name(priority.name),
            queue_type.value(),
        )

    def _get_queue_by_priority(self, priority: Priority) -> QueueType.value:
        return self.__getattribute__(
            QueuePrioritizationSystem.priority_to_queue_name(
                priority_name=priority.name
            )
        )

    def _get_highest_priority_queue(self) -> Optional[QueueType.value]:
        for priority in self._sorted_priorities:
            _queue_ref = self._get_queue_by_priority(priority=priority)
            if not _queue_ref.empty():
                print(f"using {priority} priority queue")
                return _queue_ref

        print(f"no priority queue has data")
        return None

    def put_by_priority(self, priority: Priority, item: Item) -> None:
        _queue_ref = self._get_queue_by_priority(priority=priority)
        _queue_ref.put(item)

    def get_by_priority(self, priority: Priority) -> Optional[Item]:
        _queue_ref = self._get_queue_by_priority(priority=priority)
        if not _queue_ref.empty():
            return _queue_ref.get()
        return None

    def get(self) -> Optional[Item]:
        _queue_ref = self._get_highest_priority_queue()
        if _queue_ref:
            return _queue_ref.get()
        return None


if __name__ == "__main__":
    qps = QueuePrioritizationSystem(
        priorities=[Priority.High, Priority.Low], queue_type=QueueType.queue
    )

    for i in range(10):
        qps.put_by_priority(
            item=Item(f"something not-important {i}"), priority=Priority.Low
        )

    print(qps.get_by_priority(priority=Priority.Low))

    for i in range(20):
        qps.put_by_priority(
            item=Item(f"something super-important {i}"), priority=Priority.High
        )

    print(qps.get_by_priority(priority=Priority.High))

    for i in range(42):
        print(qps.get())

    print(qps.get_by_priority(priority=Priority.Low))
