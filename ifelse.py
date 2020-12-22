SCISSOR = '가위'
ROCK = '바위'
PAPER = '보'

WIN = '승리!'
DRAW = '무승부'
LOSE = '패배'

mine = '보'
yours = '바위'

if mine == yours:
    result = DRAW
else:
    if mine == SCISSOR:
        if yours == ROCK:
            result = LOSE
        else:
            result = WIN
    elif mine == ROCK:
        if yours == PAPER:
            result = LOSE
        else:
            result = WIN
    elif mine == PAPER:
        if yours == SCISSOR:
            result = LOSE
        else:
            result = WIN
    else:
        print('오류')


print(result)


gender = "남자"
if gender == "남자":
    print("남자입니다.")
elif gender == "여자":
    print("여자입니다.")
else:
    print("논바이너리입니다")
