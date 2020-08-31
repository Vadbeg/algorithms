from typing import Union, Optional

from trees.binary_tree.traverse import traverse_inorder, traverse_depth_first


class BinarySearchTree:
    def __init__(self, payload: Union[int, float]):
        self.left_child: Optional['BinarySearchTree'] = None
        self.right_child: Optional['BinarySearchTree'] = None

        self.parent: Optional['BinarySearchTree'] = None

        self.payload: Union[int, float] = payload

    def insert_node(self, node: 'BinarySearchTree'):
        if node.payload < self.payload:
            if self.left_child:
                self.left_child.insert_node(node=node)
            else:
                self.left_child = node
                self.left_child.parent = self

        else:
            if self.right_child:
                self.right_child.insert_node(node=node)
            else:
                self.right_child = node
                self.right_child.parent = self

    def find_value(self, value: Union[int, float]) -> Optional['BinarySearchTree']:
        if value < self.payload:
            if self.left_child:
                result = self.left_child.find_value(value=value)
            else:
                return None
        elif value > self.payload:
            if self.right_child:
                result = self.right_child.find_value(value=value)
            else:
                return None
        else:
            result = self

        return result

    @staticmethod
    def __pop_max_el__(root: 'BinarySearchTree'):

        if root.right_child:
            while root.right_child:
                root = root.right_child

            if root.parent:
                if root.left_child:
                    root.parent.right_child = root.left_child
                    root.parent.right_child.parent = root.parent
                else:
                    root.parent.right_child = None

        return root

    def replace_nodes(self, node: Optional['BinarySearchTree']):
        if self.parent:
            if self.parent.left_child and self == self.parent.left_child:
                self.parent.left_child = node
            elif self.parent.right_child:
                self.parent.right_child = node

        if node:
            node.parent = self.parent

    def remove_value(self, value: Union[int, float]) -> Optional['BinarySearchTree']:
        """
        If you will try to remove root, then you will lose root node. Handle it somehow.

        """

        if value < self.payload:
            if self.left_child:
                return self.left_child.remove_value(value=value)

        elif value > self.payload:
            if self.right_child:
                return self.right_child.remove_value(value=value)

        else:
            if self.right_child and self.left_child:
                print(f'Left child: {self.left_child.payload}')
                new_node = self.__pop_max_el__(root=self.left_child)
                print(f'New node: {new_node.payload}')
                # new_node.left_child = self.left_child
                print(f'Self right child: {self.right_child.payload}')
                new_node.right_child = self.right_child
                new_node.parent = self.parent

                self.replace_nodes(node=new_node)
            elif self.right_child:
                self.replace_nodes(node=self.right_child)

            elif self.left_child:
                self.replace_nodes(node=self.left_child)

            else:
                self.replace_nodes(node=None)

            return self

        return None



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

    child_2_1 = BinarySearchTree(payload=5)
    child_2_2 = BinarySearchTree(payload=12)
    child_2_3 = BinarySearchTree(payload=14)
    child_2_4 = BinarySearchTree(payload=15)

    child_1_1 = BinarySearchTree(payload=1)
    child_1_2 = BinarySearchTree(payload=7)

    root = BinarySearchTree(payload=124)

    root.insert_node(node=child_2_1)
    root.insert_node(node=child_2_2)
    root.insert_node(node=child_2_3)
    root.insert_node(node=child_2_4)
    root.insert_node(node=child_1_1)
    root.insert_node(node=child_1_2)

    print(f'Traverse inorder:')
    traverse_inorder(root=root)
    print(f'Depth first:')
    traverse_depth_first(root=root)

    print(f'=' * 15)
    node = root.find_value(value=124)

    print(node.payload)

    if node.left_child:
        print(f'Left child: {node.left_child.payload}')
    else:
        print(f'No left child')

    if node.right_child:
        print(f'Right child: {node.right_child.payload}')
    else:
        print(f'No right child')

    print(f'=' * 15)
    value = 124
    remove_result = root.remove_value(value=value)

    if remove_result:
        print(f'Resulted node payload: {remove_result.payload}')
    else:
        print(f'There is no such node!')

    print(f'Traverse depth first:')
    traverse_depth_first(root=root)

    print(f'Traverse inorder after removing {value}:')
    traverse_inorder(root=root)
