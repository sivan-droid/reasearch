from langchain_groq import ChatGroq

from .state import SummaryState

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)


def summarize_node(state: SummaryState):

    research_content = state["research_content"]

    prompt = f"""
    You are a professional summarization assistant.

    Summarize the following research content.

    Requirements:
    - Keep the summary concise.
    - Cover all important concepts.
    - Use bullet points where appropriate.
    - Limit the summary to approximately 200-300 words.

    Research Content:

    {research_content}
    """

    response = llm.invoke(prompt)

    return {
        "summary": response.content
    }