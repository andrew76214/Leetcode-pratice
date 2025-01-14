# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root) -> list[int]:
        if not root:
            return []
        
        leaves = []
        stack = [root]

        while stack:
            current = stack.pop()

            if not current.left and not current.right:
                leaves.append(current.val)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        
        return leaves

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return False

        leaves_1 = self.dfs(root1)
        leaves_2 = self.dfs(root2)

        return leaves_1 == leaves_2
