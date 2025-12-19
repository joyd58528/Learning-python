import os
from google import genai
from google.genai import types
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Bill Generator", page_icon="🧾")
st.title("Bill Generator test build")
st.write("Upload an image")
client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
path = input("Enter image path: ")
img = Image.open(path)

uploaded_file = st.file_uploader(
    "Upload bill image",
    type=["jpg","webp", "jpeg", "png"]
)

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
