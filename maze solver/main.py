from tkinter import Tk, BOTH, Canvas


def main():
    win = Window(800, 600)
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


class Point:
    def __init__(self, x, y):
        self.x = x
        self. y = y


if __name__ == '__main__':
    main()
