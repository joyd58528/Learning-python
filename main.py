import os
from google import genai
from google.genai import types
from PIL import Image

# client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
client = genai.Client(api_key="GEMINI_API_KEY")
path = input("Enter image path: ")
img = Image.open(path)

response = client.models.generate_content(
    model="gemini-2.5-flash",
      contents=[
        "Only provide the Bill number, Date, and the total amount provide it as an .json object. Do not include any other text. and also use camel case.",
        img
    ],
    config=genai.types.GenerateContentConfig(
        temperature=0,
        top_p=0.95,
        top_k=20,
    )
)

keep = ["billNumber", "date", "totalAmount"]

print(response.candidates[0].content.parts[0].text)
