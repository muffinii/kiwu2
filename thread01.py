# function based
import threading

def worker():
    print("work")

t = threading.Thread(target=worker)
t.start()

# class based
# import threading
#
# class MyThread(threading.Thread):
#     def run(self):
#         print("work")
# t = MyThread()
# t.start()
# t.join()
