class Solution:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Solution.TreeNode, res: int):
          if not node:
            return 0

          places = 10 ** len(str(node.val))
          res = (res * places) + node.val

          if not node.left and not node.right:
            return res

          return dfs(node.left, res) + dfs(node.right, res)
        return dfs(root, 0)

def test_sumNumbers():
  solution = Solution()
  root = Solution.TreeNode(3)
  root.left = Solution.TreeNode(79, right=Solution.TreeNode(111))
  root.right = Solution.TreeNode(2)
  assert solution.sumNumbers(root) == 379143

  root = Solution.TreeNode(1)
  root.left = Solution.TreeNode(2)
  root.left.left = Solution.TreeNode(90)
  root.right = Solution.TreeNode(42)
  root.right.left = Solution.TreeNode(511)
  assert solution.sumNumbers(root) == 1290 + 142511

  root = Solution.TreeNode(1)
  root.left = Solution.TreeNode(2)
  root.left.left = Solution.TreeNode(912)
  root.left.left.left = Solution.TreeNode(3)
  root.left.left.right = Solution.TreeNode(4)
  root.right = Solution.TreeNode(46)
  root.right.left = Solution.TreeNode(5)
  root.right.right = Solution.TreeNode(61)
  assert solution.sumNumbers(root) == 129123 + 129124 + 1465 + 14661

  root = Solution.TreeNode(1)
  root.left = Solution.TreeNode(2)
  root.right = Solution.TreeNode(3)
  assert solution.sumNumbers(root) == 12 + 13

  root = Solution.TreeNode(10)
  root.left = Solution.TreeNode(200)
  root.right = Solution.TreeNode(3000)
  assert solution.sumNumbers(root) == 10200 + 103000

  root = Solution.TreeNode(10)
  root.left = Solution.TreeNode(0)
  root.right = Solution.TreeNode(0)
  assert solution.sumNumbers(root) == 200

  root = None
  assert solution.sumNumbers(root) == 0

test_sumNumbers()
