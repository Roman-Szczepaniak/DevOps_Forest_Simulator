from src.mapGenerator import MapGenerator
from src.node import Node
from src.bestCut import BestCut

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

    best_cut = BestCut.find_best_tree_to_cut(map_gen, origin)

    assert best_cut == (0, 0) or best_cut == (1, 0) or best_cut == (0, 1) or best_cut == (1, 2) or best_cut == (2, 1)

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

    results = set()
    for _ in range(10):
        best_cut = BestCut.find_best_tree_to_cut(map_gen, origin)
        results.add(best_cut)

    assert (0, 0) in results
    assert (0, 1) in results
    assert (0, 2) in results
    assert (1, 0) in results
    assert (1, 2) in results
    assert (2, 0) in results
    assert (2, 1) in results
    assert (2, 2) in results
    assert len(results) > 1  

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

    best_cut = BestCut.find_best_tree_to_cut(map_gen, origin)

    assert best_cut in [(0, 1), (1, 0), (1, 1)]