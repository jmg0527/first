
# a리스트의 각 항목에 3을 곲한 결과를 result 리스트에 담기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

# " 리스트 내포 사용

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

# 리스트 내포 = 표현식 for 항목 in 반복 가능 객체 if 조건
# ex) num * 3 for num in a if num % 2 == 0
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [x * y for x in range(2,10)
                for y in range(1,10)]
print(result)

star = 0
while star < 5:
    star = star + 1
print("*" * star, end="")