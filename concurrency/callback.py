import time
import threading

def wait_and_print(msg):
    time.sleep(2.0)
    print(msg)

def wait_and_print_async(msg):
    def callback():
        print(msg)
    timer = threading.Timer(2.0, callback)
    timer.start()

wait_and_print("first")
wait_and_print("second")
wait_and_print("third")
print("After waiting_and_print")

wait_and_print_async("first_async")
wait_and_print_async("second_async")
wait_and_print_async("third_async")
print("After waiting_and_print_aync")