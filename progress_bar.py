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
        for i in range(len(self.bars)):
            if self.bars[i].state == 1:
                """" This thread is finished """
                self.bars[i].update()
                finished_str += self.bars[i].string +"\n"
                finished_index.append(i)
        
        if len(finished_index) > 0:
            for index in finished_index:
                del self.bars[index]
            print("\n"+finished_str)

        if len(self.bars) == 0:
            print("\nAll Tasks Finished.\n")

    def __thread_func(self):

        while True:

            if self.state == 1:
                break

            if len(self.bars) == 0:
                time.sleep(1)
                continue
            #sys.stdout.write("\033[2F")
            #sys.stdout.flush()
            to_print = "\rRunning Tasks : \t"
            for i in range(len(self.bars)):
                self.bars[i].update()
                to_print += self.bars[i].string
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

    pb1 = ProgressBar()
    pb1.title = "loading1"
    pb1.start()

    pb2 = ProgressBar()
    pb2.title = "loading2"
    pb2.start()

    pbs = ProgressBars()

    pbs.add_progress_bar(pb1)
    pbs.add_progress_bar(pb2)
    pbs.start()

    time.sleep(1)

    pb2.stop()

    time.sleep(4)
    pb1.stop()

    time.sleep(0.4)
    pbs.stop()

    return

if __name__ == "__main__":
    test()