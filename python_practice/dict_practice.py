cabinet ={3: "앙" ,4: "하"}

print (cabinet.get(5))

print (cabinet.get(3))
print(cabinet.get(3 ,"사용가능"))
print(3 in cabinet)
print(5 in cabinet)

box = {"호" : 3}
print(box["호"])
print(box)
print(cabinet[3])
cabinet ={3: "허엇"}
print(cabinet[3])
cabinet [6] ="추가"
print(cabinet)

#삭제
del cabinet[3]

#key들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#ket, value 쌍으로 출력
print(cabinet.items())

#다삭제
cabinet.clear
print(cabinet)

