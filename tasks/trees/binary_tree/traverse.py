"""Module with traverse algorithms for binary tree"""

from collections import deque

from tasks.trees.binary_tree.binary_tree import BinaryTree


def traverse_preorder(root: BinaryTree):
    print(root.payload)  # Here we can not just print node, but process it someway

    if root.left_child:
        traverse_preorder(root.left_child)

    if root.right_child:
        traverse_preorder(root.right_child)


def traverse_inorder(root: BinaryTree):
    if root.left_child:
        traverse_inorder(root.left_child)

    print(root.payload)  # Here we can not just print node, but process it someway

    if root.right_child:
        traverse_inorder(root.right_child)


def traverse_postorder(root: BinaryTree):
    if root.left_child:
        traverse_postorder(root.left_child)

    if root.right_child:
        traverse_postorder(root.right_child)

    print(root.payload)


def traverse_depth_first(root: BinaryTree):
    children = deque()

    children.append(root)

    while len(children) != 0:
        node = children.popleft()

        print(node.payload)

        if node.left_child:
            children.append(node.left_child)

        if node.right_child:
            children.append(node.right_child)


if __name__ == '__main__':

    """
        A
        /\
       /  \
      /    \
      B     C
      |\    |\
      | \   | \
      D  E  F  G
    """

    child_2_1 = BinaryTree(payload='D')
    child_2_2 = BinaryTree(payload='E')
    child_2_3 = BinaryTree(payload='F')
    child_2_4 = BinaryTree(payload='G')

    child_1_1 = BinaryTree(payload='B', left_child=child_2_1, right_child=child_2_2)
    child_1_2 = BinaryTree(payload='C', left_child=child_2_3, right_child=child_2_4)

    root = BinaryTree(payload='A', left_child=child_1_1, right_child=child_1_2)

    print(f'Traverse preorder:')
    traverse_preorder(root=root)

    print(f'Traverse inorder:')
    traverse_inorder(root=root)

    print(f'Traverse postorder:')
    traverse_postorder(root=root)

    print(f'Traverse depth first:')
    traverse_depth_first(root=root)

