#one line for문 연습

#출석번호가 1,2,3,4 앞에 100을 붙이기로함 -> 101, 102, 103, 104
student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student] #i라는 값에 100을 더한값을 student에 넣을건데 i는 student에 있는값
print(student)

# 학생이름을 길이로 바꿈
student= ["iron man", "thor", "groot"]
student = [len(i) for i in student] #위와 비슷
print(student)

#학생이름을 대문자로 바꿈
student= ["iron man", "thor", "groot"]
student = [i.upper() for i in student]
print(student)
