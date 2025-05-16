while True:
    try:
        a, b = input().split(" ")
        a = int(a)
        b = int(b)
        print(a + b)
    except:
        break

# try-except 구문이 핵심이었다...