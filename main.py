from graphics import Window, Line, Point
from cell import Cell
from maze import Maze


def main():
    screen_width = 800
    screen_height = 600
    margin = 50
    num_rows = 12
    num_cols = 16
    cell_size_x = (screen_width - 2 * margin ) / num_cols
    cell_size_y = (screen_height - 2 * margin )/ num_rows

    
    window = Window(screen_width,screen_height)
    maze = Maze(margin ,margin ,num_rows, num_cols, cell_size_x, cell_size_y, window)
    
    window.wait_for_close()





main()