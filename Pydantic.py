from pydantic import BaseModel, Field
from typing import Literal

class UrgentAction(BaseModel):
    action_required: bool
    deadline_hours: int = Field(description="Hours remaining to resolve, default 24 if unstated", ge=1)


class SupportTicket(BaseModel):
    priority: Literal["low", "medium", "high", "critical"]
    category: str = Field(description="The functional department, e.g., Billing, Tech, Legal")
    actions: UrgentAction

class Node(BaseModel):
    id: int
    label: str = Field(description="The category of entity, e.g., Person, Company")
    name: str

class Edge(BaseModel):
    source: int
    target: int
    relationship_type: Literal["WORKS_AT", "FOUNDED", "ACQUIRED", "PARTNERED_WITH"]

class KnowledgeGraph(BaseModel):
    nodes: list[Node]
    edges: list[Edge]

