from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        # Apply objective test
        if grid.objective_test(root.state):
            return Solution(root, expanded)

        # Initialize frontier with the root node
        frontier = StackFrontier()
        frontier.add(root)

        while not frontier.is_empty():
            node = frontier.remove()
        
            for action in grid.actions(node.state):
                successor = grid.result(node.state, action)
                node_s = Node(successor, node, action, node.cost +grid.individual_cost(node.state, action))


                #if not hay_ciclos(s'n):
                    #if grid.objective_test(successor): 
                        #return Solution(node_s)
                    #frontier.add(node_s)
                    #expanded[node_s.state] = True



   

        return NoSolution(expanded)
