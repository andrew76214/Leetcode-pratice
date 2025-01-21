# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans_count = 0
        path = defaultdict(int)
        path[0] = 1

        def dfs(node: Optional[TreeNode], pathSum: int):
            nonlocal ans_count
            if not node:
                return
            
            pathSum += node.val
            ans_count += path[pathSum - targetSum]
            path[pathSum] += 1

            dfs(node.left, pathSum)
            dfs(node.right, pathSum)
            path[pathSum] -= 1  # BackTracking

        dfs(root, 0)

        return ans_count
