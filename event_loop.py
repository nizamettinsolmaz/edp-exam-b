import time

def event_loop(store):
    while True:
        if store.events:
            store.process_events()
        else:
            print("No events to process, waiting...")
        time.sleep(1)