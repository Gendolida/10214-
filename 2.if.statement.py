if True:
    print("True")
    print("True라면 내부는 모두 수행합니다")

if False:
    print("False")
    print("False라면 내부는 모두 수행하지않습니다.")

if True:
    print("True")
    print("True라면 내부는 모두 수행합니다")
else: # !False = True
    print("Else")
    print("위 조건들이 True가 아닐때 실행됩니다.")


print("Always")
print("=====================")
score = 70

if score > 80:
    print("A학점입니다.")
if score > 60:
    print("B학점입니다.")
if score > 40:
    print("C학점입니다.")
if score > 20:
    print("D학점입니다.")
if score > 0:
    print("낙제입니다.")
print("=====================")

#var = 1
#var2 = 2

#if var1 > var2:
#    print("var1이 더 큽니다.")
#elif var1 == var2:
    #print("var1과 var2가 같습니다.")
#else:
#    print("var2가 더 큽니다.")

print("=====================")
#print("1. 게임 시작")
#print("2. 랭킹 확인")
#print("0. 게임종료")
#print("=====================")
#user_input = input("원하는 동작을 입력하세요")

#elif user_input == "1":
#    print("게임을 시작합니다.")
#else:
#    ("게임을 재시작합니다.")


num1 = int(input("첫번째 숫자를 입력하세요"))
num2 = int(input("두번째 숫자를 입력하세요"))
op = (input("연산자를 입력하세요 "))

if number1.isdigit() and num2.isdigit():
    if op == "+":
        print(int(num1) + int(num2))
    elif op == "-":
        print(int(num1) - int(num2))
    elif op == "*":
        print(int(num1) * int(num2))
    elif op == "/":
        print(int(num1) / int(num2))
    else:
        print("잘못된 입력입니다.")
    else:
        print("숫자가 아닌 입력을 했습니다.")