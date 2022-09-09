from graphics import Window, Line, Point

def main():
    win = Window(800,800)
    l = Line(Point(50,50), Point(500,500))
    win.draw_line(l, "black")
    win.wait_for_close()

main()