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
    queue = Queue()
    lifo = LifoQueue()


class QueuePrioritizationSystem:
    @staticmethod
    def priority_to_queue_name(priority: Priority) -> str:
        return f"{priority}_data"

    @staticmethod
    def get_sorted_priorities(priorities: List[Priority]) -> List[Priority]:
        return sorted(priorities, key=lambda x: x.value, reverse=True)

    def __init__(self, priorities: List[Priority], queue_type: QueueType):
        self._sorted_priorities = QueuePrioritizationSystem.get_sorted_priorities(
            priorities=priorities
        )
        for _priority in self._sorted_priorities:
            self.__setattr__(
                QueuePrioritizationSystem.priority_to_queue_name(_priority),
                queue_type.value,
            )

    def put_by_priority(self, priority: Priority, item: Item) -> None:
        self.__getattribute__(
            QueuePrioritizationSystem.priority_to_queue_name(priority=priority)
        ).put_nowait(item)

    def get_by_priority(self, priority: Priority) -> Optional[Item]:
        _queue_ref = self.__getattribute__(
            QueuePrioritizationSystem.priority_to_queue_name(priority=priority)
        )
        if not _queue_ref.empty():
            return _queue_ref.get()
        return None

    def _get_highest_priority_queue(self) -> Optional[QueueType]:
        for priority in self._sorted_priorities:
            _queue_ref = self.__getattribute__(
                QueuePrioritizationSystem.priority_to_queue_name(priority=priority)
            )
            if not _queue_ref.empty():
                print(f"using {priority} priority queue")
                return _queue_ref

        print(f"no priority queue has data")
        return None

    def get(self) -> Optional[Item]:
        return self._get_highest_priority_queue().get()


if __name__ == "__main__":
    qps = QueuePrioritizationSystem(
        priorities=[Priority.High, Priority.Low], queue_type=QueueType.queue
    )

    for i in range(10):
        qps.put_by_priority(
            item=Item(f"something not-important {i}"), priority=Priority.Low
        )

    print(qps.get_by_priority(priority=Priority.Low.Low))

    for i in range(20):
        qps.put_by_priority(
            item=Item(f"something super-important {i}"), priority=Priority.High
        )

    print(qps.get_by_priority(priority=Priority.High.High))

    print(qps.get())
    print(qps.get())
    print(qps.get())

    print(qps.get_by_priority(priority=Priority.Low.Low))
