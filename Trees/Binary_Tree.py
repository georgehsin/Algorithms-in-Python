class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        self.balanced = True
        self.height(root)
        return self.balanced
        
    def height(self, root):
        if not root:
            return 0
        l = self.height(root.left)+1
        r = self.height(root.right)+1
        if abs(l-r) >= 2:
            self.balanced = False
        return max(l,r)