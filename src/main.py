import maze

maze = maze.Maze("../mazes/maze1.txt")
maze.print()
solution = maze.solve()
print(solution)
