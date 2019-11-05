import turtle

"""庆祖国70周年"""

# 国旗
turtle.up()
turtle.goto(-200, 200)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("red")
turtle.pencolor("red")
for i in range(2):
    turtle.forward(280)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
turtle.end_fill()

turtle.up()
turtle.goto(-170, 145)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
for x in range(5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()

turtle.up()
turtle.goto(-100, 180)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
for x in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()

turtle.up()
turtle.goto(-70, 160)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
for x in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()

turtle.up()
turtle.goto(-70, 120)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
for x in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()

turtle.up()
turtle.goto(-100, 100)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
for x in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()
turtle.hideturtle()

# 70
turtle.pensize(5)
turtle.color('red')
turtle.penup()
turtle.goto(-400, -10)
turtle.pendown()
turtle.speed(9)
turtle.fd(50)
turtle.right(90)
turtle.fd(100)
turtle.left(90)
turtle.penup()
turtle.fd(50)
turtle.goto(-300, -10)
turtle.pendown()
turtle.fd(50)
turtle.right(90)
turtle.fd(100)
turtle.right(90)
turtle.fd(50)
turtle.right(90)
turtle.fd(100)
turtle.penup()

# 周年快乐
pensize = 10
turtle.pensize(pensize)
turtle.pencolor("#FF0000")
turtle.goto(-200, -120)
turtle.penup()
turtle.speed(9)
turtle.write("周年快乐", move=False, align='left', font=("宋体", 70, 'normal'))

turtle.done()
