class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node, p, q):
            if node is None:
                return None

            if node == p or node == q:
                return node

            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if left and right:
                return node
            if left:
                return left
            if right:
                return right

        return dfs(root, p, q)

    def lowestCommonAncestorWhenOneofTheNodeIsNotPresent(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: if the root is None or root is p or q
        if node is None or node == p or node == q:
            return node

        # Recur for left and right subtree
        left = self.lowestCommonAncestorWhenOneofTheNodeIsNotPresent(node.left, p, q)
        right = self.lowestCommonAncestorWhenOneofTheNodeIsNotPresent(node.right, p, q)

        # If both left and right are non-null, root is the LCA
        if left and right:
            return node

        # Otherwise, return the non-null node (either left or right)
        return left if left else right


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
p = root.left.right.left
q = root.left.right.right
print(Solution().lowestCommonAncestor(root, p, q).val)
