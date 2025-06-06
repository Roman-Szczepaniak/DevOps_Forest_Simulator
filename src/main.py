from terrain import Terrain
from mapGenerator import MapGenerator
from fireGenerator import FireGenerator

def main():
    terrain = Terrain(percentage_of_trees=80)
    map_gen = MapGenerator(width=10, height=10, terrain=terrain)
    map_gen.generate_map()

    print("🌳 Carte initiale :")
    map_gen.print_map_console()

    simulator = FireGenerator(map_gen)
    simulator.start_fire()
    simulator.spread_fire()

    print("\n🔥 Carte après propagation du feu :")
    simulator.print_fire_map()

if __name__ == "__main__":
    main()
