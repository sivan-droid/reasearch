from fastapi import FastAPI
from pydantic import BaseModel
from research_agent.agents.research_agent import ResearchAgent
from summary_agent.agent.summary_agent import SummarizerAgent
from quiz_generator_agent.agents.quiz_generator_agent import QuizAgent

app = FastAPI()

research_agent = ResearchAgent()
summarizer_agent = SummarizerAgent()
quiz_agent = QuizAgent()

class ResearchRequest(BaseModel):
    topic: str

@app.post("/research")
def research(request: ResearchRequest):
    result = research_agent.execute(request.topic)
    return result

class SummaryRequest(BaseModel):
    research_content: str

@app.post("/summarize")
def summarize(request: SummaryRequest):
    result = summarizer_agent.execute(request.research_content)
    return result

class QuizRequest(BaseModel):
    summary: str


@app.post("/quiz")
def generate_quiz(request: QuizRequest):
    result = quiz_agent.execute(request.summary)
    return result