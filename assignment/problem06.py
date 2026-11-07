password= "python123"
a=0
while a<1:
    ibm=input()
    if ibm==password:
        print("로그인 성공! 환영합니다.")
        break

    else:
        print("비밀번호가 틀렸습니다. 다시 입력")
