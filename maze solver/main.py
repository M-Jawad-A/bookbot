from tkinter import Tk, BOTH, Canvas


def main():
    win = Window(150, 350)
    point1 = Point(100, 221)
    point2 = Point(200, 240)
    line1 = Line(point1, point2, win)
    win.drawLine("Red", line1)

    cell = Cell(win)
    cell.draw(200, 250, 300, 280)
    cell1 = Cell(win)
    cell1.draw(250, 300, 350, 330)
    cell2 = Cell(win)
    cell2.draw(400, 450, 420, 480)

    cell1.drawMove(cell)
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
        self.window.create_line(self.beginningPoint.x, self.beginningPoint.y, self.endPoint.x, self.endPoint.y,
                                fill=colour, width=2)
        self.window.pack(fill=BOTH, expand=1)


class Cell:
    def __init__(self, window):
        self.hasLeftWall = True
        self.hasRightWall = True
        self.hasTopWall = True
        self.hasBottomWall = True
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.window = window

    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if self.hasTopWall:
            pointA = Point(x1, y1)
            pointB = Point(x2, y1)
            line = Line(pointA, pointB, self.window)
            self.window.drawLine("Black", line)
        if self.hasBottomWall:
            pointA = Point(x1, y2)
            pointB = Point(x2, y2)
            line = Line(pointA, pointB, self.window)
            self.window.drawLine("Black", line)
        if self.hasRightWall:
            pointA = Point(x2, y1)
            pointB = Point(x2, y2)
            line = Line(pointA, pointB, self.window)
            self.window.drawLine("Black", line)
        if self.hasLeftWall:
            pointA = Point(x1, y1)
            pointB = Point(x1, y2)
            line = Line(pointA, pointB, self.window)
            self.window.drawLine("Black", line)

    def drawMove(self, toCell, undo=False):
        newX1 = abs(self.x1 + self.x2) // 2
        newY1 = abs(self.y1 + self.y2) // 2
        newX2 = abs(toCell.x1 + toCell.x2) // 2
        newY2 = abs(toCell.y1 + toCell.y2) // 2
        pointA = Point(newX1, newY1)
        pointB = Point(newX2, newY2)
        line = Line(pointA, pointB, self.window)
        if not undo:
            self.window.drawLine("Red", line)
        else:
            self.window.drawLine("Gray", line)


if __name__ == '__main__':
    main()
