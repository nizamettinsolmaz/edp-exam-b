from collections import deque
from event import OrderSubmittedEvent, OrderRejectedEvent

class Store:
    def __init__(self, name):
        self.name = name
        self.inventory = {"computer": 10}
        self.events = deque()

    def process_order(self, customer, product):
        if self.inventory.get(product, 0) > 0:
            self.inventory[product] -= 1
            event = OrderSubmittedEvent({
                "customer": customer.name,
                "product": product,
                "order_id": str(uuid.uuid4()) })
            self.events.append(event)
            print(f"Order submitted for {customer.name} - Product: {product}")
        else:
            event = OrderRejectedEvent({
                "customer": customer.name,
                "product": product })
            self.events.append(event)
            print(f"Order rejected for {customer.name} - Product: {product} is out of stock")

    def process_events(self):
        while self.events:
            event = self.events.popleft()
            print(f"Event: {event.event_type}, Payload: {event.payload}")