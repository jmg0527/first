
n = 0
while n < 10:
    n = n + 1
    if n % 3 == 0: continue
    print(n)


test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)


math_result = [25, 46, 59, 67, 80, 95]
number = 0
for mark in math_result:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 시험에서 통과했습니다." % number)
    else:
        print("%d번 학생은 시험에 불합격했습니다." % number )


score = float(input())
if score >= 1.0:
    print("error")
elif score <= 0.0:
    print("error")
elif score == 0.9:
    print("A")
elif score == 0.8:
    print("B")
elif score == 0.7:
    print("C")
elif score == 0.6:
    print("D")
elif score < 0.6:
    print("F")