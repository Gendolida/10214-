age=int(input("나이를 입력하세요"))
print(age)
if int(age) < 8:
    print("입장료는 0원입니다.")

elif age<=19:
    print("입장료는 10000원입니다.")

elif age<=64:
    print("입장료는 20000원입니다.")

else:
    print("입장료는 5000원입니다.")