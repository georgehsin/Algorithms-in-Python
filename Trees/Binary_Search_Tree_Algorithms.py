class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
# Calling next() will return the next smallest number in the BST.

# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.iterate(root)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.stack) > 0:
            return True

    def next(self):
        """
        :rtype: int
        """
        while len(self.stack) > 0:
            return self.stack.pop()
        return
    
    def iterate(self, root):
        if not root:
            return
        self.iterate(root.right)
        self.stack.append(root.val)
        self.iterate(root.left)

class Solution(object):
    def getMinimumDifference(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # In BST values are sorted - therefore, by using inorder traversal and putting values in a stack, you can just iterate through the stack and find the minimum difference
    nums = self.inorder(root)
    numsList = []
    for i in range(len(nums)-1):
        numsList.append(nums[i+1]-nums[i])
    return min(numsList)

# Returns an array In Order Traversal (Helper Function)
    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

# Convert a sorted Array to a BST
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums)/2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return []
        self.res = 'unset'
        self.find(root, p, q)
        return self.res
        
    #Helper    
    def find(self, root, p, q):
        if not root:
            return []
        list = self.find(root.left, p, q) + [root.val] + self.find(root.right, p, q)
        if p.val in list and q.val in list:
            if self.res == 'unset':
                self.res = root.val
        return list

# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.dict = {}
        self.preorder(root)
        max = 0
        res = []
        for key, value in self.dict.iteritems():
            if value > max:
                res = []
                max = value
                res.append(key)
            elif value == max:
                res.append(key)
        return res
    
    #Helper
    def preorder(self, root):
        if not root:
            return
        self.preorder(root.left)
        try:
            self.dict[root.val] += 1 
        except:
            self.dict[root.val] = 1 
        self.preorder(root.right)

# find minimum depth of BST.
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: 
            return 0
        l = self.minDepth(root.left)+1
        r = self.minDepth(root.right)+1
        if l == 1 or r == 1:
            return max (l,r)
        return min(l,r)

#  find the leftmost value in the last row of the BST.
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return NULL
        self.parent = [root]
        self.child = []
        while len(self.parent) > 0:
            current = self.parent.pop(0)
            print current
            if current.right:
                self.child.append(current.right)
            if current.left:
                self.child.append(current.left)
            if len(self.parent)==0 and len(self.child)==0:
                return current.val
            if len(self.parent)==0:
                self.parent = self.child
                self.child = []

# convert BST to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return []
        self.sum = 0
        self.traverse(root)
        return root
    
    #Helper
    def traverse(self, root):
        if not root:
            return
        if root.right:
            self.traverse(root.right)
        self.sum += root.val
        root.val = self.sum
        if root.left:
            self.traverse(root.left)


        
        
