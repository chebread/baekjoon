i = int(input())
list = []
for n in range(0, i):
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    list.append(a + b)


for elem in list:
    print(elem)