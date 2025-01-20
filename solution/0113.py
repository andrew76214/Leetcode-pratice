# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # If there is no root, no paths exist
        if not root:
            return []
        
        results = []
        
        def dfs(node: Optional[TreeNode], current_path: List[int], current_sum: int):
            if not node:
                return
            
            # Choose (add node's value)
            current_path.append(node.val)
            current_sum += node.val
            
            if not node.left and not node.right and current_sum == targetSum:
                results.append(list(current_path))
            
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)
            
            # Backtrack
            current_path.pop()
            current_sum -= node.val
        
        # Start DFS from the root, with an empty path and sum = 0
        dfs(root, [], 0)
        return results
