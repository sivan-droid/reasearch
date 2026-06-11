from ..graph.graph_builder import build_graph


class ResearchAgent:

    def __init__(self):
        self.graph = build_graph()

    def execute(self, topic: str):

        result = self.graph.invoke(
            {
                "topic": topic
            }
        )

        return result