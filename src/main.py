from terrain import Terrain
from mapGenerator import MapGenerator

def main():
    """
    Fonction principale du simulateur de feux de forêts
    """
    print("=== Simulateur de feux de forêts ===\n")
    
    # Terrain 40% d'arbres
    terrain = Terrain(percentage_of_trees=40)
    
    map_gen = MapGenerator(width=10, height=8, terrain=terrain)
    
    map_gen.generate_map()
    
    map_gen.print_map_console()
    
    print("\n" + "="*50)
    
    print("\nTest avec 0% d'arbres (terrain complètement vide):\n")
    terrain2 = Terrain(percentage_of_trees=0)
    map_gen2 = MapGenerator(width=8, height=6, terrain=terrain2)
    map_gen2.generate_map()
    map_gen2.print_map_console()
    
    print("\nTest avec 100% d'arbres (forêt complète):\n")
    terrain3 = Terrain(percentage_of_trees=100)
    map_gen3 = MapGenerator(width=6, height=4, terrain=terrain3)
    map_gen3.generate_map()
    map_gen3.print_map_console()

if __name__ == "__main__":
    main()