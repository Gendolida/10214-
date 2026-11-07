numbers = [12, 7, 19, 20, 33, 42, 8, 15, 26, 31]
a=0
count = 0
for number in numbers:

    if numbers[a] % 2 == 0:
        print("짝수:", numbers[a])
        count = count +1

    a += 1