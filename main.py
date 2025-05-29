from graphics import Window, Line, Point
from cell import Cell


def main():
    window = Window(800,600)

    c1 = Cell(window)
    c1.has_bottom_wall = False
    c1.draw(200, 100, 400, 100)

    c2 = Cell(window)
    c2.has_left_wall = False
    c2.draw(200, 100, 200, 300)

    c3 = Cell(window)
    c3.has_top_wall = False
    c3.draw(200, 300, 400, 300)

    c4 = Cell(window)
    c4.has_right_wall = False
    c4.draw(400, 100, 400, 300)

    c5 = Cell(window)
    c5.has_bottom_wall = False
    c5.draw(500, 100, 700, 100)

    c6 = Cell(window)
    c6.has_left_wall = False
    c6.draw(500, 100, 500, 300)

    c7 = Cell(window)
    c7.has_top_wall = False
    c7.draw(500, 300, 700, 300)

    c8 = Cell(window)
    c8.has_right_wall = False
    c8.draw(700, 100, 700, 300)

    c1.draw_move(c5)

    window.wait_for_close()





main()