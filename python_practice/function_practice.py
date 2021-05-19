#함수 practice
def open_account(): #함수정의
    print("새로운 계좌가 출력되었습니다")

open_account() #실행

def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {}원입니다.".format(balance+money))
    return balance + money #return을 통해서 값을 반환함

def withdraw(balance,money):#출금
    if balance >= money: #잔액이 출금보다 많으면(출금가능)
        print("출금이 완료되었습니다. 잔액은 {}입니다".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {}입니다".format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금
    commission = 100 #수수료 100원
    return commission,balance - money - commission #수수료가 얼마가 나왔고, 잔액을 튜플형식으로 반환

balance = 0
balance = deposit(balance,1000)
print(balance) #return을통해 1000이 반환되서 0이아니라 1000이찍힘

balance = withdraw(balance,2000)
balance = withdraw(balance,1000)
print(balance)

balance = deposit(balance,1000)
comission ,balance = withdraw_night(balance,500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(comission,balance))
