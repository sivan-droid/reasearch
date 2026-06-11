from langchain_groq import ChatGroq

from .state import QuizState


from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)


def quiz_generator_node(state: QuizState):

    summary = state["summary"]

    prompt = f"""
    You are a quiz generation assistant.

    Based on the summary below, generate 5 multiple-choice questions.

    Requirements:
    - Generate exactly 5 MCQs.
    - Each question should have 4 options (A, B, C, D).
    - Clearly indicate the correct answer.
    - Questions should test understanding, not simple memorization.

    Summary:

    {summary}
    """

    response = llm.invoke(prompt)

    return {
        "quiz": response.content
    }