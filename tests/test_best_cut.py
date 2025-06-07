from src.mapGenerator import MapGenerator
from src.node import Node

def test_find_best_tree_to_cut_minimizes_fire_spread():
    """
    Carte :
    🌳 🌳 🌳
    🌳 🔥 🌳
    🌳 🌳 🌳

    Couper (1, 0) limite la propagation mieux que les autres.
    """
    map_gen = MapGenerator(width=3, height=3, percentage_of_trees=100)
    map_gen.generate()

    # Forcer tous les noeuds à TREE
    for r in range(3):
        for c in range(3):
            map_gen.grid[r][c].state = Node.TREE

    origin = (1, 1)

    best_cut = find_best_tree_to_cut(map_gen, origin)

    assert best_cut == (1, 0)

def test_multiple_best_cut_positions_possible():
    """
    Plusieurs cases à couper réduisent les dégâts de la même manière.
    """
    map_gen = MapGenerator(width=3, height=3, percentage_of_trees=100)
    map_gen.generate()

    for r in range(3):
        for c in range(3):
            map_gen.grid[r][c].state = Node.TREE

    origin = (1, 1)

    best_cuts = find_best_tree_to_cut(map_gen, origin, return_all=True)

    assert (1, 0) in best_cuts
    assert (0, 1) in best_cuts
    assert len(best_cuts) > 1

def test_cutting_any_tree_does_not_reduce_fire_spread():
    """
    Tous les arbres brûlent même si on coupe un.
    """
    map_gen = MapGenerator(width=2, height=2, percentage_of_trees=100)
    map_gen.generate()

    for r in range(2):
        for c in range(2):
            map_gen.grid[r][c].state = Node.TREE

    origin = (0, 0)

    best_cut = find_best_tree_to_cut(map_gen, origin)

    assert best_cut in [(0, 1), (1, 0), (1, 1)]