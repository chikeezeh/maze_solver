from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.left_wall = True
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.right_wall = True
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.bottom_wall = True
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.draw(300, 300, 500, 500)

    win.wait_for_close()


main()