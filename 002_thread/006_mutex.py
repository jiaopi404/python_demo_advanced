# coding=utf-8

# 互斥锁 demo

import threading
import time

g_num = 0

mutex = threading.Lock()


def work1(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()

    print('work 1: g_num is: %s' % g_num)
    pass


def work2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()

    print('work2: g_num is: %s' % g_num)
    pass


t1 = threading.Thread(target=work1, args=(1000000,))
t2 = threading.Thread(target=work2, args=(1000000,))

t1.start()
t2.start()

while len(threading.enumerate()) != 1:
    time.sleep(1)

print('after work1 and work2, g_num is: %s ' % g_num)
