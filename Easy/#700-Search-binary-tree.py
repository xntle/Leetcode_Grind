# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        curr = root  # start from the root of the BST
        while curr is not None:  # loop until we reach a null node
            if val < curr.val:  # if val is less than current node's value, go left
                curr = curr.left
            elif val > curr.val:  # if val is greater, go right
                curr = curr.right
            else:  # if we found the value, return the current node
                return curr
        
        # If the value is not found in the BST
        return None  # return None if the value is not found
        