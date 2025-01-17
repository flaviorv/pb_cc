def range_generator(n):
    i = 0
    while i < n:
        print("Generating vaue {}".format(i))
        yield i
        i += 1
    
generator = range_generator(2)
next(generator)
next(generator)

def parrot():
    while True:
        message = yield
        print("Parrot says: {}".format(message))

generator = parrot()
generator.send(None)
generator.send("Hello")
generator.send("World")
