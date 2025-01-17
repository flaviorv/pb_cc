import threading
import time

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print(f"{thread_number} is trying to access!")
    semaphore.acquire()
    print(f"{thread_number} was granted access!")
    time.sleep(10)
    print(f"{thread_number} is now realeasing!")
    semaphore.release()

for thread_number in range(1, 11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)


path = "text.txt"
text =  ""

def readFile():
    global path, text
    while True:
        with open(path, "r") as f:
            print("reading...")
            text = f.read()
        time.sleep(3)
        

def printLoop():
    for x in range(30):
        print(text, x)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printLoop)

t1.start()
t2.start()
