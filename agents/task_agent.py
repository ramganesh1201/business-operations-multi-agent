from google import genai
from config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

def prioritize_tasks(tasks):

    prompt = f"""
    Prioritize these tasks.

    Return:

    High:
    Medium:
    Low:

    Tasks:
    {tasks}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text