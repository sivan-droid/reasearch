from langgraph.graph import StateGraph, END

from .state import SummaryState
from .nodes import summarize_node


def build_graph():

    graph = StateGraph(SummaryState)

    graph.add_node(
        "summarize_node",
        summarize_node
    )

    graph.set_entry_point(
        "summarize_node"
    )

    graph.add_edge(
        "summarize_node",
        END
    )

    return graph.compile()