import os
from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyA5BQwl-AsPmLrbxmBdugZNdMt4Ctu9E0o")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=types.Part.from_text(text='Why is the sky blue?'),
    config=types.GenerateContentConfig(
        temperature=0,
        top_p=0.95,
        top_k=20,
    ),
)

print(response.candidates[0].content.parts[0].text)
