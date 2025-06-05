import random
from terrain import Terrain

class MapGenerator:
    EMPTY = 0   
    TREE = 1    
    
    def __init__(self, width=10, height=10, terrain=None):
        self.width = width
        self.height = height
        self.terrain = terrain if terrain else Terrain()
        self.map_grid = []
    
    def generate_map(self):
        self.map_grid = []
        
        for row in range(self.height):
            map_row = []
            for col in range(self.width):
                random_value = random.randint(1, 100)
            
                if random_value <= self.terrain.get_percentage_of_trees():
                    map_row.append(self.TREE)
                else:
                    map_row.append(self.EMPTY)
            
            self.map_grid.append(map_row)
    
    def print_map_console(self):
        if not self.map_grid:
            print("Aucune carte générée. Appelez generate_map() d'abord.")
            return
        
        print(f"Carte générée avec {self.terrain.get_percentage_of_trees()}% d'arbres:")
        print("-" * (self.width * 2))
        
        for row in self.map_grid:
            formatted_cells = []
            for cell in row:
                if cell == self.TREE:
                    formatted_cells.append("🌳")
                else:
                    formatted_cells.append("🌱")
            print(" ".join(formatted_cells))
        
        print("-" * (self.width * 2))
        
        total_cells = self.width * self.height
        tree_count = sum(row.count(self.TREE) for row in self.map_grid)
        actual_percentage = (tree_count / total_cells) * 100
        
        print(f"Statistiques:")
        print(f"  - Taille: {self.width}x{self.height} ({total_cells} cases)")
        print(f"  - Pourcentage d'arbres souhaité: {self.terrain.get_percentage_of_trees()}%")
        print(f"  - Pourcentage d'arbres réel: {actual_percentage:.1f}%")
        print(f"  - Nombre d'arbres: {tree_count} 🌳")
        print(f"  - Terrain vide: {total_cells - tree_count} cases 🌱")
    
    
    def get_map(self):
        return self.map_grid
    
    def set_seed(self, seed):
        random.seed(seed)