from rx import from_iterable

obs = from_iterable(range(4))
obs.subscribe(print)
obs.subscribe(on_next=lambda x: print("Next item: ", x), on_completed=lambda: print("No more data"))

