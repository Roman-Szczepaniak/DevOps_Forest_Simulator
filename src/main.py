from src.fireGenerator import FireGenerator
from src.consoleMapLogger import ConsoleMapLogger
from src.mapGenerator import MapGenerator
from src.bestCut import BestCut
from src.node import Node
from copy import deepcopy

def main():
    # 1. Generate map
    map_without_cut = MapGenerator(width=10, height=10, percentage_of_trees=50)
    map_without_cut.generate()

    logger = ConsoleMapLogger()
    print("Carte initiale :")
    logger.log(map_without_cut)

    map_with_cut = deepcopy(map_without_cut)

    # 3. Map without cut
    sim1 = FireGenerator(map_without_cut)
    origin = sim1.start_fire()
    sim1.spread()

    print("\nCarte après feu (sans arbre coupé) :")
    logger.log(map_without_cut)

    # 4. Map with cut
    if origin:
        best_cut_pos = BestCut.find_best_tree_to_cut(map_with_cut, origin)
        if best_cut_pos:
            r, c = best_cut_pos
            map_with_cut.grid[r][c].state = Node.CUT

        sim2 = FireGenerator(map_with_cut, origin=origin)
        sim2.start_fire()
        sim2.spread()

        print("\nCarte après feu (avec arbre coupé) :")
        logger.log(map_with_cut)
    else:
        print("Pas de feu initial.")

if __name__ == "__main__":
    main()
