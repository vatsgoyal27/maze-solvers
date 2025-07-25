from turtle import Turtle

class Mouse:
    def __init__(self, c):
        self.create_mouse()
        self.mouse_pos = [17,0]
        self.mouse.width(1)
        self.mouse.pencolor(c)
        self.mouse.width(5)

    def create_mouse(self):
        self.mouse = Turtle(shape='square')
        self.mouse.setheading(90)
        #self.mouse.shapesize(0.5, 0.5)
        self.mouse.hideturtle()
        self.mouse.penup()
        self.mouse.goto(30, 30)
        self.mouse.pendown()
        self.mouse.showturtle()
        self.mouse.speed(6)

    def draw_grid(self):
        self.mouse.hideturtle()
        self.mouse.speed(0)
        self.mouse.penup()
        self.mouse.pencolor("black")
        self.mouse.width(1)

        # Draw vertical lines
        for x in range(20, 381, 20):
            self.mouse.goto(x, 20)
            self.mouse.setheading(90)
            self.mouse.pendown()
            self.mouse.forward(360)
            self.mouse.penup()

        # Draw horizontal lines
        for y in range(20, 381, 20):
            self.mouse.goto(20, y)
            self.mouse.setheading(0)
            self.mouse.pendown()
            self.mouse.forward(360)
            self.mouse.penup()

    def draw_walls(self, grid):
        self.mouse.hideturtle()
        self.mouse.speed(0)
        self.mouse.penup()
        self.mouse.pencolor("red")
        self.mouse.width(2)

        cell_size = 20

        for row in range(18):
            for col in range(18):
                x, y, walls = grid[row][col]

                if 'n' in walls:
                    self.mouse.goto(x - cell_size // 2, y + cell_size // 2)
                    self.mouse.setheading(0)
                    self.mouse.pendown()
                    self.mouse.forward(cell_size)
                    self.mouse.penup()

                if 'e' in walls:
                    self.mouse.goto(x + cell_size // 2, y + cell_size // 2)
                    self.mouse.setheading(-90)
                    self.mouse.pendown()
                    self.mouse.forward(cell_size)
                    self.mouse.penup()

                if 's' in walls:
                    self.mouse.goto(x + cell_size // 2, y - cell_size // 2)
                    self.mouse.setheading(180)
                    self.mouse.pendown()
                    self.mouse.forward(cell_size)
                    self.mouse.penup()

                if 'w' in walls:
                    self.mouse.goto(x - cell_size // 2, y - cell_size // 2)
                    self.mouse.setheading(90)
                    self.mouse.pendown()
                    self.mouse.forward(cell_size)
                    self.mouse.penup()

    def delete(self):
        self.mouse.penup()
        self.mouse.hideturtle()

    def f(self):
        if self.mouse.heading() == 90:
            self.mouse_pos[0] -= 1
        elif self.mouse.heading() == 0:
            self.mouse_pos[1] += 1
        elif self.mouse.heading() == 180:
            self.mouse_pos[1] -= 1
        elif self.mouse.heading() == 270:
            self.mouse_pos[0] += 1
        self.mouse.forward(20)

    def l(self):
        self.mouse.setheading((self.mouse.heading() + 90) % 360)

    def r(self):
        self.mouse.setheading((self.mouse.heading() - 90) % 360)

    def move_actual(self, to):
        nx, ny = to[0], to[1]
        cx, cy = self.mouse_pos[0], self.mouse_pos[1]
        if nx< cx:
            self.mouse.setheading(90)
            self.f()
        if nx> cx:
            self.mouse.setheading(270)
            self.f()
        if ny < cy:
            self.mouse.setheading(180)
            self.f()
        if ny > cy:
            self.mouse.setheading(0)
            self.f()

