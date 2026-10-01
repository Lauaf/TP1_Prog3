from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node
from .gbfs import manhattan_distance


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

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

        # Initialize frontier (priority queue ordered by f(n) = g(n) + h(n)) with the root node
        frontier = PriorityQueueFrontier()
        frontier.add(root, priority=root.cost + manhattan_distance(root.state, grid.end))

        # Main loop
        while not frontier.is_empty():
            # Pop the node with the lowest f(n) from the frontier
            node = frontier.pop()

            # Skip the node if a cheaper path to its state was found after it was added
            if node.cost > reached[node.state]:
                continue

            # Check if the goal state is reached
            if grid.objective_test(node.state):
                return Solution(node, reached)

            # Expand successors
            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)
                new_cost = node.cost + grid.individual_cost(node.state, action)

                # Add the successor to the frontier if it has not been reached or if a lower cost path is found
                if successor not in reached or new_cost < reached[successor]:
                    reached[successor] = new_cost
                    child = Node("", state=successor, cost=new_cost, parent=node, action=action)

                    # Priority is the path cost plus the heuristic to the goal
                    f = new_cost + manhattan_distance(successor, grid.end)
                    frontier.add(child, priority=f)

        return NoSolution(reached)
