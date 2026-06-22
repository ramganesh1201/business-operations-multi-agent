from google import genai
import json
from config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

def summarize_email(email_text):

    prompt = f"""
    Analyze the email and return ONLY valid JSON.

    Format:

    {{
      "summary": "...",
      "action_items": ["...", "..."],
      "deadlines": ["..."]
    }}

    Email:
    {email_text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)