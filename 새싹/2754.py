# 문제
# 어떤 사람의 C언어 성적이 주어졌을 때, 평점은 몇 점인지 출력하는 프로그램을 작성하시오.

# A+: 4.3, A0: 4.0, A-: 3.7

# B+: 3.3, B0: 3.0, B-: 2.7

# C+: 2.3, C0: 2.0, C-: 1.7

# D+: 1.3, D0: 1.0, D-: 0.7

# F: 0.0

# 입력
# 첫째 줄에 C언어 성적이 주어진다. 성적은 문제에서 설명한 13가지 중 하나이다.

# 출력
# 첫째 줄에 C언어 평점을 출력한다.

# 예제 입력 1 
# A0
# 예제 출력 1 
# 4.0

# 성적이 A... 이고 평점이 숫자 4... 이다.

grade = input() # A0 or F로 제시된다.
grade_a = grade[0] # A
A = [4.3, 4.0, 3.7] # +, 0, - 순이다.
B = [3.3, 3.0, 2.7]
C = [2.3, 2.0, 1.7]
D = [1.3, 1.0, 0.7]
if (grade_a == 'F'):
    print(0.0)
else:
    grade_b = grade[1] # +
    if grade_a == 'A':
        if grade_b == '+':
            print(A[0])
        elif grade_b == '0':
            print(A[1])
        else:
            print(A[2])
    elif grade_a == 'B':
        if grade_b == '+':
            print(B[0])
        elif grade_b == '0':
            print(B[1])
        else:
            print(B[2])
    elif grade_a == 'C':
        if grade_b == '+':
            print(C[0])
        elif grade_b == '0':
            print(C[1])
        else:
            print(C[2])
    else:
        if grade_b == '+':
            print(D[0])
        elif grade_b == '0':
            print(D[1])
        else:
            print(D[2])

# 또는,

dic = {'A+':'4.3', 'A0':'4.0', 'A-':'3.7',
       'B+':'3.3', 'B0':'3.0', 'B-':'2.7',
       'C+':'2.3', 'C0':'2.0', 'C-':'1.7',
       'D+':'1.3', 'D0':'1.0', 'D-':'0.7',
       'F':'0.0'}
grade = input()
print(dic[grade])

# 이렇게 딕셔너리로 처리하면 편하네....