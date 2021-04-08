# coding: utf-8
import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = 'i am ' + self.name + '   @   ' + str(i) + '\r\n'
            print(msg)


if __name__ == '__main__':
    t1 = MyThread()
    t1.start()
    t2 = MyThread()
    t2.start()
    t3 = MyThread()
    t3.start()
    t4 = MyThread()
    t4.start()
    t5 = MyThread()
    t5.start()