def add_10(value):
    """value에 10을 더한 값을 돌려주는 함수"""
    if value < 10:
        return 10 # 즉시 종료
    result = value + 10
    return result

n = add_10(5)
print(n)

n = add_10(42)
print(n)

n = round(1.5)
print(n)


def root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    return r1, r2

x = 1
y = 2
z = -8

r1, r2 = root(x,y,z)
print('근은 {} {}'.format(r1, r2))