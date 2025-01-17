from concurrent.futures import Future
import threading


def network_request_async(number, _time):
    future = Future()
    result = {"success": True, "result": number**2}

    timer = threading.Timer(_time, lambda: future.set_result(result))
    timer.start()
    return future

count = 0
def fetch_square(number):
    global count
    fut = network_request_async(number, 3-count)
    count += 1
    def on_done(future):
        response = future.result()
        if response["success"]:
            print("Result is: {}".format(response["result"]))
    fut.add_done_callback(on_done)


fetch_square(2)
fetch_square(3)
fetch_square(4)