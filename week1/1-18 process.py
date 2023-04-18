from multiprocessing import Process
import os

# 1
# print('hello os')
# print('my pid is', os.getpid())

# 실행결과
# # hello os
# # my pid is 28528

# 2
# def foo():
#     print('chile process', os.getpid())
#     print('my parent is', os.getppid())

# if __name__ == '__main__':
#     print('parent process', os.getpid())
#     child = Process(target=foo).start()

# 실행결과
# # parent process 5100
# # chile process 26048
# # my parent is 5100


# 3
def foo():
    print('hello, os')


if __name__ == '__main__':
    child1 = Process(target=foo).start()
    child2 = Process(target=foo).start()
    child3 = Process(target=foo).start()

# hello, os
# hello, os
# hello, os
