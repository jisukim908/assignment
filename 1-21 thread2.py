import threading
import os


def foo():
    print('thread id', threading.get_native_id())
    print('process id', os.getpid())


if __name__ == '__main__':
    print('process id', os.getpid())
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=foo).start()
    thread3 = threading.Thread(target=foo).start()


# 실행결과
# process id 7052
# thread id 20544
# process id 7052
# thread id 31604
# process id 7052
# thread id 2200
# process id 7052
