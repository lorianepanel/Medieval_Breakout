import pgzrun

from random import randint

WIDTH = 1170
HEIGHT = 900


GREEN = 38,0,77
BOX = Rect((0, 540), (WIDTH, HEIGHT))



n = None



castle = [[ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0 ],
          [ 0, n, n, n, n, n, n, n, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, n, n, n, n, n, n, n, 0 ],
          [ 0, n, n, n, n, n, n, n, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, n, n, n, n, n, n, n, 0 ],
          [ 0, n, n, n, n, n, n, n, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, n, n, n, n, n, n, n, 0 ],
          [ 0, n, n, n, n, n, n, n, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, n, n, n, n, n, n, n, 0 ],
          [ 0, n, n, n, n, n, n, n, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, n, n, n, n, n, n, n, 0 ],
          [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
          [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
          [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
          [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
          [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
          [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
          [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 2, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
          [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 2, 2, 2, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
          [ 0, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 2, 2, 2, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, 0 ],
          [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         ]



all_bricks = []



for y in range(0, len(castle)) :
    for x in range(0, 35) :


        if castle[y][x] == None :

            n = randint(0,4)

            if n == 0 :
                brick = Actor("brick2", anchor=["left","top"])
                brick.pos = [(x*30) + 60 , (y*30) + 60]
                all_bricks.append(brick)


            if n == 2 :
                brick = Actor("door", anchor=["left","top"])
                brick.pos = [(x*30) + 60 , (y*30) + 60]
                all_bricks.append(brick)

            if n == 3 :
                brick = Actor("window", anchor=["left","top"])
                brick.pos = [(x*30) + 60 , (y*30) + 60]
                all_bricks.append(brick)


        else :
                    
            if castle[y][x] == 0 :
                brick = Actor("brick2", anchor=["left","top"])
                brick.pos = [(x*30) + 60 , (y*30) + 60]
                all_bricks.append(brick)

            if castle[y][x] == 2 :
                brick = Actor("door", anchor=["left","top"])
                brick.pos = [(x*30) + 60 , (y*30) + 60]
                all_bricks.append(brick)

            if castle[y][x] == 3 :
                brick = Actor("window", anchor=["left","top"])
                brick.pos = [(x*30) + 60 , (y*30) + 60]
                all_bricks.append(brick)




player = Actor("player3")
player.pos = [WIDTH/2, 860]

ball = Actor("ball3")
ball.pos = [WIDTH/2, 600]
ball_speed = [4, -4]



def on_mouse_move(pos):
    # player.x = pos[0]
    player.pos = [pos[0], player.pos[1]]


def invert_horizontal_speed():
    ball_speed[0] = ball_speed[0] * -1

def invert_vertical_speed():
    ball_speed[1] = ball_speed[1] * -1



def update() :

    new_x = ball.pos[0] + ball_speed[0]
    new_y = ball.pos[1] + ball_speed[1]
    ball.pos = [new_x, new_y]

    if ball.right > WIDTH or ball.left < 0 :
        invert_horizontal_speed()

    if ball.top < 0 :
        invert_vertical_speed()

    if ball.colliderect(player):
        invert_vertical_speed()

    for brick in all_bricks :
        if ball.colliderect(brick):
            all_bricks.remove(brick)
            invert_vertical_speed()


def draw():

    screen.clear()

    # screen.fill((153,0,230))

    screen.draw.filled_rect(BOX, GREEN)

    for brick in all_bricks :
        brick.draw()

    player.draw()

    ball.draw()


    if len(all_bricks) == 0 :
        screen.clear()
        screen.draw.text("YOU WIN :)", (100, 100), color="green", gcolor="purple", fontsize=150)














#DERNIERE LIGNE ONLY
pgzrun.go()