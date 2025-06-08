from src.node import Node
import random

class FireGenerator:
    def __init__(self, map_grid, origin=None):
        self.map = map_grid
        self.step = 0
        self.origin = origin

    def start_fire(self):
        if self.origin is None:
            trees = [(r, c) for r in range(self.map.height)
                            for c in range(self.map.width)
                            if self.map.grid[r][c].state == Node.TREE]

            if trees:
                r, c = random.choice(trees)
                self.origin = (r, c)
        else:
            r, c = self.origin

        if self.origin:
            self.map.grid[r][c].ignite(step=self.step)
            return self.origin

        return None

    def spread(self):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                    ( 0, -1),          ( 0, 1),
                    ( 1, -1), ( 1, 0), ( 1, 1)]


        while True:
            self.step += 1
            new_fires = []
            for r in range(self.map.height):
                for c in range(self.map.width):
                    node = self.map.grid[r][c]

                    if node.state == Node.FIRE and node.burn_start < self.step:
                        if (r, c) != self.origin:
                            node.burn_out()

                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if (0 <= nr < self.map.height and 0 <= nc < self.map.width):
                                neighbor = self.map.grid[nr][nc]
                                if neighbor.is_burnable():
                                    new_fires.append((nr, nc))

            if not new_fires:
                break

            for r, c in new_fires:
                self.map.grid[r][c].ignite(step=self.step)
