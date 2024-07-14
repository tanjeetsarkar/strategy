import strawberry
from typing import List
from strawberry.types import Info

from models import Node, Link, Rule

@strawberry.type
class NodeType:
    id: int
    decision: dict

@strawberry.type
class LinkType:
    id: int
    left: int
    right: int

@strawberry.type
class RuleType:
    id: int
    rule: dict

@strawberry.type
class Query:
    @strawberry.field
    def get_nodes(self, info: Info) -> List[NodeType]:
        db = info.context["db"]
        return db.query(Node).all()

    @strawberry.field
    def get_edges(self, info: Info) -> List[LinkType]:
        db = info.context["db"]
        return db.query(Link).all()

    @strawberry.field
    def get_rules(self, info: Info) -> List[RuleType]:
        db = info.context["db"]
        return db.query(Rule).all()

@strawberry.type
class Mutation:

    @strawberry.mutation
    def add_node(self, info: Info, decision: dict) -> NodeType:
        db = info.context["db"]
        node = Node(decision=decision)
        db.add(node)
        db.commit()
        db.refresh(node)
        return node

    @strawberry.mutation
    def add_edge(self, info: Info, left: int, right:int) -> LinkType:
        db = info.context["db"]
        edge = Link(left=left, right=right)
        db.add(edge)
        db.commit()
        db.refresh(edge)
        return edge

    @strawberry.mutation
    def add_rule(self, info: Info, rule: dict) -> RuleType:
        db = info.context["db"]
        rule = Rule(rule=rule)
        db.add(rule)
        db.commit()
        db.refresh(rule)
        return rule

