from tkinter import Tk, BOTH, Canvas
from turtle import width

class Window:
    """
    Create a window that once the program runs we can draw on it.
    """
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Super Maze Solver")
        self.__canvas = Canvas(self.__root, bg="yellow", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW",self.close)

    def redraw(self):
        """"
        function to tell the window to redraw itself
        """
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        """
        This method should set the data member we created to track 
        the "running" state of the window to True. Next, it should 
        call self.redraw() over and over as long as the running state remains True.
        """
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")
    
    def close(self):
        self.__running = False
    
    def draw_line(self, line, fill_color="blue"):
        line.draw(self.__canvas, fill_color)

class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Line:

    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color="purple"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill = fill_color, width = 2
        )