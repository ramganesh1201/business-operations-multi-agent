from google import genai
from config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

def generate_report(summary, priorities):
    prompt = f"""
    Create a professional business report.

    Email Analysis:
    {summary}

    Prioritized Tasks:
    {priorities}

    Include:
    - Executive Summary
    - Key Action Items
    - Risks
    - Recommendations
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text