import time
from threading import Thread

class ProgressBar:

    counter = 0
    m = 15
    dots = "..."

    def __init__(self):
        self.state = 0
        self.title = "Loading"
        self.message = ""
        self.string = ""

    def update(self):
        #str = "\r" + self.title + "\t\t|"
        str = self.title + "\t\t|"
        if self.state == 1:
            for i in range(self.m-1):
                str += "."
            str += "|\t"+self.message +"\t[Finished]"
            #print(str,end="")
            self.string = str
            return

        for i in range(self.counter):
                str += " "
        
        str += self.dots

        for i in range(self.m-self.counter-len(self.dots)-1):
                str += " "
        
        str += "|\t" + self.message

        #print(str,end="")
        self.string = str

        self.counter += 1
        self.counter = self.counter%(self.m-len(self.dots))


    def start(self):
        self.state = 0
        #self.t = Thread(target=self.__thread_func)
        #self.t.start()

    def stop(self):
        self.state = 1


if __name__ == "__main__":

    pb = ProgressBar()
    pb.start()
    for i in range(101):
        pb.message = str(i) + " %"
        time.sleep(0.03)
        if i == 100:
            pb.stop()
            break