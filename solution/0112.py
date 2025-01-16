class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def get_sum(root, count):
            if not root:
                return False

            count += root.val

            # Check if it's a leaf node and the sum matches targetSum
            if not root.left and not root.right:
                return count == targetSum

            # Recur on left and right children
            return get_sum(root.left, count) or get_sum(root.right, count)

        return get_sum(root, 0)
