from src.node import Node

def test_node_initial_state():
    node = Node()
    assert node.state == Node.EMPTY

def test_non_burnable_node():
    node = Node(Node.EMPTY)
    assert not node.is_burnable()

def test_burnable_node():
    node = Node(Node.TREE)
    assert node.is_burnable()

def test_ignite_node():
    node = Node(Node.TREE)
    node.ignite(step=1)
    assert node.state == Node.FIRE

def test_burnout_node():
    node = Node(Node.TREE)
    node.ignite(step=1)
    node.burn_out()
    assert node.state == Node.BURNED
