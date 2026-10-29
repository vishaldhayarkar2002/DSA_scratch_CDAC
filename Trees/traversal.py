class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Inorder (recursive)
def inorder(root, res=None):
    if res is None:
        res = []
    if not root:
        return res
    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)
    return res

# Iterative inorder
def inorder_iter(root):
    res, stack = [], []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res

# Level order
from collections import deque
def level_order(root):
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res