import time
import threading

def network_request(number):
    time.sleep(1.0)
    return {"success": True, "result": number**2}

def network_request_async(number, on_done, _time):
    def timer_done():
        on_done({"success": True, "result": number **2})
    timer = threading.Timer(_time, timer_done)
    timer.start()

count = 0
def fetch_square(number, _async=False):
    if _async:
        global count
        count += 1
        def on_done(result):
            print(result)
        response = network_request_async(number, on_done, 3-count)
    else:
        response = network_request(number)
        if response["success"]:
            print("Result is: {}".format(response["result"]))


fetch_square(2)
fetch_square(3)
fetch_square(4)

fetch_square(2, True)
fetch_square(3, True)
fetch_square(4, True)