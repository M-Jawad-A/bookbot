from tkinter import Tk, BOTH, Canvas


def main():
    win = Window(150, 300)
    point1 = Point(200, 221)
    point2 = Point(200, 256)
    line1 = Line(point1, point2, win)
    win.drawLine("Red", line1)
    win.waitForClose()


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze")
        self.canvas = Canvas(self.root, bg="White", bd=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        '''a method to redraw the graphics in the window'''
        self.root.update_idletasks()
        self.root.update()

    def waitForClose(self):
        '''a method to redraw the window for as long as it is running'''
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        '''a method to close the window'''
        self.running = False

    def drawLine(self, colour, line):
        print("drawing line")
        drawnLine = Line(line.beginningPoint, line.endPoint, self.canvas)
        drawnLine.draw(colour)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, pointA, pointB, window):
        self.beginningPoint = pointA
        self.endPoint = pointB
        self.window = window

    def draw(self, colour):
        print("doing a draw line")
        self.window.create_line(self.beginningPoint.x, self.beginningPoint.y, self.endPoint.x, self.endPoint.y, fill=colour,
                           width=2)
        self.window.pack(fill=BOTH, expand=1)


if __name__ == '__main__':
    main()
