import pgzrun
from random import randint



WIDTH = 1280
HEIGHT = 800





player = Actor("player3")
player.pos = [WIDTH/2, 740]

ball = Actor("ball3")

ball.pos = [WIDTH/2, 700]
speed = 0
ball_speed  = [speed , - speed]

timer = 0

score = 0

start_button = Actor("start_button")
start_button.pos = [WIDTH/2, 700]



click = False



# LEVELS

castle1 = [ [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0 ],
            [ 0, 0, 0, 2, 3, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 2, 3, 2, 0, 0, 0 ],
            [ 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0 ],
            [ 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 2, 3, 2, 2, 3, 2, 0, 0, 0, 2, 3, 2, 2, 3, 2, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0 ],
            [ 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 2, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0 ],
            [ 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 2, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],]


n = None

castle2 = [ [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0 ],
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
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],]




def create_level(level) :

    

    global all_bricks
    global ball_speed

    all_bricks = []

    for y in range(0, len(level)) :
        for x in range(0, 35) :

            if level == castle1 :

                if castle1[y][x] == 0 :
                    brick = Actor("brick_ok", anchor=["left","top"])
                    brick.pos = [(x*30) + 120 , (y*30) + 30]
                    all_bricks.append(brick)

                if castle1[y][x] == 2 :
                    brick = Actor("door_ok", anchor=["left","top"])
                    brick.pos = [(x*30) + 120 , (y*30) + 30]
                    all_bricks.append(brick)

                if castle1[y][x] == 3 :
                    brick = Actor("window_ok", anchor=["left","top"])
                    brick.pos = [(x*30) + 120 , (y*30) + 30]
                    all_bricks.append(brick)



            if level == castle2 :


                if castle2[y][x] == None :

                    n = randint(0,4)

                    if n == 0 :
                        brick = Actor("brick_ok", anchor=["left","top"])
                        brick.pos = [(x*30) + 120 , (y*30) + 30]
                        all_bricks.append(brick)


                    if n == 2 :
                        brick = Actor("door_ok", anchor=["left","top"])
                        brick.pos = [(x*30) + 120 , (y*30) + 30]
                        all_bricks.append(brick)

                    if n == 3 :
                        brick = Actor("window_ok", anchor=["left","top"])
                        brick.pos = [(x*30) + 120 , (y*30) + 30]
                        all_bricks.append(brick)


                else :
                            
                    if castle2[y][x] == 0 :
                        brick = Actor("brick_ok", anchor=["left","top"])
                        brick.pos = [(x*30) + 120 , (y*30) + 30]
                        all_bricks.append(brick)

                    if castle2[y][x] == 2 :
                        brick = Actor("door_ok", anchor=["left","top"])
                        brick.pos = [(x*30) + 120 , (y*30) + 30]
                        all_bricks.append(brick)

                    if castle2[y][x] == 3 :
                        brick = Actor("window_ok", anchor=["left","top"])
                        brick.pos = [(x*30) + 120 , (y*30) + 30]
                        all_bricks.append(brick)

        ball.pos = [WIDTH/2, 700]
        speed = 0
        ball_speed  = [speed , - speed]



def on_mouse_down(pos) :
    if start_button.collidepoint(pos) :
        global speed
        global ball_speed
        global click

        speed = 3
        ball_speed = [ speed, - speed]
        music.play("bardcore")
        click = True






create_level(castle1)








def on_mouse_move(pos):

    player.pos = [pos[0], player.pos[1]]


def invert_horizontal_speed():
    ball_speed[0] = ball_speed[0] * -1

def invert_vertical_speed():
    ball_speed[1] = ball_speed[1] * -1


# def accelerate_ball():
    
#     global ball_speed
#     global speed
#     global score


#     if ball_speed == [speed, -speed] :
#         ball_speed[0] = ball_speed[0] + 1
#         ball_speed[1] = ball_speed[1] - 1
#         speed = speed + 1

#     if ball_speed == [-speed, -speed]:
#         ball_speed[0] = ball_speed[0] - 1
#         ball_speed[1] = ball_speed[1] - 1
#         speed = speed + 1

#     if ball_speed == [-speed, speed]:
#         ball_speed[0] = ball_speed[0] - 1
#         ball_speed[1] = ball_speed[1] + 1
#         speed = speed + 1

#     if ball_speed == [speed, speed]:
#         ball_speed[0] = ball_speed[0] + 1
#         ball_speed[1] = ball_speed[1] + 1
#         speed = speed + 1

    


def update() :

    global timer
    global score
    global ball_speed
    global speed

    new_x = ball.pos[0] + ball_speed[0]
    new_y = ball.pos[1] + ball_speed[1]
    ball.pos = [new_x, new_y]


    
    # if score == 150 :
    #     accelerate_ball()
    #     print(ball_speed)

    if ball.right > WIDTH or ball.left < 0 :
        invert_horizontal_speed()
        

    if ball.top < 0 :
        invert_vertical_speed()

    if ball.colliderect(player):
        invert_vertical_speed()
        sounds.sword.play()


    for brick in all_bricks :
        if ball.colliderect(brick):
            all_bricks.remove(brick)
            invert_vertical_speed()
            score = score + 1



    if timer > 0 :
        timer = timer - 1
        # print(timer)
    

        if timer == 0 :
            create_level(castle2)



            
    
def draw() :

    global timer
    global score
    global click
    

    screen.clear()

    screen.blit("background1.png", (0,0))

    
    



    if click == False :
        start_button.draw()

    if click == True :
        screen.draw.text("Destroy the castle !", center =(WIDTH/2, 100), fontname="dukeplus", fontsize=50, color="black")
        screen.draw.text("Score : " + str(score), center = (WIDTH/2 , 700), fontname="dukeplus", fontsize=50, color="grey")

        player.draw()

        ball.draw()


    for brick in all_bricks :
        brick.draw()








    if ball.bottom > HEIGHT :
        

        score = 0
        screen.clear()
        screen.draw.text("Game Over", center =(WIDTH/2, HEIGHT/2), fontname="dukeplus", fontsize=200, color="grey")
        

        if timer == 0 :
            timer = 3*60
            click = False
            screen.clear()

            

            if click == False :
                start_button.draw()
            

        



    if len(all_bricks) == 0 :
        screen.clear()
        screen.draw.text("You win !", center =(WIDTH/2, HEIGHT/2), fontname="dukeplus", fontsize=200, color="grey")

        if timer == 0 :
            timer = 3*60









#DERNIERE LIGNE ONLY
pgzrun.go()


