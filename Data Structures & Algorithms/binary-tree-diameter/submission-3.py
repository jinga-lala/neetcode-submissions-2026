# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.depth = None # what is the max depth assuming in the subtree with this node as root

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # for every node, i need to sum max depth left + right to get the diameter
        # depth can be obtained by backtracking

        def depth(node):
            if node is None:
                return -1
            if node.left is None and node.right is None:
                node.depth = 0
                return 0
            if node.depth is not None:
                return node.depth
            depth_left = 0
            depth_right = 0
            if node.left is not None:
                depth_left = 1 + depth(node.left)
            if node.right is not None:
                depth_right = 1 + depth(node.right)
            node.depth =  max(depth_left, depth_right)
            return node.depth
        
        def diameter(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 0
            
            diameter_left = 0
            diameter_right = 0
            if node.left is not None:
                diameter_left = 1+  depth(node.left)
            if node.right is not None:
                diameter_right = 1 + depth(node.right)
            return diameter_left + diameter_right
        
        def rec(node):
            return max(diameter(node), diameter(node.left), diameter(node.right))
        return rec(root)
