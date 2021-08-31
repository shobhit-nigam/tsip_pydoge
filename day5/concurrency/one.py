import threading
import time

def taskA():
    for i in range(3, 0, -1):
        print(i, "seconds left for task A")
        time.sleep(1)
        
def taskB():
    for i in range(9, 0, -1):
        print(i, "seconds left for task B")
        time.sleep(1)
        
ta = threading.Thread(target=taskA)
tb = threading.Thread(target=taskB)

ta.start()
tb.start()

for i in range(6, 0, -1):
    print(i, "seconds left for task main")
    time.sleep(1)
