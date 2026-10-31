arr = ["apple", "banana", "cherry"]

print("메뉴 리스트")
for item in arr:
    print(item)

print("------------------")
print("메뉴 리스트")
sale_list = {'apple':1, 'banana':0, 'cherry':3}
for key in sale_list:
    if sale_list[key] ==0:
        print(key, "sold out")
    else:
        print(key, sale_list[key])

print("------------------")
for i in range(10):
    print(i)
"""
# while 문으로 동일하게 수행하려면
a = 0
while a < 10:
    print(a)
    
    a += 1 
"""


print("------------------")
ex_arr = [num for num in range(10)]
print(ex_arr)

class_scores = [
    {
        "김철수": {"국어": 85, "영어": 90, "수학": 78, "과학": 92}
    },
    {
        "이영희": {"국어": 92, "영어": 88, "수학": 95, "과학": 96}
    },
    {
        "박민수": {"국어": 76, "영어": 65, "수학": 82, "과학": 70}
    },
    {
        "정수진": {"국어": 88, "영어": 94, "수학": 90, "과학": 89}
    },
    {
        "한동석": {"국어": 60, "영어": 72, "수학": 65, "과학": 58}
    }
]
class_scores = {
    "김철수": {"국어": 85, "영어": 90, "수학": 78, "과학": 92},
    "이영희": {"국어": 92, "영어": 88, "수학": 95, "과학": 96},
    "박민수": {"국어": 76, "영어": 65, "수학": 82, "과학": 70},
    "정수진": {"국어": 88, "영어": 94, "수학": 90, "과학": 89},
    "한동석": {"국어": 60, "영어": 72, "수학": 65, "과학": 58}
}
print("[개인별 평균]")
for name in class_scores:
    total = 0
    for score in class_scores[name].values():
        total += score
    print(name, total / 4)

print()
search = input("검색할 이름: ")
if search in class_scores:
    print(class_scores[search])
else:
    print("없는 학생입니다.")

print()
print("[과목별 최고 득점자]")
for subject in ["국어", "영어", "수학", "과학"]:
    best_name = ""
    best_score = 0
    for name in class_scores:
        if class_scores[name][subject] > best_score:
            best_score = class_scores[name][subject]
            best_name = name
    print(subject, best_name, best_score)