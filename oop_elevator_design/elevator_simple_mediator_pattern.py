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
        request_type: RequestType,
        requested_to_floor: int,
        requested_from_floor: int,
    ):
        self.request_id = str(uuid4())
        self.request_type = request_type
        (
            self.requested_to_floor,
            self.requested_from_floor,
        ) = Request._get_validated_request_floors(
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


class Hall:
    def __init__(self, mediator, floor: int):
        self._mediator = mediator
        self.floor: int = floor
        self.location_type: Location = Location.HALL

    def create_hall_request(self, requested_from_floor: int) -> Request:
        try:
            return Request(
                request_type=RequestType.HALL,
                requested_to_floor=requested_from_floor,
                requested_from_floor=self._mediator.cabin.current_floor,
            )
        except ValueError as val_err:
            raise val_err

    def print_hall_request_state(self, hall, request: Request):
        print(
            f"ID {request.request_id}, "
            f"Location type {hall.location_type}, "
            f"Request type {request.request_type}, "
            f"Status{request.request_status}, "
            f"Requested direction {request.requested_direction}, "
            f"Requested from floor {request.requested_from_floor}, "
            f"Hall floor {hall.floor}"
        )

    def process_hall1_request(self, request: Request) -> None:
        request.update_request_status(RequestStatus.SUBMITTED)

        if self._mediator.hall1.floor == self._mediator.cabin.current_floor:
            print("no movement needed")

        while self._mediator.hall1.floor != self._mediator.cabin.current_floor:
            request.update_request_status(RequestStatus.PROGRESS)

            self.print_hall_request_state(hall=self._mediator.hall1, request=request)
            self._mediator.cabin.process_movement_in_direction(request=request)
            self._mediator.cabin.print_cabin_request_state(request=request)

        request.update_request_status(RequestStatus.COMPLETED)

    def process_hall2_request(self, request: Request) -> None:
        request.update_request_status(RequestStatus.SUBMITTED)

        if self._mediator.hall2.floor == self._mediator.cabin.current_floor:
            print("no movement needed")

        while self._mediator.hall2.floor != self._mediator.cabin.current_floor:
            request.update_request_status(RequestStatus.PROGRESS)

            self.print_hall_request_state(hall=self._mediator.hall2, request=request)
            self._mediator.cabin.process_movement_in_direction(request=request)
            self._mediator.cabin.print_cabin_request_state(request=request)

        request.update_request_status(RequestStatus.COMPLETED)

    def process_hall3_request(self, request: Request) -> None:
        request.update_request_status(RequestStatus.SUBMITTED)

        if self._mediator.hall3.floor == self._mediator.cabin.current_floor:
            print("no movement needed")

        while self._mediator.hall3.floor != self._mediator.cabin.current_floor:
            request.update_request_status(RequestStatus.PROGRESS)

            self.print_hall_request_state(hall=self._mediator.hall3, request=request)
            self._mediator.cabin.process_movement_in_direction(request=request)
            self._mediator.cabin.print_cabin_request_state(request=request)

        request.update_request_status(RequestStatus.COMPLETED)


class Cabin:
    def __init__(self, mediator):
        self._mediator = mediator
        self.current_floor: int = MIN_FLOOR
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
                request_type=RequestType.CABIN,
                requested_to_floor=requested_to_floor,
                requested_from_floor=self._mediator.cabin.current_floor,
            )
        except ValueError as val_err:
            raise val_err

    def print_cabin_request_state(self, request: Request):
        print(
            f"ID {request.request_id}, "
            f"Location type {self._mediator.cabin.location_type}, "
            f"Request type {request.request_type}, "
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
        self.hall1 = Hall(self, 1)
        self.hall2 = Hall(self, 2)
        self.hall3 = Hall(self, 3)


def push_hall_button(mediator: Mediator, requested_from_floor: int):
    if requested_from_floor == 1:
        request = mediator.hall1.create_hall_request(
            requested_from_floor=requested_from_floor
        )
        mediator.hall1.process_hall1_request(request=request)
    if requested_from_floor == 2:
        request = mediator.hall2.create_hall_request(
            requested_from_floor=requested_from_floor
        )
        mediator.hall2.process_hall2_request(request=request)
    if requested_from_floor == 3:
        request = mediator.hall3.create_hall_request(
            requested_from_floor=requested_from_floor
        )
        mediator.hall3.process_hall3_request(request=request)


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


if __name__ == "__main__":
    main()
