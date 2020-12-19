people = 2
apple = 20

if people < apple /5:
    print('신나는 사과 파티! 배 터지게 먹자!')

if people % apple > 0:
    print('사과 수가 딱 맞지 않아! 몇 개는 쪼개 먹자!')


if people > apple:
    print('사람이 너무 많아! 몇 명은...')

if True:
    print(10)

if False:
    print(5)

from datetime import datetime
hour = datetime.now().hour
if hour % 6 == 0 :
    print('종이 울립니다')

if True:
    print('블럭에 속한 코드')

    if False:
        print('한 줄 더')

    if True:
        print('또 한 줄 더')
    print('블럭의 끝 코드')
print('블럭 끝')

if False:
    print('조건이 안 맞는 코드')

    if True:
        print('조건이 맞는 코드')

    print('어쨌든 실행되지 않는 코드')

print('다시 바깥에 있는 코드')