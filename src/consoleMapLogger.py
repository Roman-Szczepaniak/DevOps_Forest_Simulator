from MapLoggerI import MapLoggerI
from node import Node

class ConsoleMapLogger(MapLoggerI):
    SYMBOLS = {
        Node.EMPTY: "🟫",
        Node.TREE: "🌳",
        Node.FIRE: "🔥",
        Node.BURNED: "⬛"
    }

    def log(self, map_grid):
        for row in map_grid.grid:
            print(" ".join(self.SYMBOLS[node.state] for node in row))
