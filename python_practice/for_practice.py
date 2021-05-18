#for practice
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

#for 변수 in list -> list에있는 거를 차례대로 변수에 가져옴
for waiting_no in range(5): # 0,1,2,3,4
    print("대기번호 : {0}".format(waiting_no))


starbucks = ["아이언맨","토르", "그루트"]
for customer in starbucks:
    print("{},커피가 준비되었습니다.".format(customer))
