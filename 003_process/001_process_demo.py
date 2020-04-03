# -*- coding=utf-8 -*-

from multiprocessing import Process
from time import sleep
import os


def work1():
    while True:
        print('work 1, pid is:  %s' % os.getpid())
        sleep(1)


def main():
    p1 = Process(target=work1)
    p1.start()
    while True:
        print('work main, pid is: %s' % os.getpid())
        sleep(2)


if __name__ == '__main__':
    main()
