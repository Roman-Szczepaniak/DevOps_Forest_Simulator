from src.fireGenerator import FireGenerator
from src.node import Node
from copy import deepcopy

class BestCut:
    @staticmethod
    def count_burned_trees(map_gen, origin):
        sim_map = deepcopy(map_gen)
        sim = FireGenerator(sim_map)
        sim.origin = origin
        r, c = origin
        sim_map.grid[r][c].ignite(step=0)
        sim.spread()

        return sum(
            1 for row in sim_map.grid for node in row
            if node.state == Node.BURNED
        )

    @staticmethod
    def find_best_tree_to_cut(map_gen, origin):
        height = map_gen.height
        width = map_gen.width

        best_position = None
        min_burned = float('inf')

        for r in range(height):
            for c in range(width):
                if (r, c) == origin:
                    continue
                if map_gen.grid[r][c].state != Node.TREE:
                    continue
                  
                # Create a copy of the map to test the cut
                test_map = deepcopy(map_gen)
                test_map.grid[r][c].state = Node.CUT

                burned = BestCut.count_burned_trees(test_map, origin)

                if burned < min_burned:
                    min_burned = burned
                    best_position = (r, c)
             
        if best_position:
            r, c = best_position
            map_gen.grid[r][c].state = Node.CUT
            
        return best_position
