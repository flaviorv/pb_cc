from  concurrent.futures import Future

fut = Future()
print(fut)

fut.set_result("Hello_World")
print(fut)
print(fut.result())

#--------------------------

fut2 = Future()
fut2.add_done_callback(lambda future: print(future.result(), flush=True))
fut2.set_result("Hello_World_Again")
