from ..graph.graph_builder import build_graph


class QuizAgent:

    def __init__(self):
        self.graph = build_graph()

    def execute(self, summary: str):

        result = self.graph.invoke(
            {
                "summary": summary
            }
        )

        return result