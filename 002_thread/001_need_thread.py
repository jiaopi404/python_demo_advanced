# coding=utf-8
from time import sleep


def sing():
    for i in range(3):
        print('sing: %s' % i)
        sleep(1)
    pass


def dance():
    for i in range(3):
        print('dance: %s' % i)
        sleep(1)
    pass


def main():
    sing()
    dance()
    pass


if __name__ == '__main__':
    main()
