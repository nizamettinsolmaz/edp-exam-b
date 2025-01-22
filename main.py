import uuid
from collections import deque
import time

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
                "order_id": str(uuid.uuid4())
            })
            self.events.append(event)
            print(f"Order submitted for {customer.name} - Product: {product}")
        else:
            event = OrderRejectedEvent({
                "customer": customer.name,
                "product": product
            })
            self.events.append(event)
            print(f"Order rejected for {customer.name} - Product: {product} is out of stock")

    def process_events(self):
        while self.events:
            event = self.events.popleft()
            print(f"Event: {event.event_type}, Payload: {event.payload}")

class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, store, product):
        print(f"{self.name} is ordering {product} from {store.name}")
        store.process_order(self, product)

def event_loop(store):
    while True:
        if store.events:
            store.process_events()
        else:
            print("No events to process, waiting...")
        time.sleep(1)

if __name__ == "__main__":
    store = Store("TechStore")
    customer1 = Customer("John")
    customer2 = Customer("Jane")
    
    customer1.order(store, "computer")
    customer2.order(store, "computer")
    customer2.order(store, "computer")

    event_loop(store)