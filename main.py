import os
from google import genai
from google.genai import types
from PIL import Image

# client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
client = genai.Client(api_key="AIzaSyA5BQwl-AsPmLrbxmBdugZNdMt4Ctu9E0o")
path = input("Enter image path: ")
img = Image.open(path)

response = client.models.generate_content(
    model="gemini-2.5-flash",
      contents=[
        "Only provide the Date, Bill number and the total amount",
        img
    ],
    config=genai.types.GenerateContentConfig(
        temperature=0,
        top_p=0.95,
        top_k=20,
    )
)

print(response.candidates[0].content.parts[0].text)
