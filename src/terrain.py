class Terrain:
    def __init__(self, percentage_of_trees=30):
        if not 0 <= percentage_of_trees <= 100:
            raise ValueError("Le pourcentage d'arbres doit être entre 0 et 100")
        
        self.percentage_of_trees = percentage_of_trees
    
    def get_percentage_of_trees(self):
        return self.percentage_of_trees
    
    def set_percentage_of_trees(self, percentage):
        if not 0 <= percentage <= 100:
            raise ValueError("Le pourcentage d'arbres doit être entre 0 et 100")
        
        self.percentage_of_trees = percentage