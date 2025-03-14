class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def average_of_bst(root, low, high):
    """
    Calculates the average of node values within a given range in a BST using DFS.

    Args:
        root: The root node of the BST.
        low: The lower bound of the range.
        high: The upper bound of the range.

    Returns:
        The average of the node values within the range.
    """
    total_sum = 0
    total_count = 0

    def dfs(node):
      nonlocal total_sum, total_count
      if not node:
        return 

      if low <= node.val <= high:
        total_sum += node.val
        total_count += 1

      if node.left and node.val > low:
        dfs(node.left)

      if node.right and node.val < high:
         dfs(node.right)

    dfs(root)

    if total_count == 0:
        return 0.0  # Handle the case where no nodes are in the range
    else:
      return total_sum / total_count


def test_average_of_bst():
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right = Node(15)
    root.right.right = Node(18)

    assert abs(average_of_bst(root, 7, 15) - (32.0 / 3.0)) < 1e-9
    assert abs(average_of_bst(root, 0, 9000) - (58.0 / 6.0)) < 1e-9
    assert abs(average_of_bst(root, 7, 7) - 7.0) < 1e-9
    assert abs(average_of_bst(root, 14, 18) - (33.0 / 2.0)) < 1e-9
    assert abs(average_of_bst(root, 3, 6) - 4.0) < 1e-9
    print("All tests passed!")

test_average_of_bst()
