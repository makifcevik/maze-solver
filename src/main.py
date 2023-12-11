import maze
import tkinter as tk
from draw import DrawMaze

window = tk.Tk()
maze = maze.Maze("../mazes/maze1.txt")
# maze.print()
draw = DrawMaze(window, maze.to_list(), maze.width, maze.height)
# solution = maze.solve()
# print(solution)
window.mainloop()
