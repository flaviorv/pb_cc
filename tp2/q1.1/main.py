import seq_req, async_req, chart
import time


print("ASYNCHRONOUS HTTP REQUESTS")
async_req.call_requests(2)
time.sleep(10)
async_req.call_requests(4)
time.sleep(10)
async_req.call_requests(8)
time.sleep(10)
async_req.call_requests(16)
time.sleep(10)
async_req.call_requests(32)

print("SEQUENTIAL HTTP REQUESTS")
start = time.time()
seq_req.sequential_drink_requests()
end = time.time()
total_time = round((end-start), 2)
print("Sequential: {} seconds".format(total_time))
time_data = {"threads": None, "seconds":total_time}
seq_req.save_time(time_data)
print()

chart.spawn_chart()


