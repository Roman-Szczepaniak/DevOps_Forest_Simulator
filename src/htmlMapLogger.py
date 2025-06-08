from src.IMapLogger import IMapLogger
from src.node import Node

class HtmlMapLogger(IMapLogger):
    SYMBOLS = {
        Node.EMPTY: "🟫",
        Node.TREE: "🌳",
        Node.FIRE: "🔥",
        Node.BURNED: "⬛",
        Node.CUT: "✂️"
    }

    def __init__(self, output_file="map.html"):
        self.output_file = output_file
        self._init_file()

    def _init_file(self):
        with open(self.output_file, "w", encoding="utf-8") as f:
            f.write("<!DOCTYPE html>\n<html>\n<head>\n")
            f.write("<meta charset='utf-8'>\n")
            f.write("<title>Carte de la Forêt</title>\n")
            f.write("<style>\n")
            f.write("body { font-family: monospace; background: #222; color: white; }\n")
            f.write(".grid { display: inline-block; line-height: 1.2; margin-bottom: 20px; }\n")
            f.write(".row { display: flex; }\n")
            f.write(".cell { width: 24px; height: 24px; text-align: center; }\n")
            f.write("</style>\n</head>\n<body>\n")
            f.write("<h1>Simulations de Feu de Forêt</h1>\n")

    def log(self, map_grid, title=None):
        with open(self.output_file, "a", encoding="utf-8") as f:
            if title:
                f.write(f"<h2>{title}</h2>\n")
            f.write("<div class='grid'>\n")
            for row in map_grid.grid:
                f.write("<div class='row'>\n")
                for node in row:
                    symbol = self.SYMBOLS.get(node.state, "?")
                    f.write(f"<div class='cell'>{symbol}</div>\n")
                f.write("</div>\n")
            f.write("</div>\n")

    def end(self):
        with open(self.output_file, "a", encoding="utf-8") as f:
            f.write("</body>\n</html>\n")
