import random
from cell import Cell
import time
class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):

        self.__cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        if seed:
            random.seed(seed)

        self.__create_cells()
        # time.sleep(100)
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

    def __create_cells(self):
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self.__cells.append(col_cells)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i,j)

    def __draw_cell(self, i, j):
        if self.__win is None:
            return

        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1,y1,x2,y2)

        self.__animate()

    def __animate(self):
        if self.__win is None:
            return

        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True

        while True:
            to_visit = []

            # left
            if i > 0 and not self.__cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # right
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            # up
            if j > 0 and not self.__cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            # down
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            # return if you have nowhere to go 
            if len(to_visit) == 0:
                self.__draw_cell(i,j)
                return
            
            # randomly pick direction to visit
            direction_index = random.randrange(len(to_visit))
            next_index = to_visit[direction_index]

            if next_index[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i+1][j].has_left_wall = False

            if next_index[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False

            if next_index[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False

            if next_index[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False

            self.__break_walls_r(next_index[0],next_index[1])
    
    def __reset_cells_visited(self):
        for col in self.__cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self,i,j):
        self.__animate()
        self.__cells[i][j].visited = True

        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True
        # left
        if i > 0 and not self.__cells[i][j].has_left_wall and not self.__cells[i - 1][j].visited:
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i - 1][j], True)
        # right
        if i < self.__num_cols - 1 and not self.__cells[i][j].has_right_wall and not self.__cells[i + 1][j].visited:
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i + 1][j], True)
        # up
        if j > 0 and not self.__cells[i][j].has_top_wall and not self.__cells[i][j - 1].visited:
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j - 1], True)
        # down
        if j < self.__num_rows - 1 and not self.__cells[i][j].has_bottom_wall and not self.__cells[i][j + 1].visited:
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j + 1], True)

        return False

