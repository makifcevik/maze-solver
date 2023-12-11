import tkinter as tk

SCREEN_SIZE = 600


class DrawMaze(tk.Frame):
    def __init__(self, master: tk.Frame, maze: list, size_x, size_y):
        super().__init__(master)
        self.square_size = (SCREEN_SIZE // size_x, SCREEN_SIZE // size_y)
        self.master = master
        self.master.title("Maze Solver")
        self.master.geometry(f"{size_x * self.square_size[0]}x{size_y * self.square_size[0]}")

        self.size = (size_x, size_y)

        self.squares = []  # Store references to canvas widgets

        self.create_maze(maze)
        self.pack()

    def create_maze(self, maze):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                if maze[row][col] == '1':
                    color = "black"
                elif maze[row][col] == 'A':
                    color = "red"
                elif maze[row][col] == 'B':
                    color = "blue"
                else:
                    color = "gray"
                square = tk.Canvas(self, width=self.square_size[0], height=self.square_size[1],
                                   bg=color, highlightthickness=0)
                square.grid(row=row, column=col)
                self.squares.append(square)

    def update_color(self, row, col, new_color):
        index = row * self.size[1] + col
        try:
            self.squares[index].config(bg=new_color)
        except IndexError:
            print("Invalid index")
