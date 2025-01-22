class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, store, product):
        print(f"{self.name} is ordering {product} from {store.name}")
        store.process_order(self, product)