import turtle

turtle.color("red")
turtle.penup()# Поднимаем курсор
turtle.goto(125, 135)# Переходим по нужным координатам
turtle.pendown()# Опускаем курсор
turtle.right(45)
turtle.forward(70)

turtle.color("black")# Устанавливаем цвет черепашки
turtle.penup()# Поднимаем курсор
turtle.goto(0, -25)# Переходим по нужным координатам
turtle.pendown()# Опускаем курсор
turtle.circle(45)# Рисуем круг с радиусом 45



turtle.color("blue")
turtle.penup()
turtle.goto(145, 135)
turtle.right(225)
turtle.pendown()
turtle.forward(70)

turtle.left(90)
turtle.forward(70)

turtle.left(135) # Повернуть курсор влево на 135 градусов
turtle.forward(100)
turtle.done()
