from uuid import uuid4


class Cabin:
    def __init__(self):
        self.currentFloor = 0

    def add_one_floor(self):
        self.currentFloor += 1

    def subtract_one_floor(self):
        self.currentFloor -= 1

    def get_current_floor(self):
        return self.currentFloor


class Request:
    def __init__(self, request_id, request_status, requested_from_floor, request_type,
                 requested_to_floor=None, requested_direction=None):
        self.requestId = request_id
        self.requestStatus = request_status
        self.requestedFromFloor = requested_from_floor
        self.requestType = request_type
        self.requestedToFloor = requested_to_floor
        self.requestedDirection = requested_direction


class HallRequest(Request):
    def __init__(self, request_id, request_status, requested_from_floor, request_type):
        super().__init__(request_id, request_status, requested_from_floor, request_type)


class CabinRequest(Request):
    def __init__(self, request_id, request_status, requested_from_floor, request_type,
                 requested_to_floor, requested_direction):
        super().__init__(request_id, request_status, requested_from_floor, request_type,
                         requested_to_floor, requested_direction)


class BaseController:
    def __init__(self):
        self.requests = []

    def update_request(self, request):
        for idx, item in enumerate(self.requests):
            if item.requestId == request.requestId:
                self.requests[idx] = request

    def delete_request(self, request_id):
        for idx, item in enumerate(self.requests):
            if item.requestId == request_id:
                self.requests.pop(idx)

    def get_request_status(self, request_id):
        return [request.requestStatus for request in self.requests
                if request.requestId == request_id]

    def register_request(self, request):
        self.requests.append(request)


class CabinController(BaseController):
    @staticmethod
    def _eval_direction(requested_from_floor, requested_to_floor):
        if requested_from_floor > requested_to_floor:
            return 'down'
        return 'up'

    def __init__(self, cabin_state):
        super().__init__()
        self.cabin_state = cabin_state
        self.requests = []

    def create_request_for_ride(self, floor):
        requested_from_floor = self.cabin_state.get_current_floor()

        request = CabinRequest(request_id=str(uuid4()),
                               request_status='submitted',
                               request_type="cabin",
                               requested_to_floor=floor,
                               requested_direction=CabinController._eval_direction(requested_from_floor,
                                                                                   floor),
                               requested_from_floor=requested_from_floor)

        return request


class HallController(BaseController):
    def __init__(self):
        super().__init__()
        self.requests = []

    def create_request_for_ride(self, floor):
        request = HallRequest(request_id=str(uuid4()),
                              request_status='submitted',
                              request_type="hall",
                              requested_from_floor=floor)

        return request


class RequestProcessor:
    def __init__(self, hall_controller, cabin_controller):
        self.cabin_state = cabin_controller.cabin_state
        self.hall_controller = hall_controller
        self.cabin_controller = cabin_controller

    def print_request_status(self, request):
        print(f"cabin state: {vars(self.cabin_state)}, request: {vars(request)}")

    def move_cabin_one_floor_in_provided_direction(self, direction):
        if direction == "up":
            self.cabin_state.add_one_floor()
        elif direction == "down":
            self.cabin_state.subtract_one_floor()

    def process_movement_in_direction(self, controller, request, direction):
        self.move_cabin_one_floor_in_provided_direction(direction=direction)
        request.requestStatus = "in progress"
        controller.update_request(request)
        self.print_request_status(request)

    def process_hall_request(self, request):
        if self.cabin_state.currentFloor > request.requestedFromFloor:
            while self.cabin_state.currentFloor != request.requestedFromFloor:
                self.process_movement_in_direction(controller=self.hall_controller,
                                                   request=request,
                                                   direction="down")

        elif self.cabin_state.currentFloor < request.requestedFromFloor:
            while self.cabin_state.currentFloor != request.requestedFromFloor:
                self.process_movement_in_direction(controller=self.hall_controller,
                                                   request=request,
                                                   direction="up")

        elif self.cabin_state.currentFloor == request.requestedFromFloor:
            pass

        request.requestStatus = "done"
        self.print_request_status(request)

    def process_cabin_request(self, request):
        while self.cabin_state.currentFloor != request.requestedToFloor:
            self.process_movement_in_direction(controller=self.cabin_controller,
                                               request=request,
                                               direction=request.requestedDirection)

        request.requestStatus = "done"
        self.print_request_status(request)

    def process_request(self, request):
        processed_request = request
        self.print_request_status(processed_request)

        if processed_request.requestType == "hall":
            self.process_hall_request(processed_request)
        if processed_request.requestType == "cabin":
            self.process_cabin_request(processed_request)

hall_controller = HallController()
cabin_controller = CabinController(cabin_state=Cabin())
request_processor = RequestProcessor(hall_controller, cabin_controller)


def _elevator_button_push_button(controller, floor):
    request = controller.create_request_for_ride(floor=floor)
    controller.register_request(request)
    request_processor.process_request(request)
    return request.requestId


def _elevator_button_show_status(controller, request_id):
    request_status = controller.get_request_status(request_id)
    print(request_status)
    if request_status == "done":
        controller.delete_request(request_id)
    return


def elevator_hall_button_push_button(requested_from_floor):
    return _elevator_button_push_button(hall_controller, floor=requested_from_floor)


def elevator_hall_button_show_status(request_id):
    return _elevator_button_show_status(hall_controller, request_id)


def elevator_cabin_button_push_button(requested_to_floor):
    return _elevator_button_push_button(cabin_controller, floor=requested_to_floor)


def elevator_cabin_button_show_status(request_id):
    return _elevator_button_show_status(cabin_controller, request_id)


request_id = elevator_hall_button_push_button(requested_from_floor=2)
elevator_hall_button_show_status(request_id)

request_id = elevator_cabin_button_push_button(requested_to_floor=4)
elevator_cabin_button_show_status(request_id)

request_id = elevator_hall_button_push_button(requested_from_floor=0)
elevator_hall_button_show_status(request_id)

request_id = elevator_cabin_button_push_button(requested_to_floor=5)
elevator_cabin_button_show_status(request_id)

request_id = elevator_cabin_button_push_button(requested_to_floor=3)
elevator_cabin_button_show_status(request_id)

request_id = elevator_hall_button_push_button(requested_from_floor=3)
elevator_hall_button_show_status(request_id)

request_id = elevator_cabin_button_push_button(requested_to_floor=0)
elevator_cabin_button_show_status(request_id)
