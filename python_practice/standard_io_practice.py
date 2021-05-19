#표준 입출력

print("python", "java" ,sep=",") #,자리에 ,넣기
print("python", "java" ,sep=" vs ")#,자리에 vs 넣기
print("python", "java" ,"c++",sep=" vs ")#,자리에 vs 넣기

print("python", "java" ,sep="," , end="? ") #print의 끝을 줄바꿈이아니라 end부분으로 바꿈
print("무엇이 더 재밌을까요?")

import sys
print("python", "java" ,file=sys.stdout) #표준 출력으로 문장이 찍힘
print("python", "java" ,file=sys.stderr) #표준 에러

score = {"수학":0, "영어":50, "코딩":100} #dic
for subject, score in score.items(): #items로 하면 key와 value 페어로 나옴
    #print(subject,score)
    print(subject.ljust(8),str(score).rjust(4),sep=":")#왼쪽정렬을 하는데, 8칸의 공간을 확보하고 왼쪽으로 정렬
    #score는 4칸확보후 오른쪽 정렬

#은행 대기순번표
#001, 002, 003, ...

for number in range(1,21):
    print("대기번호 : " + str(number).zfill(3))#3칸의 공간을 확보하고 빈공간 0으로채움

answer = input("아무값이나 입력하세요 : ") #사용자가 값을 입력하면 "문자열"형태로 answer에저장
print("입력하신 값은 " + answer +"입니다.")
