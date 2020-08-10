import time
from threading import Thread

state = 0
title = "Loading ISF"
message = ""

def thread_func():
    global state
    global message
    global title

    counter = 0
    m = 15
    dots = "..."
    
    while True:
        str = "\r" + title + "\t\t|"

        if state == 1:
            for i in range(m-1):
                str += "."
            str += "|\t"+message +"\t[Finished]"
            print(str,end="")
            break

        for i in range(counter):
                str += " "
        
        str += dots

        for i in range(m-counter-len(dots)-1):
                str += " "
        
        str += "|\t" + message

        print(str,end="")

        counter += 1
        counter = counter%(m-len(dots))
        time.sleep(0.05)


def start_loading():
    global state
    global message
    state = 0
    t = Thread(target=thread_func)
    t.start()
    for i in range(1000):
        message = str(i) + " Packets Proccessed."
        time.sleep(0.1)
        if i == 100:
            state = 1
            break

def stop_loading():
    global state
    state = 1

def exec():
    start_loading()
    #time.sleep(10)
    #stop_loading()

exec()