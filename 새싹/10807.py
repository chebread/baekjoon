# n = 11
# a = 1 4 1 2 4 2 4 2 3 4 4
# v = 2
# 3

# n = 11
# a = 1 4 1 2 4 2 4 2 3 4 4
# v = 5
# 0

n = int(input())
a = map(int, input().split())
v = int(input())
x = 0 # 횟수
for i in a:
    if i == v:
        x += 1
print(x)
