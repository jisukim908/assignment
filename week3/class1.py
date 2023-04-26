# 재귀함수 : 스스로를 호출하는 함수
# 코테할 때 완전 중요함!!!
import sys

def recursion(n):
   print(n)
   recursion(n+1)

recursion(1)

# errormessage
# RecursionError: maximum recursion depth exceeded while calling a Python object
# 종료 조건을 제대로 명시하지 않았다는 것!!

print(sys.getrecursionlimit()) # 1000

