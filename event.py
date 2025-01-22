import uuid

class Event:
    def __init__(self, payload):
        self.payload = payload

class OrderSubmittedEvent(Event):
    def __init__(self, payload):
        super().__init__(payload)
        self.event_type = "OrderSubmitted"

class OrderRejectedEvent(Event):
    def __init__(self, payload):
        super().__init__(payload)
        self.event_type = "OrderRejected"