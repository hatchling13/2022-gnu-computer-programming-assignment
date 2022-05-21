import turtle
import random

t = turtle.Turtle()
t.speed('fastest')

r = random.Random()

score = 0
print('점수가 51을 넘어가면 패배합니다!')

dice_eye_color = ['red', 'blue', 'green']

while True:
    # top left = (-250, 100), length = 200
    t.penup()
    t.goto(-250, 100)
    t.pendown()

    t.color('white')
    t.begin_fill()
    for x in range(4):
        t.fd(200)
        t.rt(90)

    t.end_fill()
    t.color('black')

    for x in range(4):
        t.fd(200)
        t.rt(90)

    left_dice = r.randint(1, 6)
    score += left_dice
    left_eye_pos = []

    if left_dice == 1:
        left_eye_pos = [[-150, -25]]
    elif left_dice == 2:
        left_eye_pos = [[-200, 25], [-100, -75]]
    elif left_dice == 3:
        left_eye_pos = [[-200, 25], [-150, -25], [-100, -75]]
    elif left_dice == 4:
        left_eye_pos = [[-200, 25], [-200, -75], [-100, 25], [-100, -75]]
    elif left_dice == 5:
        left_eye_pos = [[-200, 25], [-200, -75], [-150, -25], [-100, 25], [-100, -75]]
    else: # left_dice == 6:
        left_eye_pos = [[-200, 25], [-200, -25], [-200, -75], [-100, 25], [-100, -25], [-100, -75]]

    for pos in left_eye_pos:
        t.penup()
        t.goto(pos[0], pos[1])
        t.pendown()
        t.color(dice_eye_color[r.randint(0, 2)])
        t.begin_fill()
        t.circle(20)
        t.end_fill()

    # top left = (50, 100), length = 200
    t.penup()
    t.goto(50, 100)
    t.pendown()

    t.color('white')
    t.begin_fill()
    for x in range(4):
        t.fd(200)
        t.rt(90)

    t.end_fill()
    t.color('black')

    for x in range(4):
        t.fd(200)
        t.rt(90)

    right_dice = r.randint(1, 6)
    score += right_dice
    right_eye_pos = []

    if right_dice == 1:
        right_eye_pos = [[150, -25]]
    elif right_dice == 2:
        right_eye_pos = [[100, 25], [200, -75]]
    elif right_dice == 3:
        right_eye_pos = [[100, 25], [150, -25], [200, -75]]
    elif right_dice == 4:
        right_eye_pos = [[100, 25], [100, -75], [200, 25], [200, -75]]
    elif right_dice == 5:
        right_eye_pos = [[100, 25], [100, -75], [150, -25], [200, 25], [200, -75]]
    else: # right_dice == 6:
        right_eye_pos = [[100, 25], [100, -25], [100, -75], [200, 25], [200, -25], [200, -75]]
        
    for pos in right_eye_pos:
        t.penup()
        t.goto(pos[0], pos[1])
        t.pendown()
        t.color(dice_eye_color[r.randint(0, 2)])
        t.begin_fill()
        t.circle(20)
        t.end_fill()

    print('현재 점수는 %d점입니다!\n' % score)

    if score <= 51:
        if score == 51:
            print('축하합니다! 최고 점수입니다!')
            break
        else:
            end = False
            
            while True:
                will_reroll = input('계속 던지시려면 yes, 멈추려면 no를 입력하세요 : ')
                if will_reroll == 'yes':
                    print('주사위를 다시 굴립니다.\n')
                    break
                elif will_reroll == 'no':
                    end = True
                    print('현재 점수에서 멈춥니다.\n')
                    break
                else:
                    print('다시 입력하세요.\n')

            if end == True:
                break
            
    else:
        score = 0
        print('최대 점수를 초과했습니다!!!')
        break

if score == 0:
    print('다음 번엔 좀 더 신중히 생각해봐요!')
else:
    print('최종 점수는 %d점입니다!!!' % score)
