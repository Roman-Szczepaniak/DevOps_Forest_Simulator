import random
from mapGenerator import MapGenerator
from terrain import Terrain

class FireGenerator:
    FIRE = 2
    BURNED = 3

    def __init__(self, map_gen):
        self.map_gen = map_gen
        self.map_grid = [row[:] for row in map_gen.get_map()]
        self.fire_start = None

    def start_fire(self):
        tree_positions = [(r, c) for r in range(len(self.map_grid))
                          for c in range(len(self.map_grid[0]))
                          if self.map_grid[r][c] == MapGenerator.TREE]
        
        if not tree_positions:
            print("Pas d'arbre pour démarrer un feu.")
            return

        self.fire_start = random.choice(tree_positions)
        r, c = self.fire_start
        self.map_grid[r][c] = self.FIRE

    def spread_fire(self):
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while True:
            new_fire = []
            for r in range(len(self.map_grid)):
                for c in range(len(self.map_grid[0])):
                    if self.map_grid[r][c] == self.FIRE:
                        self.map_grid[r][c] = self.BURNED
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if (0 <= nr < len(self.map_grid) and 0 <= nc < len(self.map_grid[0])
                                and self.map_grid[nr][nc] == MapGenerator.TREE):
                                new_fire.append((nr, nc))
            if not new_fire:
                break
            for r, c in new_fire:
                self.map_grid[r][c] = self.FIRE

    def print_fire_map(self):
        symbols = {
            MapGenerator.EMPTY: "🟫",
            MapGenerator.TREE: "🌳",
            self.FIRE: "🔥",
            self.BURNED: "⬛"
        }
        for row in self.map_grid:
            print(" ".join(symbols[cell] for cell in row))

        if self.fire_start:
            print(f"🔥 Feu déclenché à : {self.fire_start}")
