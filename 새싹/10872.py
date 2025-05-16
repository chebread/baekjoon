num = int(input()) # num >= 0

# 1 => 1
# 2 => 2 * 1
# 3 => 3 * 2 * 1

if num == 0:
    print(1)
else:
    sum = None
    for i in range(1, num + 1):
        # i = 1
        # i = 2
        # i = 3
        if i == 1:
            sum = i
        else:
            sum *= i

    print(sum)