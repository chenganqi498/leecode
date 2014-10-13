# Given a string s1, we may represent it as a binary tree 
# by partitioning it to two non-empty substrings recursively.

# Below is one possible representation of s1 = "great":
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t

# To scramble the string, we may choose any non-leaf node and swap its two children.

# For example, if we choose the node "gr" and swap its two children, 
# it produces a scrambled string "rgeat".

#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".

# Similarly, if we continue to swap the children of nodes "eat" and "at", 
# it produces a scrambled string "rgtae".

#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".

# Given two strings s1 and s2 of the same length, 
# determine if s2 is a scrambled string of s1.

class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# This version find all scrambles of s1, exceed time limit
class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if s1 == '' and s2 == '': return True
        if len(s1) != len(s2): return False
        trees = [TreeNode(s1[0])]
        allscramble = []

        # all possible binary trees of s1
        for s in s1[1:]:
            temp = []
            for t in trees:
                newroot = TreeNode(t.val+s)
                newroot.left = t
                newroot.right = TreeNode(s)
                temp.append(newroot)
                temp.append(self.addOneLt(t, s))
            trees = temp

        for t in trees:
            allscramble += self.scramble(t)
        for i in allscramble:
            if s2 == i.val: return True
        return False         

    def addOneLt(self, root, s):
        if root == None: return
        newroot = TreeNode(root.val+s)
        if root.right == None:
           newroot.left = TreeNode(root.val)
           newroot.right = TreeNode(s)
        else: 
           newroot.right = self.addOneLt(root.right, s)
           newroot.left = root.left
        return newroot

    def buildTree(self, left, right):
        root = TreeNode(left.val+right.val)
        root.left, root.right = left, right
        return root

    def scramble(self, root):
        newroots = []
        if root.left == None: return [root]
        newlefts = self.scramble(root.left)
        newrights = self.scramble(root.right)
        for nl in newlefts:
            for nr in newrights:
                newroots.append(self.buildTree(nl, nr))

        exchange = []
        for nr in newroots:
            temp = TreeNode(nr.right.val+nr.left.val)
            temp.left, temp.right = nr.right, nr.left
            exchange.append(temp)
        newroots += exchange
        return newroots

if __name__ == '__main__':
   s1 = "abcdefghij"
   s2 = "efghijcadb"

   test = Solution()
   out = test.isScramble(s1, s2)
   print out


