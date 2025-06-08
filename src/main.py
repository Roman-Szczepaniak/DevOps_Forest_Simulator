from src.fireGenerator import FireGenerator
from src.htmlMapLogger import HtmlMapLogger
from src.mapGenerator import MapGenerator
from src.bestCut import BestCut
from src.node import Node
from copy import deepcopy

def main():
    # 1. Générer la carte
    map_without_cut = MapGenerator(width=10, height=10, percentage_of_trees=50)
    map_without_cut.generate()

    logger = HtmlMapLogger("simulation.html")
    logger.log(map_without_cut, title="Carte initiale")

    map_with_cut = deepcopy(map_without_cut)

    # 2. Simulation sans coupe
    sim1 = FireGenerator(map_without_cut)
    origin = sim1.start_fire()
    sim1.spread()

    logger.log(map_without_cut, title="Après feu sans arbre coupé")

    # 3. Simulation avec arbre coupé
    if origin:
        best_cut_pos = BestCut.find_best_tree_to_cut(map_with_cut, origin)
        if best_cut_pos:
            r, c = best_cut_pos
            map_with_cut.grid[r][c].state = Node.CUT

        sim2 = FireGenerator(map_with_cut, origin=origin)
        sim2.start_fire()
        sim2.spread()

        logger.log(map_with_cut, title="Après feu avec arbre coupé")
    else:
        logger.log(map_with_cut, title="Aucun feu initial.")

    logger.end()

if __name__ == "__main__":
    main()
