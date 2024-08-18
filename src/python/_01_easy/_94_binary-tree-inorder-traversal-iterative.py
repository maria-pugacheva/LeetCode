import doctest
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Examples:
            >>> s = Solution()
            >>> s.inOrderTraversal(\
            TreeNode(1, None, TreeNode(2, TreeNode(3))))
            [1, 3, 2]
            >>> s.inOrderTraversal(None)
            []
            >>> s.inOrderTraversal(TreeNode(1))
            [1]
        """
        res, stack, curr = [], [], root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


if __name__ == '__main__':
    doctest.testmod(extraglobs={'s': Solution()})
