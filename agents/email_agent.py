from google import genai
from config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)


def summarize_email(email_text):
    prompt = f"""
    Analyze the following email.

    Return:
    1. Summary
    2. Action Items
    3. Deadlines

    Email:
    {email_text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text