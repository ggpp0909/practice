#튜플 (list와 비슷하지만 내용수정 불가, 빠르게사용가능)

menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])
#menu.add("생선까스") 오류남 -> 튜플 내용추가(수정)안됨

# name = '김종국'
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국" ,20 , "코딩") #한번에 선언가능
print(name, age, hobby)
