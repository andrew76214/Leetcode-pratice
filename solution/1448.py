class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        self.count = 0
        def dfs(node, path):
            if not node:
                return
            
            path.append(node.val)
            if node.val >= max(path):
                self.count += 1

            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        dfs(root, [])

        return self.count
