from uuid import uuid4
from queue import Queue


class CabinState:
    def __init__(self, current_floor):
        self.currentFloor = current_floor


class Request:
    def __init__(self, request_id, request_status, requested_from_floor, request_type,
                 requested_floor=None, requested_direction=None):
        self.requestId = request_id
        self.requestStatus = request_status
        self.requestedFromFloor = requested_from_floor
        self.requestType = request_type
        self.requestedFloor = requested_floor
        self.requestedDirection = requested_direction


class RequestEventBus:
    def __init__(self):
        self.r_queue = Queue()

    def qet_event_bus_queue(self):
        return self.r_queue


class BaseController:
    def __init__(self, request_queue):
        self.requestQueue = request_queue
        self.requests = []

    def _put_request_to_queue(self, request):
        self.requestQueue.put(request)

    def update_request(self, request):
        for idx, item in enumerate(self.requests):
            if item.requestId == request.requestId:
                self.requests[idx] = request

    def get_request_status(self, request_id):
        return [{request.requestId, request.requestStatus} for request in self.requests
                if request.requestId == request_id]

    def register_request(self, request):
        self._put_request_to_queue(request)
        self.requests.append(request)


class CabinController(BaseController):
    @staticmethod
    def _evaluate_direction_from_params(requested_from_floor, requested_floor):
        if requested_from_floor == requested_floor:
            raise Exception
        if requested_from_floor > requested_floor:
            return 'down'
        return 'up'

    def __init__(self, request_queue):
        super().__init__(request_queue)
        self.requestQueue = request_queue
        self.requests = []

    def create_request_to_ride_to_floor_number(self, requested_from_floor, requested_floor):
        request = Request(request_id=str(uuid4()),
                          request_status='submitted',
                          request_type="cabin",
                          requested_floor=requested_floor,
                          requested_direction=CabinController._evaluate_direction_from_params(requested_from_floor,
                                                                                              requested_floor),
                          requested_from_floor=requested_from_floor)

        return request


class HallController(BaseController):
    def __init__(self, requestQueue):
        super().__init__(requestQueue)
        self.requestQueue = requestQueue
        self.requests = []

    def create_request_to_ride_to_direction(self, requested_from_floor, requested_direction):
        request = Request(request_id=str(uuid4()),
                          request_status='submitted',
                          request_type="hall",
                          requested_floor=None,
                          requested_direction=requested_direction,
                          requested_from_floor=requested_from_floor)

        return request


class CabinRequestProcessor:
    def __init__(self, request_queue, hall_controller, cabin_controller):
        self.cabin_state = CabinState(current_floor=0)
        self.request_queue = request_queue
        self.hall_controller = hall_controller
        self.cabin_controller = cabin_controller

    def report_on_request(self, request):
        print(f"cabin state: {vars(self.cabin_state)}, request: {vars(request)}")

    def move_cabin_one_floor_in_provided_direction(self, direction):
        if direction == "up":
            self.cabin_state.currentFloor += 1
        elif direction == "down":
            self.cabin_state.currentFloor -= 1

    def process_requests_from_queue(self):
        while self.request_queue.qsize() > 0:
            processed_request = self.request_queue.get()

            if processed_request.requestType == "hall":
                while self.cabin_state.currentFloor != processed_request.requestedFromFloor:
                    self.move_cabin_one_floor_in_provided_direction(direction=processed_request.requestedDirection)
                    hall_controller.update_request(processed_request)
                    self.report_on_request(processed_request)
                processed_request.requestStatus = "done"
                self.report_on_request(processed_request)

            if processed_request.requestType == "cabin":
                while self.cabin_state.currentFloor != processed_request.requestedFloor:
                    self.move_cabin_one_floor_in_provided_direction(direction=processed_request.requestedDirection)
                    cabin_controller.update_request(processed_request)
                    self.report_on_request(processed_request)
                processed_request.requestStatus = "done"
                self.report_on_request(processed_request)

queue = RequestEventBus().qet_event_bus_queue()
hall_controller = HallController(queue)
cabin_controller = CabinController(queue)
request_processor = CabinRequestProcessor(queue, hall_controller, cabin_controller)

request = hall_controller.create_request_to_ride_to_direction(requested_from_floor=2, requested_direction='up')
hall_controller.register_request(request)
request_processor.process_requests_from_queue()
print(hall_controller.get_request_status(request.requestId))

request = cabin_controller.create_request_to_ride_to_floor_number(requested_from_floor=2, requested_floor=4)
cabin_controller.register_request(request)
request_processor.process_requests_from_queue()
print(cabin_controller.get_request_status(request.requestId))

request = cabin_controller.create_request_to_ride_to_floor_number(requested_from_floor=4, requested_floor=5)
cabin_controller.register_request(request)
request_processor.process_requests_from_queue()
print(cabin_controller.get_request_status(request.requestId))

request = cabin_controller.create_request_to_ride_to_floor_number(requested_from_floor=4, requested_floor=3)
cabin_controller.register_request(request)
request_processor.process_requests_from_queue()
print(cabin_controller.get_request_status(request.requestId))

request = hall_controller.create_request_to_ride_to_direction(requested_from_floor=3, requested_direction='down')
hall_controller.register_request(request)
request_processor.process_requests_from_queue()
print(hall_controller.get_request_status(request.requestId))

request = cabin_controller.create_request_to_ride_to_floor_number(requested_from_floor=3, requested_floor=0)
cabin_controller.register_request(request)
request_processor.process_requests_from_queue()
print(cabin_controller.get_request_status(request.requestId))
