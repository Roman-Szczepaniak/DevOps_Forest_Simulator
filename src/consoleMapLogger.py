from src.IMapLogger import IMapLogger
from src.node import Node

class ConsoleMapLogger(IMapLogger):
    SYMBOLS = {
        Node.EMPTY: "🟫",
        Node.TREE: "🌳",
        Node.FIRE: "🔥",
        Node.BURNED: "⬛",
        Node.CUT: "✂️"
    }

    def log(self, map_grid):
        for row in map_grid.grid:
            symbols = []
            for node in row:
                if node.state == Node.FIRE:
                    symbols.append(self.SYMBOLS[node.state]) 
                else:
                    symbols.append(self.SYMBOLS[node.state])
            print(" ".join(symbols))
