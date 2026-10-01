"""
LeetCode - Binary Tree In Order Traversal

Time complexity: O(n log n) if the tree is balanced, because each of the
log(n) levels copies about n elements as results are passed up. O(n^2) if
the tree is skewed.

Space complexity: O(n) for the output plus temporary lists, and O(h) for the
recursion stack, h being the height of the tree.

A brute force approach would be to scan the tree and store every node to put it in order. The optimized approach would be to start at the left and visit its node then the right. This only visits each node once. 
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        tree = []

        if root is not None:
            left = self.inorderTraversal(root.left)
            tree.extend(left)
            tree.append(root.val)
            right = self.inorderTraversal(root.right)
            tree.extend(right)

        return tree

if __name__ == "__main__":
    sol = Solution()

    t1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert sol.inorderTraversal(t1) == [1, 3, 2]

    t2 = TreeNode(1,
                  TreeNode(2,
                           TreeNode(4),
                           TreeNode(5, TreeNode(6), TreeNode(7))),
                  TreeNode(3,
                           None,
                           TreeNode(8, TreeNode(9))))
    assert sol.inorderTraversal(t2) == [4, 2, 6, 5, 7, 1, 3, 9, 8]

    assert sol.inorderTraversal(None) == []

    print("Passed")