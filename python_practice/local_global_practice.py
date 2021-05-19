#지역변수 : 함수내에서만 호출되고 사라지는 변수, 전역변수 : 프로그램 모든 공간에서 부를수있음
gun = 10
'''
def checkpoint(soldiers): #경계근무
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {}".format(gun))
checkpoint(2) #2명이 경계근무 나감
print("남은 총 : {}".format(gun))
'''
#위처럼 코딩하면 오류생김
#이유: 함수내의 gun은 지역변수로써 선언되어 처음선언한 gun=10 이 적용안됨
#함수내에 gun= 20 같이 다시 선언해주면 오류는 안생김
# global gun 이용
def checkpoint(soldiers): #경계근무
    global gun #gun을 전역변수로 쓰겠다 -> 앞에 gun = 10이 적용됨
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {}".format(gun))
checkpoint(2) #2명이 경계근무 나감
print("남은 총 : {}".format(gun))
#전역변수 많이쓰면 코드관리 어려워져서 권장되지않음

#권장되는 방식
gun=10
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun #함수의 gun값을 반환

print("전체 총 : {}".format(gun))
gun = checkpoint_ret(gun,2)
print("남은 총 : {}".format(gun))
