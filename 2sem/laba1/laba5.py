import sys


class Drawer(object):
    def __init__(self):
        self.canvas_size = 80
        self.canvas = [[' '] * self.canvas_size for _ in range(self.canvas_size)]
        self.brush = ' '

    def print_canvas(self):
        for row in self.canvas:
            print(''.join(row))

    def brush_inst(self, brush):
        self.brush = brush

    def draw_a_rectangle(self, x0, y0, x1, y1):
        self.draw_a_line(x0, y0, x1, y0)
        self.draw_a_line(x0, y1, x1, y1)
        self.draw_a_line(x0, y0, x0, y1)
        self.draw_a_line(x1, y0, x1, y1)

    def draw_a_filled_rectangle(self, x0, y0, x1, y1):
        for m in range(x0, x1 + 1):
            for n in range(y0, y1 + 1):
                self.canvas[m][n] = self.brush
        return self

    def draw_a_sprite(self, x0, y0, width, height, symbol):
        x1 = x0 + width + 1
        y1 = y0 + height + 1
        symbol.reverse()
        for i in range(x0, x1):
            for j in range(y0, y1):
                brush = symbol.pop()
                self.canvas[i][j] = brush

    def draw_a_line(self, x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0

        sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
        sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

        if dx < 0:
            dx = -dx
        if dy < 0:
            dy = -dy

        if dx > dy:
            pdx, pdy = sign_x, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sign_y
            es, el = dx, dy

        x, y = x0, y0

        error, t = el / 2, 0

        self.canvas[y][x] = self.brush

        while t < el:
            error -= es
            if error < 0:
                error += el
                x += sign_x
                y += sign_y
            else:
                x += pdx
                y += pdy
            t += 1
            self.canvas[y][x] = self.brush


my_drawing = Drawer()

for line in sys.stdin:
    line1 = line.rstrip('\n')
    new_line = line.split(' ')
    if line.startswith("brush"):
        my_drawing.brush_inst(new_line[1])
    elif line.startswith("rect"):
        my_drawing.draw_a_rectangle(int(new_line[1]), int(new_line[2]), int(new_line[3]), int(new_line[4]))
    elif line.startswith("fillRect"):
        my_drawing.draw_a_filled_rectangle(int(new_line[1]), int(new_line[2]), int(new_line[3]), int(new_line[4]))
    elif line.startswith("sprite"):
        symbol1 = new_line[5:]
        my_drawing.draw_a_sprite(int(new_line[1]), int(new_line[2]), int(new_line[3]), int(new_line[4]), symbol1)
    elif line.startswith("line"):
        my_drawing.draw_a_line(int(new_line[1]), int(new_line[2]), int(new_line[3]), int(new_line[4]))

my_drawing.print_canvas()
