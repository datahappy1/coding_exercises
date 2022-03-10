from enum import Enum, auto
from typing import Optional, Union
from uuid import uuid4


class Direction(Enum):
    UP = auto()
    DOWN = auto()


class RequestType(Enum):
    HALL = auto()
    CABIN = auto()


class RequestStatus(Enum):
    SUBMITTED = auto()
    PROGRESS = auto()
    COMPLETED = auto()


class Request:
    def __init__(
            self,
            request_type: RequestType,
            requested_to_floor: int,
            requested_from_floor: int
    ):
        self.request_id = str(uuid4())
        self.request_type = request_type
        self.requested_direction = Request.eval_direction(
            requested_from_floor, requested_to_floor
        )
        self.requested_to_floor = requested_to_floor
        self.requested_from_floor = requested_from_floor
        self.request_status = RequestStatus.SUBMITTED

    def update_request_status(self, status: RequestStatus) -> None:
        self.request_status = status

    @staticmethod
    def eval_direction(from_floor: int, to_floor: int) -> Optional[Direction]:
        if from_floor > to_floor:
            return Direction.DOWN
        if from_floor < to_floor:
            return Direction.UP


class HallController:
    def __init__(self, floor: int):
        self.floor: int = floor

    def process_movement_in_direction(self, request: Request):
        request.update_request_status(RequestStatus.PROGRESS)

        print(f"ID {request.request_id}, "
              f"Type {request.request_type}, "
              f"Status{request.request_status}, "
              f"Requested direction {request.requested_direction}, "
              f"Requested from floor {request.requested_from_floor}, "
              f"Hall floor {self.floor}")


class CabinController:
    def __init__(self):
        self.currentFloor: int = 1

    def _add_one_floor(self):
        self.currentFloor += 1

    def _subtract_one_floor(self):
        self.currentFloor -= 1

    def _move_cabin_one_floor(self, direction: Direction):
        if direction == Direction.UP:
            self._add_one_floor()
        elif direction == Direction.DOWN:
            self._subtract_one_floor()
        else:
            return

    def process_movement_in_direction(self, request: Request):
        self._move_cabin_one_floor(direction=request.requested_direction)
        request.update_request_status(RequestStatus.PROGRESS)

        print(f"ID {request.request_id}, "
              f"Type {request.request_type}, "
              f"Status {request.request_status}, "
              f"Requested direction {request.requested_direction}, "
              f"Requested from floor {request.requested_from_floor}, "
              f"Requested to floor {request.requested_to_floor}, "
              f"Current floor {self.currentFloor}")


class RequestProcessor:
    def __init__(self, **kwargs):
        self.requests: [Request] = []
        for key, value in kwargs.items():
            setattr(self, key, value)

    def process_hall_request(self, hall, request: Request):
        self.requests.append(request)

        hall_controller = getattr(self, hall)

        if hall_controller.floor == cabin_controller.currentFloor:
            print("no movement needed")

        while hall_controller.floor != cabin_controller.currentFloor:
            hall_controller.process_movement_in_direction(request=request)
            cabin_controller.process_movement_in_direction(request=request)

        request.update_request_status(RequestStatus.COMPLETED)

    def process_cabin_request(self, request: Request):
        self.requests.append(request)

        while cabin_controller.currentFloor != request.requested_to_floor:
            cabin_controller.process_movement_in_direction(request=request)

        request.update_request_status(RequestStatus.COMPLETED)


MIN_FLOOR = 1
MAX_FLOOR = 3

floor1_hall_controller = HallController(floor=1)
floor2_hall_controller = HallController(floor=2)
floor3_hall_controller = HallController(floor=3)
cabin_controller = CabinController()

request_processor = RequestProcessor(
    **dict(floor1_hall_controller=floor1_hall_controller,
           floor2_hall_controller=floor2_hall_controller,
           floor3_hall_controller=floor3_hall_controller,
           cabin_controller=cabin_controller)
)


def push_hall_button(requested_to_floor, requested_from_floor):
    request = Request(
        request_type=RequestType.HALL,
        requested_to_floor=requested_to_floor,
        requested_from_floor=requested_from_floor
    )

    hall_id = f"floor{requested_from_floor}_hall_controller"

    request_processor.process_hall_request(hall_id, request)


def push_cabin_button(requested_to_floor, requested_from_floor):
    request = Request(
        request_type=RequestType.CABIN,
        requested_to_floor=requested_to_floor,
        requested_from_floor=requested_from_floor
    )
    request_processor.process_cabin_request(request)


push_hall_button(requested_from_floor=1, requested_to_floor=MAX_FLOOR)

push_hall_button(requested_from_floor=3, requested_to_floor=MIN_FLOOR)

push_cabin_button(requested_from_floor=3, requested_to_floor=2)

push_hall_button(requested_from_floor=3, requested_to_floor=MAX_FLOOR)

# push_cabin_button(requested_from_floor=2, requested_to_floor=1)
