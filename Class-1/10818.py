# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
N = int(input())
list = list(map(int, input().split()))

# max = list[0]
# min = list[0]

# for i in range(0, N):
#     a =  list[i]
#     if max < a:
#         max = a
#     if min > a:
#         min = a

# print(min, max)

# 이 방법 보다 min, max 함수를 쓰는게 더 효울적이다.
# min(x)은 인수로 받은 자료형 내에서 최소값을 찾아서 반환하는 함수 입니다.
# 여기서 중요한게 x는 iterable 한 자료형이 들어가야한다는 것 입니다.
# 즉, min(iterable)은 iterable에서 가장 작은 값을 찾아서 반환한다.

print(max(list), min(list))