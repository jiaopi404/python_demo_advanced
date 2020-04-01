import threading
from time import sleep


def say_sorry():
    print('I am sorry')
    sleep(1)


def main():
    for i in range(5):
        t = threading.Thread(target=say_sorry)
        t.start()
    pass


if __name__ == '__main__':
    main()
