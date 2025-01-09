class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        q = []
        q.append(root)
        depth = 0
        while len(q):
            for i in range(len(q)):
                node = q.pop(0)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)

            depth += 1

        return depth
