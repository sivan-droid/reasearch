from langgraph.graph import StateGraph, END

from .state import QuizState
from .nodes import quiz_generator_node


def build_graph():

    graph = StateGraph(QuizState)

    graph.add_node(
        "quiz_generator_node",
        quiz_generator_node
    )

    graph.set_entry_point(
        "quiz_generator_node"
    )

    graph.add_edge(
        "quiz_generator_node",
        END
    )

    return graph.compile()