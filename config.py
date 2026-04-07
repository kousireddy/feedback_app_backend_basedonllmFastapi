import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    MODEL_NAME = "gemini-2.5-flash"
    TEMPERATURE = 0

settings = Settings()

# LLM instance
llm = ChatGoogleGenerativeAI(
    model=settings.MODEL_NAME,
    temperature=settings.TEMPERATURE,
    google_api_key=settings.GOOGLE_API_KEY
)