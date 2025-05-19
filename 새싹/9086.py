# 각 테스트 케이스에 대해서 주어진 문자열의 첫 글자와 마지막 글자를 연속하여 출력한다.
i = int(input())
for a in range(0, i):
    s = input()
    print(f"{s[0]}{s[-1]}")