from rx.operators import take, map, group_by, merge_all
from rx import from_iterable, interval

print("Take operator processes only the number passed as a parameter")
op = take(4)
obs = from_iterable(range(100))
op(obs).subscribe(print)

print("Map operator to square the numbers in a range of 4")
map(lambda x: x**2) (from_iterable(range(4))).subscribe(print)

print("Group by")
obs = group_by(lambda x: x%2) (from_iterable(range(7)))
obs.subscribe(lambda x: print("group key: ", x.key))
print("Even")
take(1) (obs).subscribe(lambda x: x.subscribe(print))
print("Merging all")
merge_all() (obs).subscribe(print)

import time
start = time.time()

from rx.operators import publish

start = time.time()

obs = publish()(map(lambda a: (a, time.time() - \

start))(interval(1)))

time.sleep(1)
take(4)(obs).subscribe(lambda x: print("First \
subscriber: {}".format(x)))

obs.connect() # Data production starts here

time.sleep(2)

take(4)(obs).subscribe(lambda x: print("Second \
subscriber: {}".format(x)))