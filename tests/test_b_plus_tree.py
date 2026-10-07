"""tests for the b+Tree implementation"""

from seriousdb.b_plus_tree import _InternalNode, _LeafNode, bPlusTree


def assertTreeStructure(tree: bPlusTree) -> None:
    node = tree._root
    # okay here i will just make it a really long for loop so it cannot run infenetly if there is an error in the tree code
    children = []
    for i in range(0, 5000000, 1):
        if isinstance(node, _LeafNode):
            if node is not tree._root:
                assert node._parent is not None
            assert isinstance(node._parent, _LeafNode) is not True
            assert len(node._keys) <= tree._maxKeys
            assert len(node._values) == len(node._keys)
            return
        if isinstance(node, _InternalNode):
            if node is not tree._root:
                assert node._parent is not None
            assert len(node._keys) <= tree._maxKeys
            for child in node._children:
                if child not in children:
                    children.append(child)
            node = children.pop()


def test_put_first_key():
    maxChildren: int = 3
    tree: bPlusTree = bPlusTree(maxChildren)

    result = tree.put(1, b"2")

    assert result is True


def test_put_same_key():
    maxChildren: int = 3
    tree: bPlusTree = bPlusTree(maxChildren)

    tree.put(1, b"2")
    result: bool = tree.put(1, b"2")

    assert result is False


def test_force_split():
    maxChildren: int = 3
    tree: bPlusTree = bPlusTree(maxChildren)
    tree.put(1, b"AA")
    tree.put(2, b"AA")
    tree.put(3, b"AA")
    tree.put(4, b"AA")

    assertTreeStructure(tree)
    assert isinstance(tree._root, _InternalNode)


def test_stress_put():
    maxChildren: int = 3
    tree: bPlusTree = bPlusTree(maxChildren)
    for i in range(0, 100000, 1):
        tree.put(i, b"bbb")

    assertTreeStructure(tree)


def test_get_success():
    maxChildren: int = 3
    tree: bPlusTree = bPlusTree(maxChildren)

    tree.put(1, b"AA")
    value = tree.get(1)

    assert value == b"AA"


def test_get_empyTree():
    maxChildren: int = 3
    tree: bPlusTree = bPlusTree(maxChildren)
    # retrive
    value = tree.get(1)
    assert value == None


def test_get_KeyNotInTree():
    maxChildren: int = 3
    tree: bPlusTree = bPlusTree(maxChildren)

    tree.put(2, b"AA")
    tree.put(3, b"BB")

    value = tree.get(5)
    assert value == None
