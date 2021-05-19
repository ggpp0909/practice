  
#ramdom모듈의 셔플과 샘플 활용예제
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst) #리스트의 값 순서 무작위로 바꿈
# print(lst)
# print(sample(lst,1))#리스트중에 한개를 무작위로 뽑음


#치킨, 커피 당첨자 추첨프로그램 (내가만든)
ID = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
from random import *
shuffle(ID)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(ID[0]))
print("커피 당첨자 : {}".format(ID[1:4]))
print("-- 축하합니다 --")

#정답
from random import *
users = range(1,21) #1부터 20까지 숫자를 생성 but, type이 range라 바꿔줘야함
users = list(users)
shuffle(users)

winners = sample(users, 4) #네명중 1명은 치킨 3명은 커피
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print("-- 축하합니다 --")
