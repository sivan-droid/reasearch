from langgraph.graph import StateGraph, END

from .state import ResearchState
from .nodes import research_node


def build_graph():

    graph = StateGraph(ResearchState)

    graph.add_node(
        "research_node",
        research_node
    )

    graph.set_entry_point(
        "research_node"
    )

    graph.add_edge(
        "research_node",
        END
    )

    return graph.compile()