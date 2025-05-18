# import sys
# input = sys.stdin.readline
# print = sys.stdout.write
# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우
# # .rstrip()(오른쪽 공백문자 제거)을 추가로 해 주는 것이 좋다.

import sys
s_input = sys.stdin.readline

l = input = s_input().rstrip()
list = []
for i in range(0, int(l)):
    a, b = map(int, s_input().split())
    res = a + b
    list.append(res)
for j in list:
    print(str(j))

# - [ ] s_input 이란 무엇인가?