from search import util

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.
    """
    stack = util.Stack()
    visited = set()
    stack.push((problem.getStartState(), []))

    while not stack.isEmpty():
        current_state, actions = stack.pop()

        if problem.isGoalState(current_state):
            return actions

        if current_state not in visited:
            visited.add(current_state)
            successors = problem.getSuccessors(current_state)
            for successor, action, _ in successors:
                if successor not in visited:
                    stack.push((successor, actions + [action]))

    return False

def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    queue = util.Queue()
    visited = set()
    queue.push((problem.getStartState(), [], 0))

    while not queue.isEmpty():
        current_state, actions, cost = queue.pop()

        if problem.isGoalState(current_state):
            return actions

        if current_state not in visited:
            visited.add(current_state)
            successors = problem.getSuccessors(current_state)
            for successor, action, step_cost in successors:
                total_cost = cost + step_cost
                queue.push((successor, actions + [action], total_cost))

    return False

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the path that has the lowest combined cost and heuristic first.
    """
    paths = util.PriorityQueue()
    paths.push((problem.getStartState(), []), 0)
    visited = set()

    while not paths.isEmpty():
        (current_state, actions) = paths.pop()

        if problem.isGoalState(current_state):
            return actions

        if current_state in visited:
            continue

        visited.add(current_state)

        for successor, action, cost in problem.getSuccessors(current_state):
            if successor not in visited:
                paths.push(
                    (successor, actions + [action]),
                    cost + heuristic(successor, problem),
                )

    return False

class GridWorldSearchProblem:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal

    def getStartState(self):
        return self.start

    def isGoalState(self, state):
        return state == self.goal

    def getSuccessors(self, state):
        successors = []
        x, y = state
        if x > 0 and self.grid[x-1][y] != '#':
            successors.append(((x-1, y), 'left', 1))
        if x < len(self.grid)-1 and self.grid[x+1][y] != '#':
            successors.append(((x+1, y), 'right', 1))
        if y > 0 and self.grid[x][y-1] != '#':
            successors.append(((x, y-1), 'up', 1))
        if y < len(self.grid[0])-1 and self.grid[x][y+1] != '#':
            successors.append(((x, y+1), 'down', 1))
        return successors

# Define a grid world problem
problem = GridWorldSearchProblem([
    [' ', ' ', ' ', ' '],
    [' ', '#', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'G']
], (0, 0), (3, 3))

# Perform depth first search
actions = depthFirstSearch(problem)

# Print the actions taken to reach the goal state
print(actions)

# Perform breadth first search
actions = breadthFirstSearch(problem)

# Print the actions taken to reach the goal state
print(actions)

# Perform A* search
actions = aStarSearch(problem)

# Print the actions taken to reach the goal state
print(actions)
