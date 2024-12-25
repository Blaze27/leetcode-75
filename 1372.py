from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root):
            if not root:
                return
            nonlocal ans
            ans = max(helper(root, ""), ans)
            dfs(root.left)
            dfs(root.right)

        def helper(root, direction):
            if not root:
                return 0

            if root.left and direction == 'left':
                return 1 + helper(root.left, 'right')

            if root.right and direction == 'right':
                return 1 + helper(root.right, 'left')

            return max(helper(root.left, 'right'), helper(root.right, 'left'))

        dfs(root)
        return ans + 1 if ans > 0 else ans


# root = TreeNode(1)
# root.left = TreeNode()
# root.right = TreeNode(1)
# root.right.left = TreeNode(1)
# root.right.right = TreeNode(1)
# root.right.right.right = TreeNode(1)
# root.right.right.left = TreeNode(1)
# root.right.right.left.right = TreeNode(1)
# root.right.right.left.right.right = TreeNode(1)
root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.right = TreeNode(1)
print(Solution().longestZigZag(root))


