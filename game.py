import pygame
import time
import random

black = (0, 0, 0)
pygame.init()

red = (255, 0, 0)
gold = (231, 131, 123)
display = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Car Game")
carimg = pygame.image.load("hero.png")
bacimg = pygame.image.load("Road.jpg")
backgroundleft = pygame.image.load("left.png")
backgroundright = pygame.image.load("right.png")
car_width = 40
dag_width = 23


# -------------------------rastar sada dag---------------------------------
def dagcar(dag_startx, dag_starty, dag):
    global dag_come
    if dag == 0:
        dag_come = pygame.image.load("dag1.png")
    if dag == 1:
        dag_come = pygame.image.load("dag2.png")
    if dag == 2:
        dag_come = pygame.image.load("dag3.png")

    display.blit(dag_come, (dag_startx, dag_starty))

    # ---------------------------- bom and texi------------------------------------------


def policecar(police_startx, police_starty, police):  # define police function
    if police == 0:  # at 0 stage
        police_come = pygame.image.load("car2.png")  # police car2 come
    if police == 2:  # at 1 stage
        police_come = pygame.image.load("car3.png")  # police car3 come
    if police == 1:
        police_come = pygame.image.load("car1.png")  # police car1 come

    display.blit(police_come, (police_startx, police_starty))  # display the police car


def score_system(passed, score):
    font = pygame.font.SysFont(None, 26)
    text = font.render("Passed: " + str(passed), True, black)
    score = font.render("score :" + str(score), True, red)
    display.blit(text, (5, 50))
    display.blit(score, (5, 30))


def crash():
    message_display("Car Crashed")


def message_display(text):  # create function for message edit
    largetext = pygame.font.Font("freesansbold.ttf", 80)  # message in this style and the size will be 80
    textsurf, textrect = text_object(text, largetext)
    textrect.center = ((400), (300))
    display.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(2)  # after crashed 3 sec restart the game
    loop()


def text_object(text, font):  # display after crash the car
    textsurface = font.render(text, True, gold)  # display in this colour
    return textsurface, textsurface.get_rect()  # after that restart the game & ready to give some input


def background():
    display.blit(backgroundleft, (0, 0))
    display.blit(backgroundright, (700, 0))


def car(x, y):  # create car function
    display.blit(carimg, (x, y - 80))  # set position of car


def loop():
    global dag_starty, dag_startx, dag, passed
    x = 400
    y = 540
    x_change = 0
    y_change = 0
    policecar_speed = 7
    dagcar_speed = -7
    police = 0
    dag = 0
    dag_startx = 240
    dag_starty = -500
    police_startx = random.randrange(135, 690)  # police car ekdom prothomtar x position
    police_starty = random.randrange(-800, -100)  ## police car ekdom prothomtar y position
    police_width = 23  # police car width
    dag_width = 1
    police_height = 47  # police car height
    dag_height = 1

    ##### ------------------------- score and level funtion  start ------------------------
    passed=0
    level=0
    score=0


    bumped = False  # if game is not any problem to start
    while not bumped:  # game is start
        for event in pygame.event.get():  # if any input is given
            if event.type == pygame.QUIT:  # if quit input is given
                pygame.quit()
                quit()

                #  Key chapa suru

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5  # move right side +5
                if event.key == pygame.K_UP:
                    policecar_speed = 30
                    dagcar_speed = -32
                # if event.key == pygame.K_SPACE:
                #     dagcar_speed = -25
                #     policecar_speed = 15


                    #  Key chaira dia suru

            if event.type == pygame.KEYUP:
                x_change = 0
                y_change = 0
                # if event.key == pygame.K_SPACE:
                #     policecar_speed = 11
                #     dagcar_speed = -10
                if event.key == pygame.K_UP:
                    policecar_speed = 7
                    dagcar_speed = -7

        x += x_change
        y += y_change

        display.fill(black)
        # display.blit(bacimg, (0, 0))
        background()

        score_system(passed, score)

        police_starty -= (policecar_speed / 20)  # police car speed at y axis
        policecar(police_startx, police_starty, police)  # call police function
        police_starty += policecar_speed  # police car speed increse
        if x < 130 or x > 700 - car_width:  # if car goes out of this range
            bumped = False  # stop the game
            crash()  # call crash function
        if police_starty > 600:  # police car pass it without crashed
            police_starty = 0 - police_height  # police car uporer ( y er position) kotha theke nama shuru korbe se position
            police_startx = random.randrange(130, (
                        700 - car_width))  # police car pasher ( x er position) kotha theke nama shuru korbe se position
            police = random.randrange(0, 3)  # diffrent car come
            passed = passed + 1
            score = passed * 10

        if y < police_starty + police_height:  # if police car not pass
            if x > police_startx and x < police_startx + police_width or x + car_width > police_startx and x + car_width < police_startx + police_width:
                crash()  # crash the car

        dag_starty -= (dagcar_speed / 1)  # police car speed at y axis
        dagcar(dag_startx, dag_starty, dag)  # call police function
        car(x, y)
        if dag_starty > 600:  # police car pass it without crashed
            dag_starty = -600  # only one car is crossed
            dag_startx = 240
            dag = random.randrange(0, 2)  # diffrent car come
            bumped = False

        pygame.display.update()  # update the display


loop()  # call the loop function
pygame.quit()  # package is stop
quit()  # game is stop
