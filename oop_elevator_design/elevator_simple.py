from enum import Enum, auto
from typing import Optional
from uuid import uuid4

MIN_FLOOR = 1
MAX_FLOOR = 3


class Direction(Enum):
    UP = auto()
    DOWN = auto()


class RequestType(Enum):
    HALL = auto()
    CABIN = auto()


class ControllerType(Enum):
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
        self.requested_to_floor, self.requested_from_floor = \
            Request._get_validated_request_floors(
                requested_to_floor,
                requested_from_floor
            )
        self.requested_direction = \
            Request._eval_direction(
                requested_from_floor,
                requested_to_floor
            )
        self.request_status = None

    @staticmethod
    def _get_validated_request_floors(
            requested_to_floor: int,
            requested_from_floor: int
    ) -> (int, int):
        if requested_to_floor > MAX_FLOOR:
            raise ValueError(f"invalid requested_to_floor value {requested_to_floor}")
        if requested_from_floor < MIN_FLOOR:
            raise ValueError(f"invalid request_from_floor value {requested_from_floor}")
        return requested_to_floor, requested_from_floor

    @staticmethod
    def _eval_direction(from_floor: int, to_floor: int) -> Optional[Direction]:
        if from_floor > to_floor:
            return Direction.DOWN
        if from_floor < to_floor:
            return Direction.UP

    def update_request_status(self, status: RequestStatus) -> None:
        self.request_status = status


class HallController:
    def __init__(self, floor: int):
        self.floor: int = floor
        self.controller_type: ControllerType = ControllerType.HALL

    def process_movement_in_direction(self, request: Request):
        print(f"ID {request.request_id}, "
              f"Controller type {self.controller_type}, "
              f"Request type {request.request_type}, "
              f"Status{request.request_status}, "
              f"Requested direction {request.requested_direction}, "
              f"Requested from floor {request.requested_from_floor}, "
              f"Hall floor {self.floor}")


class CabinController:
    def __init__(self):
        self.current_floor: int = MIN_FLOOR
        self.controller_type: ControllerType = ControllerType.CABIN

    def _add_one_floor(self):
        if self.current_floor < MAX_FLOOR:
            self.current_floor += 1

    def _subtract_one_floor(self):
        if self.current_floor > MIN_FLOOR:
            self.current_floor -= 1

    def _move_cabin_one_floor(self, direction: Direction):
        if direction == Direction.UP:
            self._add_one_floor()
        elif direction == Direction.DOWN:
            self._subtract_one_floor()

    def process_movement_in_direction(self, request: Request):
        self._move_cabin_one_floor(direction=request.requested_direction)

        print(f"ID {request.request_id}, "
              f"Controller type {self.controller_type}, "
              f"Request type {request.request_type}, "
              f"Status {request.request_status}, "
              f"Requested direction {request.requested_direction}, "
              f"Requested from floor {request.requested_from_floor}, "
              f"Requested to floor {request.requested_to_floor}, "
              f"Current floor {self.current_floor}")


class RequestProcessor:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def create_hall_request(self, requested_from_floor: int):
        try:
            return Request(
                request_type=RequestType.HALL,
                requested_to_floor=requested_from_floor,
                requested_from_floor=self.cabin_controller.current_floor
            )
        except ValueError as val_err:
            raise val_err

    def create_cabin_request(self, requested_to_floor):
        try:
            return Request(
                request_type=RequestType.CABIN,
                requested_to_floor=requested_to_floor,
                requested_from_floor=self.cabin_controller.current_floor
            )
        except ValueError as val_err:
            raise val_err

    def process_hall_request(self, hall, request: Request):
        request.update_request_status(RequestStatus.SUBMITTED)

        hall_controller = getattr(self, hall)

        if hall_controller.floor == self.cabin_controller.current_floor:
            print("no movement needed")

        while hall_controller.floor != self.cabin_controller.current_floor:
            request.update_request_status(RequestStatus.PROGRESS)

            hall_controller.process_movement_in_direction(request=request)
            self.cabin_controller.process_movement_in_direction(request=request)

        request.update_request_status(RequestStatus.COMPLETED)

    def process_cabin_request(self, request: Request):
        request.update_request_status(RequestStatus.SUBMITTED)

        while self.cabin_controller.current_floor != request.requested_to_floor:
            request.update_request_status(RequestStatus.PROGRESS)
            self.cabin_controller.process_movement_in_direction(request=request)

        request.update_request_status(RequestStatus.COMPLETED)


request_processor = RequestProcessor(
    **dict(floor1_hall_controller=HallController(floor=1),
           floor2_hall_controller=HallController(floor=2),
           floor3_hall_controller=HallController(floor=3),
           cabin_controller=CabinController())
)


def push_hall_button(requested_from_floor):
    request = request_processor.create_hall_request(
        requested_from_floor=requested_from_floor
    )

    hall_id = f"floor{requested_from_floor}_hall_controller"

    request_processor.process_hall_request(hall_id, request)


def push_cabin_button(requested_to_floor):
    request = request_processor.create_cabin_request(
        requested_to_floor=requested_to_floor
    )

    request_processor.process_cabin_request(request)


push_hall_button(requested_from_floor=1)

push_hall_button(requested_from_floor=3)

push_cabin_button(requested_to_floor=2)

push_hall_button(requested_from_floor=2)

push_cabin_button(requested_to_floor=1)

push_cabin_button(requested_to_floor=3)
