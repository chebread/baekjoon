# A가 B보다 큰 경우에는 '>'를 출력한다.
# A가 B보다 작은 경우에는 '<'를 출력한다.
# A와 B가 같은 경우에는 '=='를 출력한다.
# a b 입력

a, b = input().split(" ")
a = int(a) # 재할당
b = int(b)

# 이거는 a, b = map(int, input().split()) 이렇게 축약하는게 파이서닉한 방법이다.

# map(function, iterable)
# function: 각 요소에 적용할 함수입니다.
# iterable: 함수를 적용할 데이터 집합입니다.
# map() 함수는 iterable의 각 요소에 대해 function 함수를 적용한 결과를 새로운 iterator로 반환합니다. 이때, function 함수는 각 요소를 인자로 받아서 처리하며, 함수의 반환값이 새로운 iterator의 각 요소가 됩니다.

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("=")