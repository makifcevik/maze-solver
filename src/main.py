import maze
import tkinter as tk
from draw import DrawMaze

window = tk.Tk()
maze = maze.Maze("../mazes/maze3.txt")
# maze.print()
draw = DrawMaze(window, maze.to_list(), maze.width, maze.height)
solution = maze.solve(frontier="s")
# print(solution)
solution_path = solution[0][1]
# explored_areas = list(solution[1])
# print(explored_areas)
for element in solution_path[:-1]:
    draw.update_color(element[0], element[1], "yellow")
    window.after(1000 // len(solution_path))
    window.update()
window.mainloop()
