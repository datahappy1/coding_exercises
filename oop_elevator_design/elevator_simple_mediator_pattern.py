from enum import Enum, auto
from typing import Optional
from uuid import uuid4

MIN_FLOOR_NUMBER = 1
MAX_FLOOR_NUMBER = 5


class Direction(Enum):
    UP = auto()
    DOWN = auto()


class Location(Enum):
    HALL = auto()
    CABIN = auto()


class RequestStatus(Enum):
    SUBMITTED = auto()
    PROGRESS = auto()
    COMPLETED = auto()


class Request:
    def __init__(
        self,
        request_location: Location,
        requested_to_floor: int,
        requested_from_floor: int,
    ):
        self.request_id = str(uuid4())
        self.request_location = request_location
        self.requested_to_floor, self.requested_from_floor = \
            Request._get_validated_request_floors(
                requested_to_floor, requested_from_floor
            )
        self.requested_direction = Request._eval_direction(
            requested_from_floor, requested_to_floor
        )
        self.request_status = None

    @staticmethod
    def _get_validated_request_floors(
        requested_to_floor: int, requested_from_floor: int
    ) -> (int, int):
        if requested_to_floor > MAX_FLOOR_NUMBER:
            raise ValueError(f"invalid requested_to_floor value {requested_to_floor}")
        if requested_from_floor < MIN_FLOOR_NUMBER:
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


class Hall:
    def __init__(self, mediator, floor: int):
        self._mediator = mediator
        self.floor: int = floor
        self.location_type: Location = Location.HALL

    def create_hall_request(self, requested_from_floor: int) -> Request:
        try:
            return Request(
                request_location=Location.HALL,
                requested_to_floor=requested_from_floor,
                requested_from_floor=self._mediator.cabin.current_floor,
            )
        except ValueError as val_err:
            raise val_err

    def print_hall_request_state(self, hall_name: str, request: Request):
        print(
            f"ID {request.request_id}, "
            f"Location type {self._mediator.halls[hall_name].location_type}, "
            f"Request location {request.request_location}, "
            f"Status{request.request_status}, "
            f"Requested direction {request.requested_direction}, "
            f"Requested from floor {request.requested_from_floor}, "
            f"Hall floor {self._mediator.halls[hall_name].floor}"
        )

    def process_hall_request(self, hall_name: str, request: Request) -> None:
        request.update_request_status(RequestStatus.SUBMITTED)

        if self._mediator.halls[hall_name].floor == self._mediator.cabin.current_floor:
            print("no movement needed")

        while (
            self._mediator.halls[hall_name].floor != self._mediator.cabin.current_floor
        ):
            request.update_request_status(RequestStatus.PROGRESS)

            self.print_hall_request_state(hall_name=hall_name, request=request)
            self._mediator.cabin.process_movement_in_direction(request=request)
            self._mediator.cabin.print_cabin_request_state(request=request)

        request.update_request_status(RequestStatus.COMPLETED)


class Cabin:
    def __init__(self, mediator):
        self._mediator = mediator
        self.current_floor: int = MIN_FLOOR_NUMBER
        self.location_type: Location = Location.CABIN

    def _move_cabin_one_floor(self, direction: Direction):
        if direction == Direction.UP:
            self.current_floor += 1
        elif direction == Direction.DOWN:
            self.current_floor -= 1

    def process_movement_in_direction(self, request: Request):
        self._move_cabin_one_floor(direction=request.requested_direction)

    def create_cabin_request(self, requested_to_floor: int) -> Request:
        try:
            return Request(
                request_location=Location.CABIN,
                requested_to_floor=requested_to_floor,
                requested_from_floor=self._mediator.cabin.current_floor,
            )
        except ValueError as val_err:
            raise val_err

    def print_cabin_request_state(self, request: Request):
        print(
            f"ID {request.request_id}, "
            f"Location type {self._mediator.cabin.location_type}, "
            f"Request location {request.request_location}, "
            f"Status {request.request_status}, "
            f"Requested direction {request.requested_direction}, "
            f"Requested from floor {request.requested_from_floor}, "
            f"Requested to floor {request.requested_to_floor}, "
            f"Current floor {self._mediator.cabin.current_floor}"
        )

    def process_cabin_request(self, request: Request) -> None:
        request.update_request_status(RequestStatus.SUBMITTED)

        while self._mediator.cabin.current_floor != request.requested_to_floor:
            request.update_request_status(RequestStatus.PROGRESS)

            self._mediator.cabin.process_movement_in_direction(request=request)
            self.print_cabin_request_state(request=request)

        request.update_request_status(RequestStatus.COMPLETED)


class Mediator:
    def __init__(self):
        self.cabin = Cabin(self)
        self.halls = {
            transform_floor_number_to_hall_name(floor_number): Hall(self, floor_number)
            for floor_number in range(MIN_FLOOR_NUMBER, MAX_FLOOR_NUMBER + 1)
        }


def transform_floor_number_to_hall_name(floor: int) -> str:
    return f"hall{floor}"


def push_hall_button(mediator: Mediator, requested_from_floor: int):
    hall_name = transform_floor_number_to_hall_name(requested_from_floor)

    request = mediator.halls[hall_name].create_hall_request(
        requested_from_floor=requested_from_floor
    )

    mediator.halls[hall_name].process_hall_request(hall_name=hall_name, request=request)


def push_cabin_button(mediator: Mediator, requested_to_floor: int):
    request = mediator.cabin.create_cabin_request(requested_to_floor=requested_to_floor)

    mediator.cabin.process_cabin_request(request=request)


def main():
    mediator = Mediator()

    push_hall_button(mediator=mediator, requested_from_floor=1)

    push_hall_button(mediator=mediator, requested_from_floor=3)

    push_cabin_button(mediator=mediator, requested_to_floor=2)

    push_hall_button(mediator=mediator, requested_from_floor=2)

    push_cabin_button(mediator=mediator, requested_to_floor=1)

    push_cabin_button(mediator=mediator, requested_to_floor=3)

    push_cabin_button(mediator=mediator, requested_to_floor=5)


if __name__ == "__main__":
    main()
