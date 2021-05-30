import tkinter as tk
import turtle
import time
import random
from PIL import ImageTk, Image
import pygame as pg
from pygame import mixer

delay = 0.1
speed = 10   #global speed

# set up the music
mixer.init()   #this going to let us play music
sound1 = 'C:/Users/user/PycharmProjects/j.a.r.v.i.s/song1.mp3'
sound2 = 'C:/Users/user/PycharmProjects/j.a.r.v.i.s/song2.mp3'
queue = [sound1, sound2]
song_index = 0
mixer.music.load(queue[song_index])
mixer.music.play()

pg.init()
MUSIC_ENDED = pg.USEREVENT
pg.mixer.music.set_endevent(MUSIC_ENDED)

# ----------------------Set up the screen------------------------------------------
root = tk.Tk()  #instance of tkinter
root.title("Snake Game")  #give title
root.state('zoomed')   #so that we expand window full

spaceImage1 = Image.open('C:\\Users\\user\\PycharmProjects\\j.a.r.v.i.s\\day.jpg')
spaceImage1 = spaceImage1.resize((1280, 720), Image.ANTIALIAS)
resized1 = ImageTk.PhotoImage(spaceImage1)  #resized image

spaceImage2 = Image.open('C:\\Users\\user\\PycharmProjects\\j.a.r.v.i.s\\night.jpg')
spaceImage2 = spaceImage2.resize((1280, 720), Image.ANTIALIAS)
resized2 = ImageTk.PhotoImage(spaceImage2)

background_label = tk.Label(root, image=resized1)    #put the image in the background
background_label.place(x=0, y=0)            #place it in on window for center x and y is 0

#for top tab
topFrame = tk.Frame(root, background='white') #frame is used to hold the widgets
topFrame.pack(fill='x')  #pack is used for organised the widgets in blocks before placing in parent widget

#for write the level text in top tab
levelText = tk.Label(topFrame, text='Level ', font=('bangers', 18, 'bold'), foreground='#00cca3', bg='white')
levelText.pack(side='left')

#for write the which level is it
levelDigit = tk.Label(topFrame, text='0', font=('bangers', 18, 'bold'), foreground='#00cca3', bg='white')
levelDigit.pack(side='left')

#score text
scoreText = tk.Label(topFrame, text='Score ', font=('bangers', 18, 'bold'), foreground='#00cca3', bg='white')
scoreText.pack(side='left')

#how much score
scoreDigit = tk.Label(topFrame, text='0', font=('bangers', 18, 'bold'), foreground='#00cca3', bg='white')
scoreDigit.pack(side='left')

#total highscore
highScoreDigit = tk.Label(topFrame, text='0', font=('bangers', 18, 'bold'), foreground='#00cca3', bg='white')
highScoreDigit.pack(side='right')

#high score text
highScoreText = tk.Label(topFrame, text=' High Score ', font=('bangers', 18, 'bold'), foreground='#00cca3', bg='white')
highScoreText.pack(side='right')

#top level
topLevelDigit = tk.Label(topFrame, text='0', font=('bangers', 18, 'bold'), foreground='#00cca3', bg='white')
topLevelDigit.pack(side='right')

#top level text
topLevelText = tk.Label(topFrame, text='Top Level ', font=('bangers', 18, 'bold'), foreground='#00cca3', bg='white')
topLevelText.pack(side='right')


#-----------------create a canvas-----------------------
#here in this canva we play the game.
canvas = tk.Canvas(root, height=600, width=640)

#create a turtle screen
turtle_screen = turtle.TurtleScreen(canvas)   #we want to loated this turtle screen in our canva
turtle_screen.bgcolor('#25258e')   #for color the turtle screen

canvas.pack(pady=10)  #to create a sepration of canva with the background window on top

turtle_screen.tracer(0)  # turns off window animation on the screen

# -----------------------------Snake head--------------------
head = turtle.RawTurtle(turtle_screen)
head.speed(0)               #speed of snake
head.shape('circle')          #give a shape to head of snake
head.color('white')             #color of head
head.penup()        #used for drawing so if we don't use penup the snake is gonna leave a trail of lines whereever we move it to.
head.goto(0, 0)  # by default we already at 0,0 but we use this for good practice
head.direction = 'stop'  # dictates the direction of the snake at the beginning of game
# you can use 'stop' as well

# Snake food
food = turtle.RawTurtle(turtle_screen)
food.speed(0)
food.shape('square')
food.color('#4d94ff')
food.penup()
food.goto(0, 100)

segments = []


# -----------functions to control the moves---------------
def move_up():
    if head.direction != 'down':
        head.direction = 'up'


def move_down():
    if head.direction != 'up':
        head.direction = 'down'


def move_left():
    if head.direction != 'right':
        head.direction = 'left'


def move_right():
    if head.direction != 'left':
        head.direction = 'right'

