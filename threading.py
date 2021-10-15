import threading
import time

def useless_function():
	print("hi: ", time.time())


t = threading.Thread(target=useless_function)
t2 =  threading.Thread(target=useless_function)

t.start()

time.sleep(4)
t2.start()
t.join()
t2.join()
