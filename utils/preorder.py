def preorder_iterative(root):
    end_nodes = []
    q = []
    q.append(root)
    while len(q):
        current = q.pop()
        print(current.val)

        if current.right != None:
            q.append(current.right)

        if current.left != None:
            q.append(current.left)
        print(q)

preorder_iterative(root1)
