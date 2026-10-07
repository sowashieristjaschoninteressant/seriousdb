"""tests for the b+Tree implementation"""

from seriousdb.b_plus_tree import bPlusTree


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
