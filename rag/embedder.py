import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",        
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    output_dimensionality=768              
)