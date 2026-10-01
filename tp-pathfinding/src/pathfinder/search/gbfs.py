from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

def manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    """Calculate the Manhattan distance between two grid points
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier (priority queue ordered by heuristic h(n)) with the root node
        frontier = PriorityQueueFrontier() 
        h_root = manhattan_distance(root.state, grid.end)
        frontier.add(root, priority=h_root)

        #Main loop
        while not frontier.is_empty():
            node = frontier.pop()

            #Objective test upon expanding the node
            if grid.objective_test(node.state):
                return Solution(node, reached)

            #Expand successors
            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)
                if successor not in reached:
                    cost = node.cost + grid.individual_cost(node.state, action)
                    reached[successor] = cost
                    child = Node("", state=successor, cost=cost, parent=node, action=action)

                    #calculate heuristic to the goal
                    h = manhattan_distance(successor, grid.end)
                    frontier.add(child, priority=h)
                    
        return NoSolution(reached)
