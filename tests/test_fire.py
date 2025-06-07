from src.mapGenerator import MapGenerator
from src.fireGenerator import FireGenerator
from src.node import Node

def test_fire_starts_if_tree_exists():
    map_gen = MapGenerator(width=5, height=5, percentage_of_trees=100)
    map_gen.generate()
    fire = FireGenerator(map_gen)
    fire.start_fire()
    r, c = fire.origin
    assert map_gen.grid[r][c].state == Node.FIRE

def test_fire_does_not_start_if_no_trees():
    map_gen = MapGenerator(width=5, height=5, percentage_of_trees=0)
    map_gen.generate()
    fire = FireGenerator(map_gen)
    fire.start_fire()
    assert fire.origin is None

def test_fire_spreads_to_all_trees():
    map_gen = MapGenerator(width=3, height=3, percentage_of_trees=100)
    map_gen.generate()
    fire = FireGenerator(map_gen)
    fire.start_fire()
    fire.spread()

    for row in map_gen.grid:
        for node in row:
            assert node.state == Node.BURNED or node.state == Node.FIRE

def test_fire_stops_when_no_more_burnable_neighbors():
    map_gen = MapGenerator(width=3, height=3, percentage_of_trees=0)
    map_gen.generate()
    # Ajout d'un TREE à la main pour isoler le feu
    map_gen.grid[1][1].state = Node.TREE
    fire = FireGenerator(map_gen)
    fire.start_fire()
    fire.spread()
    assert map_gen.grid[1][1].state == Node.FIRE # FIRE et pas BURNED car on doit garder l'icône de feu pour savoir où ça a commencé


def test_fire_propagates_and_stops_correctly():
    map_gen = MapGenerator(width=3, height=3, percentage_of_trees=0)
    map_gen.generate()

    # Ajout de plusieurs TREE à la main
    tree_positions = [(1, 1), (0, 1), (1, 0), (1, 2), (2, 1)]
    for r, c in tree_positions:
        map_gen.grid[r][c].state = Node.TREE

    fire = FireGenerator(map_gen)
    fire.origin = (1, 1)
    map_gen.grid[1][1].ignite()
    fire.spread()
    # Le start FIRE
    assert map_gen.grid[1][1].state == Node.FIRE
    # Les voisins BURNED
    for r, c in [(0, 1), (1, 0), (1, 2), (2, 1)]:
        assert map_gen.grid[r][c].state == Node.BURNED
