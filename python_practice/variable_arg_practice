#가변인자 practice

# def profile(name, age, lang1, lang2, lang3 ,lang4, lang5):
#     print("이름: {0}\t나이 : {1}\t".format(name,age), end=" ")
#     #end=" "는 끝나고 줄바꿈하지않고 공백으로 끝낸다는뜻
#     print(lang1,lang2,lang3,lang4,lang5)

# profile("유재석",20,"python","java","C","C++","C#")
# profile("김태호",25,"kotlin","swift","","","")

def profile(name, age, *language): #가변인자 사용하여 위처럼 귀찮은일 없앰
    print("이름: {0}\t나이 : {1}\t".format(name,age), end=" ")
    
    for lang in language:
        print(lang, end=" ")
    print()#줄바꿈용
    
profile("유재석",20,"python","java","C","C++","C#","java")
profile("김태호",25,"kotlin","swift")
