list = []
while True:
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    if a == 0 and b == 0: # or (a, b) == (0, 0) 이렇게 볼 수도 있다.
        break
    list.append(a + b)


for elem in list:
    print(elem)