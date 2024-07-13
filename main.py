# strategy is going to be a multi-headed linked list which will act as graph.
# each node will contain links to other nodes in list (as it can be changed). 
# each node will have a call back function which will define the functionality of the node.

import uuid
import random

class Node:

    def __init__(self, decision) -> None:
        self.decision = decision
        self.id = uuid.uuid4().hex

    def __repr__(self) -> str:
        return self.decision

class Link:

    def __init__(self, left:Node, right:Node) -> None:
        self.left = left
        self.right = right

class Graph:
    def __init__(self, node_count:int, edge_count:int) -> None:
        self.node_count = node_count
        self.edge_count = edge_count


    def create(self):
        graph: dict[Node, list[Node]] = {}

        for i in range(self.node_count):
            node = Node(decision=f"Node {i}")
            graph[node] = []

        for _ in range(self.edge_count):
            x,y = random.sample(list(graph.keys()), 2)
            graph[x].append(y)

        return graph


if __name__ == "__main__":
    g = Graph(8,20)
    graph = g.create()
    print(graph)
