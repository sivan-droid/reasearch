from ..graph.graph_builder import build_graph


class SummarizerAgent:

    def __init__(self):
        self.graph = build_graph()

    def execute(self, research_content: str):

        result = self.graph.invoke(
            {
                "research_content": research_content
            }
        )

        return result