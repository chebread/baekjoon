# 아니 입력을 받고, 그에 따라 출력을 하면 된다는 거다. 즉, 입력 - 출력 - 입력 -출력 무한 반복이다.
while True:
  try:
    s = input()
    if s == '':
        break
    else:
        print(s)
  except:
     break
  
# - [ ] 아니 근데 왜 except try가 있어야 되는거야? EOF 에러발생 한다는데? 이게 뭐지?