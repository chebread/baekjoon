# 행렬 덧셈

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

# n, m = map(int, input().split()) # n*m 행렬
# a = [] # [[1, 1, 1], [2, 2, 2], [0, 1, 0]]
# b = [] # [[3, 3, 3], [4, 4, 4], [5, 5, 100]]
# for i in range(0, m):
#     x = list(map(int, input().split()))
#     a.append(x)
# for j in range(0, m):
#     x = list(map(int, input().split()))
#     b.append(x)

n, m = 3, 3
# n은 행(y축), m은 열(x축)이다.
a = [[1, 1, 1], [2, 2, 2], [0, 1, 0]]
b = [[3, 3, 3], [4, 4, 4], [5, 5, 5]]
# 즉, a[0][0] + b[0][0], a[0][1] + b[0][1], ... 이다.

for i in range(n): # - [ ] m으로 바꾸면 안되나?
    for j in range(n):
        # i = 0 j = 0
        # i = 0 j = 1
        result = a[i][j] + b[i][j]
        print(result,end=' ')
    print()

# 아. 인덱스를 활용하면 되는구나.