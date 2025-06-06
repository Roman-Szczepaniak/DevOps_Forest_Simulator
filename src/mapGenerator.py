from node import Node
import random

class MapGenerator:
    def __init__(self, width, height, percentage_of_trees):
        self.width = width
        self.height = height
        self.percentage_of_trees = percentage_of_trees
        self.grid = []

    def generate(self):
        self.grid = []
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                if random.randint(1, 100) <= self.percentage_of_trees:
                    row.append(Node(Node.TREE))
                else:
                    row.append(Node(Node.EMPTY))
            self.grid.append(row)

    def get_node(self, r, c):
        return self.grid[r][c]

    def nodes(self):
        for row in self.grid:
            for node in row:
                yield node
