from fastapi import FastAPI
from pydantic import BaseModel

from config import llm
from rag.retriever import retrieve, add_feedback
from prompts.feedback_prompt import build_prompt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    

add_feedback([
    "App is slow and crashes",
    "Great UI and smooth experience",
    "Payment failed multiple times"
])


@app.post("/chat")
def chat(req: ChatRequest):
    context = retrieve(req.message)

    prompt = build_prompt(req.message, context)

    response = llm.invoke(prompt)

    return {
        "response": response.content
    }