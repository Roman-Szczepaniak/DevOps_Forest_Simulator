from src.mapGenerator import MapGenerator
from src.node import Node

def test_map_dimensions():
    map_gen = MapGenerator(width=5, height=4, percentage_of_trees=50)
    map_gen.generate()
    assert len(map_gen.grid) == 4
    assert all(len(row) == 5 for row in map_gen.grid)

def test_map_contains_only_nodes():
    map_gen = MapGenerator(width=3, height=3, percentage_of_trees=50)
    map_gen.generate()
    for row in map_gen.grid:
        for node in row:
            assert isinstance(node, Node)

def test_tree_ratio_respected_high_density():
    map_gen = MapGenerator(width=10, height=10, percentage_of_trees=90)
    map_gen.generate()
    tree_count = sum(node.state == Node.TREE for row in map_gen.grid for node in row)
    assert tree_count >= 80  # tolérance ±10%

def test_tree_ratio_respected_low_density():
    map_gen = MapGenerator(width=10, height=10, percentage_of_trees=10)
    map_gen.generate()
    tree_count = sum(node.state == Node.TREE for row in map_gen.grid for node in row)
    assert tree_count <= 20  # tolérance ±10%
