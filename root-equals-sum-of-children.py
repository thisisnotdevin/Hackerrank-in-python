class Solution(object):
    def checkTree(self, root):
        if root.left.val + root.right.val == root.val:
            return True
        return False
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
