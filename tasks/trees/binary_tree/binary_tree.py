

class BinaryTree:
    def __init__(self, payload: str,
                 left_child: 'BinaryTree' = None,
                 right_child: 'BinaryTree' = None):
        self.left_child = left_child
        self.right_child = right_child

        self.payload = payload


# class BinarySearchTree:
#     def __init__(self):
#         pass
#
#     def add_node(self):