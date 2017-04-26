class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
# Check if our Binary Tree is balanced
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
        
# Get height of Binary Tree
    def height(self, root):
        if not root:
            return 0
        l = self.height(root.left)+1
        r = self.height(root.right)+1
        if abs(l-r) >= 2:
            self.balanced = False
        return max(l,r)

# Given a binary tree, find its maximum depth.
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

# Invert Binary Tree
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # if root:
        #     self.invertTree(root.right)
        #     self.invertTree(root.left)
        #     temp = root.right
        #     root.right = root.left
        #     root.left = temp
        # return root
        
        if root:
            (root.left, root.right) = (self.invertTree(root.right), self.invertTree(root.left))
        return root

# Sum of left leaves
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        if root:
            if root.right:
                sum += self.sumOfLeftLeaves(root.right)
            leftroot = root.left
            if root.left:
                if leftroot.left == None and leftroot.right == None:
                    sum += leftroot.val
                else:
                    sum += self.sumOfLeftLeaves(root.left)
        return sum

# Given two binary trees, write a function to check if they are equal or not
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.best = 1
        self.height(root)
        return self.best - 1 

    #Helper Function
    def height(self,root):  
        if not root:
            return 0
        right = self.height(root.right)
        left = self.height(root.left)
        self.best = max(self.best, right + left + 1)
        return 1 + max(right, left)

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        self.adding(root, sum)
        if root:
            self.count += self.pathSum(root.right, sum)
            self.count += self.pathSum(root.left, sum)
        return self.count
        
    #Helper    
    def adding(self, root, sum):
        if not root:
            return 0
        if root.val == sum:
            self.count +=1
        newsumpath = sum - root.val
        self.adding(root.left, newsumpath)
        self.adding(root.right, newsumpath)

# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        list = []
        stack = [(root,0)]
        while stack:
            root, level = stack.pop()
            print root.val
            if len(list) < level+1:
                list.insert(0,[])
            list[-(level+1)].append(root.val)
            if root.right:
                stack.append((root.right,level+1))
            if root.left:
                stack.append((root.left,level+1))
            print list
        return list

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.checkleft(root) == self.checkright(root)
    
    #Helpers
    def checkleft(self, root):    
        if not root:
            return [0]
        return [root.val] + self.checkleft(root.left) + self.checkleft(root.right)
    def checkright(self, root):
        if not root:
            return [0]
        return [root.val] + self.checkright(root.right) + self.checkright(root.left)

# return all root-to-leaf paths.
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.stack = []
        self.list = []
        self.traverse(root)
        return self.stack

    #Helper
    def traverse(self, root):
        self.list.append(root.val)
        if root.right == None and root.left == None:
            path = ''
            for x in range (len(self.list)-1):
                path += str(self.list[x]) + '->'
            path += str(self.list.pop())
            self.stack.append(path)
            return
        if root.left:
            self.traverse(root.left)       
        if root.right:
            self.traverse(root.right)
        self.list.pop()

# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.left == None and root.right == None and root.val == sum:
            return True
        if root.right:    
            if self.hasPathSum(root.right, sum-root.val):
                return True
        if root.left:    
            if self.hasPathSum(root.left, sum-root.val):
                return True
        return False

# find the largest value in each row of a binary tree.

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        max = [root.val]
        parentstack = [root]
        childstack = []
        while len(parentstack) >= 0:
            if len(parentstack) == 0:
                if len(childstack) == 0:
                    break
                maxrow = childstack[0].val
                for x in range (1,len(childstack)):
                    if childstack[x].val > maxrow:
                        maxrow = childstack[x].val
                max.append(maxrow)
                parentstack = childstack
                childstack = []
            current = parentstack.pop()
            if current.left:
                childstack.append(current.left)
            if current.right:
                childstack.append(current.right)
        return max

# Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.
from collections import Counter
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        self.sumlist = []
        self.traverse(root)
        count = Counter(self.sumlist)
        res =[]
        for i in count.most_common():
            mostcommon = count.most_common()[0][1]
            if i[1] != mostcommon:
                break
            res.append(i[0])
        return res

    #Helper
    def traverse(self, root):
        if not root: return 0
        sum = 0
        sum = self.traverse(root.left) + self.traverse(root.right) + root.val
        self.sumlist.append(sum)
        return sum

# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.stack = []
        self.count = -1
        self.append(root, 0)
        return self.stack
        
    #Helper
    def append(self, root, height):
        if not root: 
            return
        if height > self.count:
            self.stack.append(root.val)
            self.count += 1
        self.append(root.right, height+1)
        self.append(root.left, height+1)

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res = [[root.val]]
        self.parent = [root]
        self.children = []
        while len(self.parent) > 0:
            current = self.parent.pop(0)
            if current.left:
                self.children.append(current.left)
            if current.right:
                self.children.append(current.right)
            if len(self.parent) == 0:
                list = []
                for i in self.children:
                    list.append(i.val)
                res.append(list)
                self.parent = self.children
                self.children = []
        res.pop()
        return res