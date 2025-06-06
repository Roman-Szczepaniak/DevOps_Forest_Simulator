import pytest
from src.mapGenerator import MapGenerator
from src.terrain import Terrain

def test_map_generation_dimensions():
    terrain = Terrain(percentage_of_trees=50)
    generator = MapGenerator(width=10, height=8, terrain=terrain)
    generator.set_seed(42)
    generator.generate_map()

    map_grid = generator.get_map()
    assert len(map_grid) == 8
    assert all(len(row) == 10 for row in map_grid)

def test_tree_percentage_approximation():
    width, height = 20, 20
    target_percentage = 40
    terrain = Terrain(percentage_of_trees=target_percentage)
    generator = MapGenerator(width=width, height=height, terrain=terrain)
    generator.set_seed(123)
    generator.generate_map()

    map_grid = generator.get_map()
    total_cells = width * height
    tree_cells = sum(row.count(MapGenerator.TREE) for row in map_grid)
    real_percentage = (tree_cells / total_cells) * 100

    assert target_percentage - 5 <= real_percentage <= target_percentage + 5
