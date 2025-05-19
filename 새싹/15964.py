# 연산자의 기호는 ＠으로, A＠B = (A+B)×(A-B)으로 정의내리기로 했다.
# 4 3 => 7
def f(x, y):
    return (x + y) * (x - y)
a, b = map(int, input().split())
print(f(a, b))