#control the speed with moves
def move():
    global speed
    if head.direction == 'up':
        y = head.ycor()  #return the turtle's y  coordinate of the current position of turtle
        head.sety(y + speed) #it set the y cordinate and remain unchanged the x cordinate

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - speed)

    if head.direction == 'left':
        x = head.xcor()   #return the turtle's x  coordinate of the current position of turtle
        head.setx(x - speed) #it set the x cordinate and remain unchanged the y cordinate

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + speed)


def spaceTheme1():
    background_label.config(image=resized1)
    turtle_screen.bgcolor('#325432')  # green
    scoreText.config(foreground='#00cca3')
    scoreDigit.config(foreground='#00cca3')
    highScoreDigit.config(foreground='#00cca3')
    highScoreText.config(foreground='#00cca3')
    levelDigit.config(foreground='#00cca3')
    levelText.config(foreground='#00cca3')
    topLevelDigit.config(foreground='#00cca3')
    topLevelText.config(foreground='#00cca3')
    head.color('white')


def spaceTheme2():
    background_label.config(image=resized2)
    turtle_screen.bgcolor('#3d0099')  #blue purple type
    scoreText.config(foreground='#8533ff')
    scoreDigit.config(foreground='#8533ff')
    highScoreDigit.config(foreground='#8533ff')
    highScoreText.config(foreground='#8533ff')
    levelDigit.config(foreground='#8533ff')
    levelText.config(foreground='#8533ff')
    topLevelDigit.config(foreground='#8533ff')
    topLevelText.config(foreground='#8533ff')
    head.color('white')


def on_closing():
    mixer.music.stop()
    pg.event.clear()
    root.destroy()


root.protocol('WM_DELETE_WINDOW', on_closing)

# Keyboard bindings
turtle_screen.listen()
turtle_screen.onkeypress(move_up, 'Up')
turtle_screen.onkeypress(move_down, 'Down')
turtle_screen.onkeypress(move_left, 'Left')
turtle_screen.onkeypress(move_right, 'Right')



# Main game loop
def playsnake():
    global speed
    global song_index
    highScore = 0
    topLevel = 0
    level = 0
    score = 0
    start = False
    while True:

        turtle_screen.update()  # turns on window animation on the screen

        # is start is True increment score by 10 and update scoreDigit Label to the score
        if start == True:
            score += 10
            scoreDigit.config(text=score)

        # check for collision with the border
        if head.xcor() > 310 or head.xcor() < -310 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # update the highest score
            score -= 10
            if score > highScore:
                highScore = score
                highScoreDigit.config(text=highScore)  #write the highscore after the high score text

            if level > topLevel:
                topLevel = level
                topLevelDigit.config(text=topLevel)  #same for level

            # clear the segments list.... reset score,scoreDigit,level,levelDigit,speed,start
            segments.clear()
            score = 0
            scoreDigit.config(text=score)
            level = 0
            levelDigit.config(text=level)
            speed = 10
            start = False
            spaceTheme1()

        if head.distance(food) < 30:  # distance is a built in function to measure distance between two turtles
            # its < 20 because each basic turtle shape is 20x20 pixels
            # that means the center of one pixel to the outer edge is 10
            # and 10 + 10 = 20
            start = True
            # move the food to a random spot
            x = random.randint(-310, 310)  # from -310 to 310 any random number is given to x
            y = random.randint(-290, 290)  # from -290 to 290 any random number is given to y
            food.goto(x, y)

            # Add a segment .. If we are in this if statement, obviously we touched the food
            # hence, we create a new triangle
            new_segment = turtle.RawTurtle(turtle_screen)
            new_segment.speed(0)
            new_segment.shape('triangle')
            new_segment.color('#66ffe0')
            new_segment.penup()
            segments.append(new_segment)

            # increase level and speed after food is eaten
            speed += 1
            level += 1
            levelDigit.config(text=level)
            if level >= 20: #if level is greater then 20 then it goes to next theme
                spaceTheme2()
                for i in range(0, len(segments)):
                    s = segments[i]
                    s.color('#8533ff')

                    # move the end segments first in reverse order
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        # move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        # check for head collision with the body
        for segment in segments:  # we check each segment
            if segment.distance(head) < 10:
                time.sleep(1)  # we sleep
                head.goto(0, 0)  # go back to the center
                head.direction = 'stop'  # stop moving

                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

                # update the highest score
                score -= 10
                if score > highScore:
                    highScore = score
                    highScoreDigit.config(text=highScore)

                if level > topLevel:
                    topLevel = level
                    topLevelDigit.config(text=topLevel)

                # Clear the segments list
                segments.clear()
                score = 0
                scoreDigit.config(text=score)
                level = 0
                levelDigit.config(text=level)
                speed = 10
                start = False
                spaceImage1()

        # event checking if music is done playing
        for event in pg.event.get():
            if event.type == MUSIC_ENDED:
                song_index += 1
                if song_index >= len(queue) - 1:
                    song_index = 0
                    mixer.music.load(queue[song_index])
                    mixer.music.play()
                else:
                    mixer.music.load(queue[song_index])
                    mixer.music.play()

        time.sleep(delay)  # we want to delay how fast this loop is going so we can see the 'head' move
playsnake()
root.mainloop()