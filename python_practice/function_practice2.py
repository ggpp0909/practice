#기본값 practice
# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang))

# profile("유재석", 20 , "파이썬")
# profile("김태호", 25, "자바")

#같은학교 같은반 수업

def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
        .format(name, age, main_lang))  #위와 동일하지만 값을 전달못받으면 기본값이나옴

profile("유재석")
profile("김태호")
profile("장영남")
