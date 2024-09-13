import threading
import time

def fun():
    while True:
        print("Running...")
        time.sleep(1)

# Creating a daemon thread
thread = threading.Thread(target=fun, daemon=True)
thread.start()

# Main thread sleeps for 3 seconds
time.sleep(3)
print("Main thread exiting")
