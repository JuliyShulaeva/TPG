import turtle

turtle.reset()
turtle.speed(10000)


def TRI(x1, y1, x2, y2, x3, y3, N):
    if N > 0:
        x12 = (x1 + x2) // 2
        y12 = (y1 + y2) // 2
        x23 = (x2 + x3) // 2
        y23 = (y2 + y3) // 2
        x31 = (x3 + x1) // 2
        y31 = (y3 + y1) // 2
        turtle.pu()
        turtle.goto(x31, y31)
        turtle.pd()
        turtle.goto(x12, y12)
        turtle.goto(x23, y23)
        turtle.goto(x31, y31)
        TRI(x1, y1, x12, y12, x31, y31, N - 1);
        TRI(x2, y2, x12, y12, x23, y23, N - 1);
        TRI(x3, y3, x31, y31, x23, y23, N - 1)


x1 = 20
y1 = -200
x2 = 339
y2 = 279
x3 = -300
y3 = 279
n = 4
turtle.pu()
turtle.goto(x1, y1)
turtle.pd()
turtle.goto(x2, y2)
turtle.goto(x3, y3)
turtle.goto(x1, y1)
TRI(x1, y1, x2, y2, x3, y3, n);
turtle.exitonclick()