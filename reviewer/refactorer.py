from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_refactor_patch(code: str, feedback: str):
    prompt = f"""
Based on the review feedback, generate a git-style patch to refactor the code.

Code:
{code}

Feedback:
{feedback}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
