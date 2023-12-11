from frontier import Node, StackFrontier, QueueFrontier


class Maze:
    def __init__(self, filename):
        with open(filename, mode="r") as file:
            self.rows = file.readlines()

        # determine the width and the height
        self.height = len(self.rows)
        self.width = max(len(row.strip()) for row in self.rows)

        self.solution = None
        self.walls = []
        self.start = None
        self.end = None

        # keep track of how many nodes explored
        self.num_of_explored = 0
        self.explored = set()

        self.construct_maze()

    def to_list(self):
        return [row.strip("\n").strip() for row in self.rows]

    def construct_maze(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if self.rows[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif self.rows[i][j] == "B":
                        self.end = (i, j)
                        row.append(False)
                    elif self.rows[i][j] == "0":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    print("An index error occurred")
                    row.append(False)

            self.walls.append(row)

    def detect_actions(self, state):
        row, col = state

        actions = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("right", (row, col + 1)),
            ("left", (row, col - 1))
        ]

        valid_actions = []
        for action, (r, c) in actions:
            try:
                if not self.walls[r][c]:
                    valid_actions.append((action, (r, c)))
            except IndexError:
                continue
        return valid_actions

    def solve(self, frontier="s"):
        # Initialize the start
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier() if frontier == "s" else QueueFrontier()
        # frontier = QueueFrontier()
        frontier.add(start)

        # loop till a solution is found
        while True:
            if frontier.is_empty():
                raise Exception("No solution found!")

            node = frontier.remove()
            self.num_of_explored += 1

            # solution found
            if node.state == self.end:
                actions = []
                cells = []

                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return self.solution, self.explored, len(self.solution[1]), self.num_of_explored

            self.explored.add(node.state)

            for action, state in self.detect_actions(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

    def print(self):
        for row in self.rows:
            print(row.strip("\n"))
        print(f"height: {self.height}\nwidth: {self.width}")
