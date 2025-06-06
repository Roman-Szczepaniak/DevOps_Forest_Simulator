import pytest
from src.terrain import Terrain

def test_terrain_set_percentage_of_trees():
    terrain = Terrain()
    terrain.set_percentage_of_trees(80)
    assert terrain.get_percentage_of_trees() == 80

def test_terrain_invalid_set_percentage_of_trees():
    terrain = Terrain()
    with pytest.raises(ValueError):
        terrain.set_percentage_of_trees(200)

def test_terrain_percentage_of_trees():
    terrain = Terrain(percentage_of_trees=50)
    assert terrain.get_percentage_of_trees() == 50

def test_terrain_invalid_percentage_of_trees():
    with pytest.raises(ValueError):
        Terrain(percentage_of_trees=150)
