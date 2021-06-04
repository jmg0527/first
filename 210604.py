#Q1
#3번째가 참이므로 shirt 출력


#Q2
y= 3
three = [x * y for x in range(1,334)]
print(sum(three))

"""
result=0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)
"""

#Q3
star = 0
while star < 5:
    star = star + 1
    print("*" * star)

#Q4
for i in range(1,101):
    print(i)


#Q5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score

average = total / len(A)
print(average)


#Q6
numbers = [1,2,3,4,5]
result=[n * 2 for n in numbers if n % 2 == 1]
print(result)

def add(a,b):
    return a + b

print(add(3,5))
