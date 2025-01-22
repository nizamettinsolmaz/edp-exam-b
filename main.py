from store import Store
from customer import Customer
from event_loop import event_loop

if __name__ == "__main__":
    store = Store("TechStore")
    customer1 = Customer("John")
    customer2 = Customer("Jane")
    
    customer1.order(store, "computer")
    customer2.order(store, "computer")
    customer2.order(store, "computer")

    event_loop(store)