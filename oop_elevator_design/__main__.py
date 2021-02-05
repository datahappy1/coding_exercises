from uuid import uuid4
from queue import Queue


class CabinState:
    def __init__(self, currentFloor):
        self.currentFloor = currentFloor


class Request:
    def __init__(self, requestId, requestStatus, currentFloor, requestType,
                 requestedFloor=None, requestedDirection=None):
        self.requestId = requestId
        self.requestStatus = requestStatus
        self.requestType = requestType
        self.requestedFloor = requestedFloor
        self.requestedDirection = requestedDirection
        self.currentFloor = currentFloor


class RequestQueue:
    def __init__(self):
        self.r_queue = Queue()

    def return_queue(self):
        return self.r_queue


class CabinController:
    @staticmethod
    def _evaluate_direction_from_params(currentFloor, requestedFloor):
        if currentFloor == requestedFloor:
            raise Exception
        if currentFloor > requestedFloor:
            return 'down'
        return 'up'

    def __init__(self, requestQueue):
        self.requestQueue = requestQueue
        self.requests = []

    def create_request_to_ride_to_floor_number(self, currentFloor, requestedFloor):
        request = Request(requestId=str(uuid4()),
                          requestStatus='submitted',
                          requestType="cabin",
                          requestedFloor=requestedFloor,
                          requestedDirection=CabinController._evaluate_direction_from_params(currentFloor,
                                                                                             requestedFloor),
                          currentFloor=currentFloor)

        self._put_request_to_queue(request)
        self.requests.append(request)
        return request.requestId

    def _put_request_to_queue(self, request):
        self.requestQueue.put(request)

    def update_request(self, request):
        for idx, item in enumerate(self.requests):
            if item.requestId == request.requestId:
                self.requests[idx] = request

    def get_request_status(self, request_id):
        return [req.requestStatus for req in self.requests if req.requestId == request_id]


class HallController:
    def __init__(self, requestQueue):
        self.requestQueue = requestQueue
        self.requests = []

    def create_request_to_ride_to_direction(self, currentFloor, direction):
        request = Request(requestId=str(uuid4()),
                          requestStatus='submitted',
                          requestType="hall",
                          requestedFloor=None,
                          requestedDirection=direction,
                          currentFloor=currentFloor)
        self._put_request_to_queue(request)
        self.requests.append(request)
        return request.requestId

    def _put_request_to_queue(self, request):
        self.requestQueue.put(request)

    def update_request(self, request):
        for idx, item in enumerate(self.requests):
            if item.requestId == request.request_id:
                self.requests[idx] = request

    def get_request_status(self, request_id):
        return [req.requestStatus for req in self.requests if req.requestId == request_id]


class CabinRequestProcessor:
    def __init__(self, requestQueue, hall_controller, cabin_controller):
        self.cabin_state = CabinState(currentFloor=0)
        self.requestQueue = requestQueue
        self.hall_controller = hall_controller
        self.cabin_controller = cabin_controller

    def move_cabin_one_floor_in_provided_direction(self, direction):
        if direction == "up":
            self.cabin_state.currentFloor += 1
        elif direction == "down":
            self.cabin_state.currentFloor -= 1

    def process_requests_from_queue(self):
        while self.requestQueue.qsize() > 0:
            _request = self.requestQueue.get()

            while self.cabin_state.currentFloor != _request.currentFloor:
                print(f"{_request.requestId} type {_request.requestType} requested "
                      f"one move {_request.requestedDirection} to get to requester direction")
                self.move_cabin_one_floor_in_provided_direction(direction=_request.requestedDirection)

            if not _request.requestedFloor:
                _request.requestStatus = "done"
                break

            while self.cabin_state.currentFloor != _request.requestedFloor:
                print(f"{_request.requestId} type {_request.requestType} requested "
                      f"one move {_request.requestedDirection} to get to requested direction")
                self.move_cabin_one_floor_in_provided_direction(direction=_request.requestedDirection)
            _request.requestStatus = "done"

            if _request.requestType == "hall":
                hall_controller.update_request(_request)
            elif _request.requestType == "cabin":
                cabin_controller.update_request(_request)


queue = RequestQueue().return_queue()
hall_controller = HallController(queue)
cabin_controller = CabinController(queue)
request_processor = CabinRequestProcessor(queue, hall_controller, cabin_controller)

request_id = hall_controller.create_request_to_ride_to_direction(currentFloor=2, direction='up')
request_processor.process_requests_from_queue()
print(hall_controller.get_request_status(request_id))

request_id = cabin_controller.create_request_to_ride_to_floor_number(currentFloor=2, requestedFloor=4)
request_processor.process_requests_from_queue()
print(cabin_controller.get_request_status(request_id))

request_id = cabin_controller.create_request_to_ride_to_floor_number(currentFloor=4, requestedFloor=3)
request_processor.process_requests_from_queue()
print(cabin_controller.get_request_status(request_id))
