from IMapLogger import IMapLogger
from node import Node

class HtmlMapLogger(IMapLogger):
    SYMBOLS = {
        Node.EMPTY: "🟫",
        Node.TREE: "🌳",
        Node.FIRE: "🔥",
        Node.BURNED: "⬛"
    }

    def __init__(self, output_file="map.html"):
        self.output_file = output_file

    def log(self, map_grid):
        with open(self.output_file, "w", encoding="utf-8") as f:
            f.write("<!DOCTYPE html>\n<html>\n<head>\n")
            f.write("<meta charset='utf-8'>\n")
            f.write("<title>Carte de la Forêt</title>\n")
            f.write("<style>\n")
            f.write("body { font-family: monospace; background: #222; color: white; }\n")
            f.write(".grid { display: inline-block; line-height: 1.2; }\n")
            f.write(".row { display: flex; }\n")
            f.write(".cell { width: 24px; height: 24px; text-align: center; }\n")
            f.write("</style>\n</head>\n<body>\n")
            f.write("<h1>Carte de la Forêt</h1>\n<div class='grid'>\n")

            for row in map_grid.grid:
                f.write("<div class='row'>\n")
                for node in row:
                    symbol = self.SYMBOLS[node.state]
                    f.write(f"<div class='cell'>{symbol}</div>\n")
                f.write("</div>\n")

            f.write("</div>\n</body>\n</html>\n")
