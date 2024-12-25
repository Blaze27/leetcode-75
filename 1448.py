class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


ans = 0


class Solution:
    def findAns(self, root, max_val):
        if not root:
            return
        if root.val >= max_val:
            global ans
            ans += 1
            max_val = root.val
        self.findAns(root.left, max_val)
        self.findAns(root.right, max_val)

    def goodNodes(self, root: TreeNode) -> int:
        max_val = float('-inf')
        self.findAns(root, max_val)
        return ans


root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(3)

root.right = TreeNode(4)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

s = Solution()
print(s.goodNodes(root))
