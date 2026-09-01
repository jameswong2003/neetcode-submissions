# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(curr):
            if not curr:
                return [True, 0]

            left = depth(curr.left)
            right = depth(curr.right)

            if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
                return [True, 1 + max(left[1], right[1])]
            
            return [False, 1 + max(left[1], right[1])]
        
        return depth(root)[0]