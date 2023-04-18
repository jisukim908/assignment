import threading
import os


def foo():
    print('thread id', threading.get_native_id())
    print('process id', os.getpid())


if __name__ == '__main__':
    print('process id', os.getpid())
    thread = threading.Thread(target=foo).start()

# 실행결과
# process id 28140
# thread id 2536
# process id 28140
