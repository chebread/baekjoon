# 3 3

# 1 1 1
# 2 2 2
# 0 1 0
# 3 3 3
# 4 4 4
# 5 5 100

# 4 4 4
# 6 6 6
# 5 6 100

n, m = map(int, input().split()) # n*m 행렬
a = [] # [[1, 1, 1], [2, 2, 2], [0, 1, 0]]
b = [] # [[3, 3, 3], [4, 4, 4], [5, 5, 100]]
for i in range(0, m):
    x = map(int, input().split())
    a.append(x)
for j in range(0, m):
    x = map(int, input().split())
    b.append(x)

#  - [ ] 행렬 내적하는 거 구현하기