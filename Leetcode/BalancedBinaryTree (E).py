class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        if left - right > 1 or right - left > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def height(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return -1
        if root.left == None and root.right == None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))