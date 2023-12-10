# Definition for a binary tree node.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.array_to_bst(nums=nums)

        return root

    def array_to_bst(self, nums: List[int], root: Optional[TreeNode] = None):
        middle_index = len(nums) // 2
        curr_val = nums[middle_index]
        print(curr_val)

        if root is None:
            root = TreeNode(val=curr_val)
        else:
            root.val = curr_val

        if len(nums[:middle_index]) > 0:
            root.left = TreeNode()
            self.array_to_bst(nums=nums[:middle_index], root=root.left)

        if len(nums[middle_index + 1:]) > 0:
            root.right = TreeNode()
            self.array_to_bst(nums=nums[middle_index + 1:], root=root.right)

        return root


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            if root.left is not None:
                print_tree(root.left, level + 1, "L--- ")
            if root.right is not None:
                print_tree(root.right, level + 1, "R--- ")


if __name__ == '__main__':
    solution = Solution()

    nums = [-10, -3, 0, 5, 9]
    root = solution.sortedArrayToBST(nums=nums)
    print_tree(root=root)

