class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root.left, root.right)
        
    def check(self, left: Optional[TreeNode], right: Optional[TreeNode]):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        if left.val == right.val:
            return self.check(left.left, right.right) and self.check(left.right, right.left)
        return False

        