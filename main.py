import turtle
import os

wng = turtle.Screen()
wng.title("FIRST GAME PONG Alfian")
wng.bgcolor("black")
wng.setup(width=800,height=600)
wng.tracer(0)

# SCORE
score_a = 0
score_b = 0

# SISI Kiri ATAU SISI A

sisiA = turtle.Turtle()
sisiA.speed(0)
sisiA.shape("square")
sisiA.color("white")
sisiA.penup()
sisiA.goto(-350,0)
sisiA.shapesize(stretch_len=1, stretch_wid=5)


# SISI Kanan ATAU SISI B

sisiB = turtle.Turtle()
sisiB.speed(0)
sisiB.shape("square")
sisiB.color("white")
sisiB.penup()
sisiB.goto(350,0)
sisiB.shapesize(stretch_len=1, stretch_wid=5)

# Bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = -0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : 0 Player B : 0", align="center",font=("Courier",24,"normal"))

# fucntion SISI A
def sisiAup():
    y = sisiA.ycor()
    y += 20
    sisiA.sety(y)

def sisiAdown():
    y = sisiA.ycor()
    y -= 20
    sisiA.sety(y)

# Function SISIB

def sisiBup():
    y = sisiB.ycor()
    y += 20
    sisiB.sety(y)

def sisiBdown():
    y = sisiB.ycor()
    y -= 20
    sisiB.sety(y)



# Keyboard
wng.listen()
wng.onkeypress(sisiAup, "w")
wng.onkeypress(sisiAdown,"s")
wng.onkeypress(sisiBup,"Up")
wng.onkeypress(sisiBdown,"Down")



# MAIN GAME LOOP
while True:
    wng.update() #Setiap looping dijalankan maka windows akan selalu update
#     move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border Checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay pong.wav")

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay pong.wav")

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
        os.system("afplay pong.wav")

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_a, score_b), align="center",font=("Courier", 24, "normal"))
        os.system("afplay pong.wav")

    #paddle and ball colision

    if (ball.xcor()>340 and ball.xcor() <350) and (ball.ycor() < sisiB.ycor()+50 and ball.ycor()>sisiB.ycor() -50 ):
        ball.setx(340)
        ball.dx *=-1
        os.system("afplay pong.wav")

    if (ball.xcor()< -340 and ball.xcor() > -350) and (ball.ycor() < sisiA.ycor()+50 and ball.ycor()>sisiA.ycor() -50 ):
        ball.setx(-340)
        ball.dx *=-1
        os.system("afplay pong.wav")