# A+B, A-B, A*B, A/B(몫), A%B(나머지)
A, B = input().split(" ")
A = int(A)
B = int(B)
res = [
    A + B,
    A - B,
    A * B,
    A // B,
    A % B
]

for i in res:
    print(i)