import tkinter as tk


class DrawMaze(tk.Frame):
    def __init__(self, master, maze: list, size_x, size_y, square_size=40):
        super().__init__(master)
        self.master = master
        self.master.title("Chessboard")
        self.master.geometry(f"{size_x * square_size}x{size_y * square_size}")

        self.size = (size_x, size_y)
        self.square_size = square_size

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
                square = tk.Canvas(self, width=self.square_size, height=self.square_size,
                                   bg=color, highlightthickness=0)
                square.grid(row=row, column=col)
