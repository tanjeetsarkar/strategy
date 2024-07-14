import uuid
import random
from models import Node as ModelNode
from models import Link as ModelLink
from sqlalchemy.orm.session import Session
from models import SessionLocal

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

    def create_in_db(self, db:Session):
        graph: dict[Node, list[Node]] = {}
        for i in range(self.node_count):
            node = ModelNode(decision=f"Node {i}")
            db.add(node)
            print(node.id)
            graph[node] = []
        db.flush()
        for _ in range(self.edge_count):
            x,y = random.sample(list(graph.keys()), 2)
            link = ModelLink(left=x.id, right=y.id)
            print("left: ", x.id,"right: ", y.id, "linkId: ", link.id)
            db.add(link)
            graph[x].append(y)
        db.flush()
        db.commit()
        return graph


if __name__ == "__main__":
    g = Graph(8,20)
    db = SessionLocal()
    graph = g.create_in_db(db)

