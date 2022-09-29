from typing import Hashable, Mapping, Union
import networkx as nx
from collections import deque
import matplotlib.pyplot as plt


def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)

    nx.draw_networkx_labels(graph, pos)

    for edge in graph.edges:
        nx.draw_networkx_edges(
            graph, pos,
            edgelist=[(edge[0], edge[1])], connectionstyle="arc3,rad=0.2"
            )

    plt.show()


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """

    draw_graph(g)
    path_node = []
    visited_nodes = {node: False for node in g.nodes}
    wait_nodes = []

    def recursion_dfs(current_node):
        if visited_nodes[current_node]:
            return None
        visited_nodes[current_node] = True
        path_node.append(current_node)
        neighbours = g[current_node]
        for neighbour in neighbours:
            if not visited_nodes[neighbour]:
                recursion_dfs(neighbour)
        return path_node

