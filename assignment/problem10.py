words = {
    "사과": "apple",
    "바나나": "banana",
    "학교": "school"
}
score=0
for key in words:
    print(key)
    ans=input()
    if ans in words[key]:
        print("정답입니다! 👍")
        score=score+1
    else:
        print("아쉬워요, 정답은",words[key], "입니다")
print(score)