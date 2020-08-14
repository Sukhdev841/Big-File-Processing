import time
from threading import Thread
from APIs.loading import *
import sys

class ProgressBars:

    bars = []

    def __init___(self):
        self.bars = []
        self.state = 0
        return
    
    def add_progress_bar(self,pb):
        self.bars.append(pb)

    def __update(self):
        finished_str = ""
        finished_index = []
        updated_bars = []
        for i in range(len(self.bars)):
            if self.bars[i].state == 1:
                """" This thread is finished """
                self.bars[i].update()
                finished_str += self.bars[i].string +"\t\t"
                finished_index.append(i)
            else:
                updated_bars.append(self.bars[i])
        
        if len(finished_index) > 0:
            while len(finished_str) <= self.last_print_len:
                finished_str += " "

            #del self.bars
            self.bars = updated_bars

            print("\r"+finished_str)

    def __thread_func(self):

        while True:

            if self.state == 1:
                break

            if len(self.bars) == 0:
                time.sleep(1)
                continue
            to_print = "\rRunning Tasks : "
            for i in range(len(self.bars)):
                self.bars[i].update()
                to_print += self.bars[i].string + "\t\t"
            
            self.last_print_len = len(to_print)
            print(to_print,end="")
            time.sleep(0.05)
            self.__update()

    def start(self):

        self.state = 0
        self.t = Thread(target=self.__thread_func)
        self.t.start()

    def stop(self):
        self.state = 1
        



def test():

    pbs = ProgressBars()
    pbs.start()

    pb1 = ProgressBar()
    pb1.title = "loading1"

    pb2 = ProgressBar()
    pb2.title = "loading2"

    pb3 = ProgressBar()
    pb3.title = "loading3"

    

    pbs.add_progress_bar(pb1)
    pbs.add_progress_bar(pb2)
    pbs.add_progress_bar(pb3)
    

    time.sleep(3)

    pb2.stop()
    #time.sleep(1)
    pb3.stop()
    time.sleep(4)
    pb1.stop()

    time.sleep(0.4)
    pbs.stop()

    return

if __name__ == "__main__":
    test()