import time , threading
def foo():
    print(time.ctime())
    threading.Timer(0.1,foo).start()

foo()  
while 1:
    print(55)
    time.sleep(1)
