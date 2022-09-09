from tkinter import Tk, BOTH, Canvas

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
