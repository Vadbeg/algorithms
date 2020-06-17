from typing import Dict, List


def remove_edge(node1: int, node2: int, graph: Dict[int, List[int]]) -> Dict[int, List[int]]:
    if node1 in graph.keys():
        if node2 in graph[node1]:
            graph[node1].remove(node2)

    return graph


def add_edge(node1: int, node2: int, graph: Dict[int, List[int]]) -> Dict[int, List[int]]:
    graph[node1].append(node2)

    return graph


def build_tree_from_node(node: int, graph: Dict[int, List[int]], memory: List) -> Dict[int, List[int]]:
    tree = {}

    tree[node] = graph[node]

    if node in memory:
        return tree
    else:
        memory.append(node)

    for child_node in graph[node]:
        tree.update(build_tree_from_node(child_node, graph, memory))

    return tree


def depth_search(root: int, tree: Dict[int, List[int]], memory: List[int]) -> List[List[int]]:
    paths = list()

    print(f'Root value: {root}')
    if len(tree[root]) == 0 or root in memory:
        paths = [[root]]
        return paths

    memory.append(root)

    for child_node in tree[root]:

        for curr_path in depth_search(child_node, tree, memory):
            paths.append([root] + curr_path)

    return paths


if __name__ == '__main__':

    graph1 = {}

    graph1[0] = []
    graph1[1] = [2]
    graph1[2] = [3]
    graph1[3] = []
    graph1[4] = [1, 3]
    graph1[5] = [6]
    graph1[6] = [7]
    graph1[7] = [5]
    graph1[8] = []
    graph1[9] = [8]

    graph2 = {}

    graph2[1] = [3]
    graph2[2] = [1]
    graph2[3] = [2, 4]
    graph2[4] = [5]
    graph2[5] = [2]


    graph3 = {}
    graph3[0] = [1, 2]
    graph3[1] = []
    graph3[2] = [3]
    graph3[3] = [1, 4]
    graph3[4] = [6]
    graph3[5] = [1, 6]
    graph3[6] = [5, 2]

    # euler_cycle = get_euler_cycles_from_node(node_main=5, graph=graph2)
    NODE = 5

    tree = build_tree_from_node(node=NODE, graph=graph1, memory=[])

    print(f'Tree: {tree}')

    path = depth_search(root=NODE, tree=tree, memory=[])

    print(f'Path: {path}')
