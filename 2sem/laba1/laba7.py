from tkinter import *
from enum import Enum
import time
import random


class PythonSnake:
    def __init__(self, window, canv_x, canv_y, canv_width, canv_height):
        self.__vector = self.Const.RIGHT.value
        self.body = []
        self.__started = 1
        self.__spped = 10
        self.__window = window
        self.__canv_x = canv_x
        self.__canv_y = canv_y
        self.canv_width = canv_width
        self.canv_height = canv_height
        self.__snake_x = self.canv_width // 2
        self.__snake_y = self.canv_height // 2
        self.canv = Canvas(self.__window, width=self.canv_width, height=self.canv_height,
                           bg=self.Const.CANVAS_BGCOLOR.value)
        self.canv.place(x=self.__canv_x, y=self.__canv_y)
        self.create_head_food()

        self.__window.bind('<Right>', self.right)
        self.__window.bind('<Down>', self.down)
        self.__window.bind('<Left>', self.left)
        self.__window.bind('<Up>', self.up)

    class Const(Enum):
        RIGHT = 1
        DOWN = 2
        LEFT = 3
        UP = 4
        SNAKE_HCOLOR = 'red'
        SNAKE_BCOLOR = 'green'
        CANVAS_BGCOLOR = '#bfcff1'
        SNAKE_THICKNESS = 11
        FOOD_THICKNESS = 15
        FOOD_COLOR = '#aced95'
        EXPLOSIVE = 15
        EXPLOSIVE_BORD = 10
        EXPLOSIVE_BCOLOR = '#ff9999'

    def right(self, event):
        pass

    def down(self, event):
        self.__vector = self.Const.DOWN.value

    def left(self, event):
        self.__vector = self.Const.LEFT.value

    def up(self, event):
        self.__vector = self.Const.UP.value

    def speed_key(self, event):
        if event.keysym == 'KP_Add' or event.keysym == 'plus':
            self.speed('+')
        elif event.keysym == 'KP_Subtract' or event.keysym == 'minus':
            self.speed('-')

    def create_head_food(self):
        rand_vect = random.randint(1, 4)
        if rand_vect == 1:
            self.__vector = self.Const.RIGHT.value
        elif rand_vect == 2:
            self.__vector = self.Const.DOWN.value
        elif rand_vect == 3:
            self.__vector = self.Const.LEFT.value
        else:
            self.__vector = self.Const.UP.value
        self.head = self.ElementSquare(self, self.__snake_x, self.__snake_y, self.Const.SNAKE_THICKNESS.value,
                                        self.Const.SNAKE_HCOLOR.value)
        self.food.add(self)
        self.body.append({'id': self.head.draw(), 'x': self.__snake_x, 'y': self.__snake_y})
        self.step('add')
        self.step('add')
        self.step('add')
        self.step('add')

    def speed(self, way):
        if way == '+' and self.__spped > 1:
            self.__spped -= 1
        elif way == '-' and self.__spped < 20:
            self.__spped += 1

    def reload(self):
        self.quit = 'n'
        self.__started = 1
        self.__spped = 10
        self.canv.delete('all')
        del self.body
        self.body = []
        self.create_head_food()
        self.start()

    def move(self, event):
        if self.quit != 'n':
            self.start()

    def start(self):
        if self.__started == 1:
            self.quit = 'n'
            i = 0
            add = 'del'
            while i == 0:
                self.step(add)
                if self.food.eat(self) == 1:
                    add = 'add'
                    self.speed('+')
                elif add == 'add':
                    add = 'del'
                if self.bump_wall() == 'the end':
                    break
                if self.bump_body() == 'the end':
                    break
                for x in range(1, (self.__spped + 1)):
                    time.sleep(0.05)
                    self.__window.update()
                    if self.quit == 'y':
                        i = 1
                        break

    def bump_wall(self):
        __head_x = self.body[-1]['x']
        __head_y = self.body[-1]['y']
        if ((__head_x < ((self.Const.SNAKE_THICKNESS.value // 2) + 1))
                or (__head_y < ((self.Const.SNAKE_THICKNESS.value // 2) + 1))
                or (__head_x > (self.canv_width - (self.Const.SNAKE_THICKNESS.value // 2) + 1))
                or (__head_y > (self.canv_height - (self.Const.SNAKE_THICKNESS.value // 2) + 1))):
            self.explosive()
            return 'the end'
        else:
            return 0

    def bump_body(self):
        __head_x = self.body[-1]['x']
        __head_y = self.body[-1]['y']
        bump = 0
        for i in range(0, (len(self.body) - 1)):
            if (__head_x == self.body[i]['x']) and (__head_y == self.body[i]['y']):
                self.explosive()
                bump = 'the end'
        return bump

    def explosive(self):
        self.__started = 0
        self.canv.create_oval((self.body[-1]['x'] - self.Const.EXPLOSIVE.value),
                              (self.body[-1]['y'] - self.Const.EXPLOSIVE.value),
                              (self.body[-1]['x'] + self.Const.EXPLOSIVE.value),
                              (self.body[-1]['y'] + self.Const.EXPLOSIVE.value),
                              fill=self.Const.EXPLOSIVE_BCOLOR.value,
                              outline=self.Const.EXPLOSIVE_CCOLOR.value,
                              width=self.Const.EXPLOSIVE_BORD.value)

    def step(self, add):
        global deltax, deltay
        if self.__vector == self.Const.RIGHT.value:
            deltax = self.Const.SNAKE_THICKNESS.value
            deltay = 0
        elif self.__vector == self.Const.DOWN.value:
            deltax = 0
            deltay = self.Const.SNAKE_THICKNESS.value
        elif self.__vector == self.Const.LEFT.value:
            deltax = -self.Const.SNAKE_THICKNESS.value
            deltay = 0
        elif self.__vector == self.Const.UP.value:
            deltax = 0
            deltay = -self.Const.SNAKE_THICKNESS.value
        self.head.x += deltax
        self.head.y += deltay
        self.head = self.ElementSquare(self, self.head.x, self.head.y, self.Const.SNAKE_THICKNESS.value,
                                        self.Const.SNAKE_HCOLOR.value)
        self.body.append({'id': self.head.draw(), 'x': self.head.x, 'y': self.head.y})  # Создал новую голову
        self.canv.itemconfig(self.body[-2]['id'], fill=self.Const.SNAKE_BCOLOR.value)  # Перекрасил старую голову в тело
        if add != 'add':
            self.canv.delete(self.body[0]['id'])
            self.body.pop(0)

    class food:
        def add(self):
            self.food.x = random.randint(self.Const.FOOD_THICKNESS.value // 2,
                                         self.canv_width - self.Const.FOOD_THICKNESS.value // 2)
            self.food.y = random.randint(self.Const.FOOD_THICKNESS.value // 2,
                                         self.canv_height - self.Const.FOOD_THICKNESS.value // 2)
            self.food.body = self.ElementSquare(self, self.food.x, self.food.y, self.Const.FOOD_THICKNESS.value,
                                                 self.Const.FOOD_COLOR.value)
            self.food.id = self.food.body.draw()

        def eat(self):
            head_x = self.body[-1]['x']
            head_y = self.body[-1]['y']
            eat = 0
            if ((head_x + self.Const.SNAKE_THICKNESS.value // 2 >
                 (self.food.x - self.Const.FOOD_THICKNESS.value // 2))
                    and (head_x - self.Const.SNAKE_THICKNESS.value // 2 <
                         (self.food.x + self.Const.FOOD_THICKNESS.value // 2))
                    and (head_y + self.Const.SNAKE_THICKNESS.value // 2 >
                         (self.food.y - self.Const.FOOD_THICKNESS.value // 2))
                    and (head_y - self.Const.SNAKE_THICKNESS.value // 2 <
                         (self.food.y + self.Const.FOOD_THICKNESS.value // 2))):
                self.canv.delete(self.food.id)
                self.food.add(self)
                eat = 1
            return eat

    class ElementSquare:
        def __init__(self, self_glob, x, y, d, color):
            self.self_glob = self_glob
            self.x = x
            self.y = y
            self.d = d
            self.color = color
            if (self.d % 2) == 0:
                self.d += 1

        def draw(self):
            x = self.x - (self.d // 2)
            y = self.y - (self.d // 2)
            return self.self_glob.canv.create_rectangle(x, y, x + self.d, y + self.d, fill=self.color, width=2)


def main():

    root = Tk()
    root.title('Змейка :)')
    root.geometry('800x600+150+150')

    snake = PythonSnake(root, 30, 100, 740, 470)
    snake.start()

    root.mainloop()


if __name__ == '__main__':
    main()
