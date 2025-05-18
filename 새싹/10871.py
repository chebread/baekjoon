# 10 5
# 1 10 4 9 2 3 8 5 7 6

n, x = map(int, input().split())
a = map(int, input().split())

for i in a:
    if i < x:
        print(i)