import doctest
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Examples:
            >>> s = Solution()
            >>> s.preorderTraversal(\
            TreeNode(1, None, TreeNode(2, TreeNode(3))))
            [1, 2, 3]
            >>> s.preorderTraversal(None)
            []
            >>> s.preorderTraversal(TreeNode(1))
            [1]
        """
        res, stack = [], [root]
        while stack:
            root = stack.pop()
            if root is not None:
                res.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return res


if __name__ == '__main__':
    doctest.testmod(extraglobs={'s': Solution()})
