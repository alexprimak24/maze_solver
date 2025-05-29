from graphics import Window, Line, Point


def main():
    window = Window(800,600)
    l = Line(Point(0, 50), Point(800, 50))
    window.draw_line(l, "black")
    window.wait_for_close()

main()