a = {1 : 'hi' , 2 : 'Hello'}
print(a[1])


grade = {'pey':10, 'julliet':99}
grade['pey']
grade['julliet']

a = {'name': 'mingyo', 'phone': '01095121614', 'birth': '20000527'}
print(a.keys())

for k in a.keys():
        print(k)

print(list(a.keys()))

print(a.values())
for k in a.values():
        print(k)
print(a.items())

print(a.get('name'))

a.clear()
print(a)

a.get('old', '1~100')

s1 = set([1,2,3,4])
print(s1)

s2 = set("hello")
print(s2)
a = 2
while a<=1000:
        a = a*5
b = 5
while b<=1000:
        b = b*5
a1 = set(a)
a2 = set(b)
print(sum(a1 & a2))