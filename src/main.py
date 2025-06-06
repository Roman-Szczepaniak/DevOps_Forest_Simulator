from terrain import Terrain
from mapGenerator import MapGenerator

def main():
    # Genération de la carte
    terrain = Terrain(percentage_of_trees=50)
    map_gen = MapGenerator(width=10, height=10, terrain=terrain)
    map_gen.generate_map()
    map_gen.print_map_console()

if __name__ == "__main__":
    main()