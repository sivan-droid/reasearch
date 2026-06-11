from typing import Any
from langchain_groq import ChatGroq

ResearchState = dict[str, Any]

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)

def research_node(state: ResearchState):

    topic = state["topic"]

    prompt = f"""
    Generate detailed research notes about:

    {topic}

    Include:
    - Introduction
    - Key Concepts
    - Applications
    - Advantages
    - Challenges
    - Future Scope

    Return well-structured content.
    """

    response = llm.invoke(prompt)

    return {
        "research_content": response.content
    }