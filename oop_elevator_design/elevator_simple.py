from uuid import uuid4
from enum import Enum, auto
from typing import Optional


class Direction(Enum):
    UP = auto()
    DOWN = auto()


def eval_direction(from_floor: int, to_floor: int) -> Optional[Direction]:
    if from_floor == to_floor:
        return
    if from_floor < to_floor:
        return Direction.UP
    return Direction.DOWN


class RequestType(Enum):
    HALL = auto()
    CABIN = auto()


class RequestStatus(Enum):
    SUBMITTED = auto()
    PROGRESS = auto()
    COMPLETED = auto()


class Hall:
    def __init__(self, floor: int):
        self.floor: int = floor


class Cabin:
    def __init__(self):
        self.currentFloor: int = 0

    def add_one_floor(self):
        self.currentFloor += 1

    def subtract_one_floor(self):
        self.currentFloor -= 1


class Request:
    def __init__(self,
                 request_type: RequestType,
                 requested_direction: Direction,
                 requested_from_floor: int,
                 requested_to_floor: int = None):
        self.requestId: str = str(uuid4())
        self.requestType: RequestType = request_type
        self.requestedDirection: Direction = requested_direction
        self.requestedToFloor: int = requested_to_floor
        self.requestedFromFloor: int = requested_from_floor
        self.requestStatus: RequestStatus = RequestStatus.SUBMITTED

    @property
    def request_status(self) -> RequestStatus:
        return self.requestStatus

    def update_request_status(self, status: RequestStatus) -> None:
        self.requestStatus = status


class HallRequest(Request):
    def __init__(self, request_type: RequestType, direction: Direction, requested_from_floor: int):
        super().__init__(request_type=request_type,
                         requested_direction=direction,
                         requested_from_floor=requested_from_floor)


class CabinRequest(Request):
    def __init__(self, request_type: RequestType, requested_to_floor: int, requested_from_floor: int):
        super().__init__(request_type=request_type,
                         requested_direction=Direction.eval_direction(requested_from_floor, requested_to_floor),
                         requested_to_floor=requested_to_floor,
                         requested_from_floor=requested_from_floor)


class HallController:
    def __init__(self, hall: Hall):
        self.hall: Hall = hall


class CabinController:
    def __init__(self, cabin: Cabin):
        self.cabin: Cabin = cabin

    def move_cabin_one_floor(self, direction: Direction):
        if direction == Direction.UP:
            self.cabin.add_one_floor()
        elif direction == Direction.DOWN:
            self.cabin.subtract_one_floor()

    def process_movement_in_direction(self, request: Request, direction: Direction):
        self.move_cabin_one_floor(direction=direction)
        request.update_request_status(RequestStatus.PROGRESS)


class RequestProcessor:
    def __init__(self, hall_controller, cabin_controller):
        self.requests: [Request] = []
        self.hall_controller: hall_controller() = hall_controller
        self.cabin_controller: cabin_controller() = cabin_controller

    def process_hall_request(self, request: Request):
        if self.cabin_controller.cabin.currentFloor > request.requestedFromFloor:
            while self.cabin_controller.cabin.currentFloor != request.requestedFromFloor:
                self.cabin_controller.process_movement_in_direction(controller=self.hall_controller,
                                                                    request=request,
                                                                    direction=Direction.DOWN)

        elif self.cabin_controller.cabin.currentFloor < request.requestedFromFloor:
            while self.cabin_controller.cabin.currentFloor != request.requestedFromFloor:
                self.cabin_controller.process_movement_in_direction(controller=self.hall_controller,
                                                                    request=request,
                                                                    direction=Direction.UP)

        elif self.cabin_controller.cabin.currentFloor == request.requestedFromFloor:
            pass

        request.update_request_status(RequestStatus.COMPLETED)

    def process_cabin_request(self, request: Request):
        while self.cabin_controller.cabin.currentFloor != request.requestedToFloor:
            self.cabin_controller.process_movement_in_direction(controller=self.cabin_controller,
                                                                request=request,
                                                                direction=request.requestedDirection)

        request.update_request_status(RequestStatus.COMPLETED)

    def process_request(self, request: Request):
        processed_request = request

        if processed_request.requestType == RequestType.HALL:
            self.process_hall_request(processed_request)
        if processed_request.requestType == RequestType.CABIN:
            self.process_cabin_request(processed_request)


floor1_hall_controller = HallController(hall=Hall(floor=1))
floor2_hall_controller = HallController(hall=Hall(floor=2))
floor3_hall_controller = HallController(hall=Hall(floor=3))
cabin_controller1 = CabinController(cabin=Cabin())

# def _hall_button_push_button(controller: HallController, requested_from_floor, direction):
#     request = controller.create_request_for_ride(requested_from_floor=requested_from_floor, direction=direction)
#     controller.register_request(request)
#     request_processor.process_request(request)
#     return request.requestId
#
#
# def _cabin_button_push_button(controller: CabinController, floor):
#     request = controller.create_request_for_ride(target_floor=floor)
#     controller.register_request(request)
#     request_processor.process_request(request)
#     return request.requestId
#
#
# def elevator_button_show_status(controller, request_id):
#     print(controller.get_request_status(request_id))
#
#
# def elevator_hall_button_push_button(requested_from_floor, direction):
#     return _hall_button_push_button(hall_controller, requested_from_floor=requested_from_floor, direction=direction)
#
#
# def elevator_cabin_button_push_button(requested_to_floor):
#     return _cabin_button_push_button(cabin_controller, floor=requested_to_floor)
#
#
# request_id = elevator_hall_button_push_button(requested_from_floor=0, direction=Direction.UP)
# elevator_button_show_status(hall_controller, request_id)
#
# request_id = elevator_cabin_button_push_button(requested_to_floor=4)
# elevator_button_show_status(cabin_controller, request_id)
#
# request_id = elevator_hall_button_push_button(requested_from_floor=2, direction=Direction.DOWN)
# elevator_button_show_status(hall_controller, request_id)
#
# request_id = elevator_cabin_button_push_button(requested_to_floor=5)
# elevator_button_show_status(cabin_controller, request_id)
#
# request_id = elevator_cabin_button_push_button(requested_to_floor=3)
# elevator_button_show_status(cabin_controller, request_id)
#
# request_id = elevator_hall_button_push_button(requested_from_floor=3, direction=Direction.UP)
# elevator_button_show_status(hall_controller, request_id)
#
# request_id = elevator_cabin_button_push_button(requested_to_floor=0)
# elevator_button_show_status(cabin_controller, request_id)
