# strategy is going to be a multi-headed linked list which will act as graph.
# each node will contain links to other nodes in list (as it can be changed). 
# each node will have a call back function which will define the functionality of the node.


from typing import List
import random
import uuid

class Node:

    def __init__(self, data, inward:list = [], outward:list=[]) -> None:
        self.data = data
        self.inward = inward
        self.outward = outward

    def node_type(self):
        if len(self.outward) and not len(self.inward):
            return "INPUT"
        elif len(self.inward) and not len(self.outward):
            return "OUTPUT"
        elif not len(self.inward) and not len(self.outward):
            return "ISOLATED"
        else:
            return "PROCESSING"

    def clear_links(self):
        self.inward = []
        self.outward = []

    def __repr__(self) -> str:
        return uuid.uuid4().hex

class StrategyGraph:

    def __init__(self, nodes: List[Node]= []) -> None:
        self.nodes = nodes

    def add_node(self, data, from_:List[Node] = [], to_:List[Node] = []) -> Node:
        new_node = Node(data=data, inward=from_, outward=to_)
        self.nodes.append(new_node)
        return new_node

    def del_node(self, node:Node):
        froms = node.inward
        tos = node.outward
        for x_node in froms:
            print("Node Type:", x_node.node.node_type)
            x_node.outward.extend(tos)
        for y_node in tos:
            print("Node Type:", y_node.node.node_type)
            y_node.inward.extend(froms)
        node.clear_links()

    def print_graph(self):
        for node in self.nodes:
            print("\t",node,node.node_type(), " <------ ", node.inward)
            print("\t","|")
            print("\t","------> ", node.outward)
            print()

if __name__ == "__main__":
    sg = StrategyGraph()
    for i in range(10):
        from_nodes = random.sample(sg.nodes, random.randint(0,i))
        to_nodes = random.sample(sg.nodes, random.randint(0,i))
        sg.add_node(i, from_=from_nodes, to_=to_nodes)
    sg.print_graph()



