money = True
if money:
        print("저축을 하자")
else:
        print("돈을 아끼자")

pocket = ['paper', 'money', 'iphone']
if 'money' in pocket:
    pass
else:
    print("카드를 쓰자")

iost_price = 36
if iost_price < 70:
    print("손실중")
elif iost_price >= 70:
    print("이득중")
elif iost_price >= 100:
    print("떡상")
elif iost_price <= 30:
    print("ㅈㅈ")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number !=4:
    print(prompt)
    number = int(input())


coffee = 10
while True:
    money = int(input("돈을 입력해주세요: "))
    if money == 300:
        print("커피를 주문합니다")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d원을 반환하고 커피를 주문합니다." % (money - 300))
        coffee = coffee - 1
    else:
        print("금액이 부족합니다. 커피 주문이 취소 되었습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 매진되었습니다. 주문 불가능합니다.")
        break

# 금액을 입력 받고 커피 최대 개수 시키고, 남은 커피 갯수와 주문한 커피 갯수 출력하기
# 잔돈도 출력하기
"""
coffee = 1500
money = int(input())
while money:
    print("금액이 충분합니다. 커피를 주문합니다")
"""