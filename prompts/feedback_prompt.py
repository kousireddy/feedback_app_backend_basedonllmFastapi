def build_prompt(user_input, context):
    return f"""
You are a smart feedback analysis assistant.

User Feedback:
{user_input}

Relevant Past Feedback:
{context}

Tasks:
1. Classify sentiment (positive, negative, neutral)
2. Extract key issues
3. Suggest improvements
4. Give a short summary

Answer clearly.
"""