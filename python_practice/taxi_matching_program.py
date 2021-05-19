#50명의 승객과 매칭기회가 있을때 총 탑승 승객수를구하는 프로그램
#조건 1 : 승객별 운행 소요시간은 5~50사이의 난수
#조건 2 : 소요시간 5~15 사이의 승객만 매칭해야함

#내가만든코드
from random import *
customer = range(1,51)
customer = list(customer)
count = 0
for i in customer:
    customer_time=int(random()*46)+5 #5~50사이의 난수 생성
    print("{0}번째 손님 (소요시간 : {1}분)".format(customer[i-1],customer_time))
    if 5 <= customer_time <= 15: #5~15사이의 승객수 세기
        count += 1

print("총 탑승 승객 : {} 분".format(count))

#정답
from random import *
cnt = 0 #총 탑승 승객 수
for i in range(1,51): # 1~50의 승객
    time = randrange(5,51)#5분~50분 소요시간
    if 5<= time <= 15: #5분에서 15분 이내의 손님
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i,time))#매칭성공
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))#매칭실패

print("총 탑승 승객 : {} 분".format(cnt))
    
