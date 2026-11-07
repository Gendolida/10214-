num1 = int(input("첫번째 숫자"))
num2 = int(input("두번째 숫자"))
cal = input("연산자를 입력하세요")

if cal== "+":
    num3= num1+num2
    print(num3)

elif cal== "-":
    num3= num1-num2
    print(num3)

elif cal== "*":
    num3= num1*num2
    print(num3)

elif cal== "/":
    num3= num1/num2
    print(num3)

else:
    print("잘못된 연산자입니다.")
