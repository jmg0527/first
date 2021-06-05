"""
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(2,5,6)
print(result)
"""


def add_mul(choice, *args):
    if choice == "add": # 입력받은 모든 수 더하기
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul": # 입력받은 모든 수 곱하기
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 2,4,6,8)
print(result)

result = add_mul('mul', 2,4,6,8)
print(result)


# 키워드 파라미터 ** (**을 매개변수 이름 앞에 붙이면 매개변수는
# 딕셔너리가 되고 입력 값은 저장됨

def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(a=1)

print_kwargs(name='mingyo', age=22)


def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result)

result1, result2 = add_and_mul(3,4)
print(result1, result2)

def say_myself(name, old, man=True):
    print("저의 이름은 %s 입니다." % name)
    print("저의 나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

print(say_myself("정민교", 22, True))

# input 입력되는 모든 것을 문자열로 취급

number = input("입력 받은 내용을 출력합니다")

print(number)