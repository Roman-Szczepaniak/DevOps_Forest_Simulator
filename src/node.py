class Node:
    EMPTY = "empty"
    TREE = "tree"
    FIRE = "fire"
    BURNED = "burned"

    def __init__(self, state=EMPTY):
        self.state = state
        self.burn_start = None 

    def is_burnable(self):
        return self.state == Node.TREE

    def ignite(self, step=0):
        self.state = Node.FIRE
        self.burn_start = step

    def burn_out(self):
        self.state = Node.BURNED
