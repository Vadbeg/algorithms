"""Tinkoff trees task"""

from typing import Dict


class Node:
    def __init__(self, value_a):
        self.value_a = value_a
        self.children_and_distance: Dict['Node', int] = {}

    def add_child(self, node, distance):
        self.children_and_distance[node] = distance


def solve_tinkoff_task(root: Node):
    children_to_remove = []
    children_to_add_and_distance = {}

    for child, distance in root.children_and_distance.items():
        if len(child.children_and_distance) != 0:
            solve_tinkoff_task(root=child)

            children_to_remove_from_child = []

            for grand_child, grand_distance in child.children_and_distance.items():
                if grand_distance + distance <= grand_child.value_a:
                    children_to_add_and_distance[grand_child] = grand_distance + distance

                if grand_distance > grand_child.value_a:
                    children_to_remove_from_child.append(grand_child)

            for grand_child in children_to_remove_from_child:
                child.children_and_distance.pop(grand_child, None)

        if distance > child.value_a:
            children_to_remove.append(child)

    for child in children_to_remove:
        root.children_and_distance.pop(child, None)

    for child, distance in children_to_add_and_distance.items():
        root.children_and_distance[child] = distance


def test_case1():
    root = Node(value_a=1)

    node_2 = Node(value_a=2)
    node_3 = Node(value_a=5)

    node_4 = Node(value_a=7)
    node_5 = Node(value_a=4)

    node_2.add_child(node=node_4, distance=7)
    node_2.add_child(node=node_5, distance=6)

    root.add_child(node=node_2, distance=2)
    root.add_child(node=node_3, distance=6)

    solve_tinkoff_task(root=root)

    all_lengths = []
    for curr_node in [root, node_2, node_3, node_4, node_5]:
        print(curr_node.value_a)
        for child, distance in curr_node.children_and_distance.items():
            print("  ", child.value_a, distance)
        print('-' * 10)

        all_lengths.append(len(curr_node.children_and_distance))
    print('*' * 10)

    assert all_lengths == [1, 1, 0, 0, 0]


def test_case2():
    root = Node(value_a=1)

    node_2 = Node(value_a=2)
    node_3 = Node(value_a=4)
    node_4 = Node(value_a=6)
    node_5 = Node(value_a=8)

    root.add_child(node=node_2, distance=2)
    node_2.add_child(node=node_3, distance=2)
    node_3.add_child(node=node_4, distance=2)
    node_4.add_child(node=node_5, distance=2)

    solve_tinkoff_task(root=root)

    all_lengths = []
    for curr_node in [root, node_2, node_3, node_4, node_5]:
        print(curr_node.value_a)
        for child, distance in curr_node.children_and_distance.items():
            print("  ", child.value_a, distance)
        print('-' * 10)

        all_lengths.append(len(curr_node.children_and_distance))
    print('*' * 10)

    assert all_lengths == [4, 3, 2, 1, 0]


def test_case3():
    root = Node(value_a=1)

    node_2 = Node(value_a=2)
    node_3 = Node(value_a=4)

    root.add_child(node=node_2, distance=2)
    node_2.add_child(node=node_3, distance=2)

    solve_tinkoff_task(root=root)

    all_lengths = []
    for curr_node in [root, node_2, node_3]:
        print(curr_node.value_a)
        for child, distance in curr_node.children_and_distance.items():
            print("  ", child.value_a, distance)
        print('-' * 10)

        all_lengths.append(len(curr_node.children_and_distance))
    print('*' * 10)

    assert all_lengths == [2, 1, 0]


def test_case4():
    root = Node(value_a=1)

    node_2 = Node(value_a=2)
    node_3 = Node(value_a=2)

    root.add_child(node=node_2, distance=2)
    root.add_child(node=node_3, distance=100)

    solve_tinkoff_task(root=root)

    all_lengths = []
    for curr_node in [root, node_2, node_3]:
        print(curr_node.value_a)
        for child, distance in curr_node.children_and_distance.items():
            print("  ", child.value_a, distance)
        print('-' * 10)

        all_lengths.append(len(curr_node.children_and_distance))
    print('*' * 10)

    assert all_lengths == [1, 0, 0]


def test_case5():
    root = Node(value_a=1)

    node_2 = Node(value_a=2)
    node_3 = Node(value_a=2)

    root.add_child(node=node_2, distance=100)
    root.add_child(node=node_3, distance=100)

    solve_tinkoff_task(root=root)

    all_lengths = []
    for curr_node in [root, node_2, node_3]:
        print(curr_node.value_a)
        for child, distance in curr_node.children_and_distance.items():
            print("  ", child.value_a, distance)
        print('-' * 10)

        all_lengths.append(len(curr_node.children_and_distance))
    print('*' * 10)

    assert all_lengths == [0, 0, 0]


def test_case6():
    root = Node(value_a=1)

    node_2 = Node(value_a=2)
    node_3 = Node(value_a=2)

    node_4 = Node(value_a=10_000)

    root.add_child(node=node_2, distance=1)
    root.add_child(node=node_3, distance=100)

    node_3.add_child(node=node_4, distance=5)

    solve_tinkoff_task(root=root)

    all_lengths = []
    for curr_node in [root, node_2, node_3, node_4]:
        print(curr_node.value_a)
        for child, distance in curr_node.children_and_distance.items():
            print("  ", child.value_a, distance)
        print('-' * 10)

        all_lengths.append(len(curr_node.children_and_distance))
    print('*' * 10)

    assert all_lengths == [2, 0, 1, 0]


if __name__ == "__main__":
    test_case1()
    test_case2()
    test_case3()
    test_case4()
    test_case5()
    test_case6()
