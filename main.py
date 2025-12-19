import os
from google import genai
from google.genai import types
from PIL import Image
import streamlit as st
import json

if "image_bytes" not in st.session_state:
    st.session_state["image_bytes"] = None

if "result" not in st.session_state:
    st.session_state["result"] = None

if "raw" not in st.session_state:
    st.session_state["raw"] = None

if "processing" not in st.session_state:
    st.session_state["processing"] = False

st.set_page_config(page_title="Bill Generator", page_icon="🧾", layout="wide")
st.title("Bill Generator test build")
st.write("Upload an image")

client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))

input_col, output_col = st.columns(2)

#input
with input_col:
    uploaded_file = st.file_uploader(
        "Upload bill image",
        type=["jpg","webp", "jpeg", "png"]
    )
    if uploaded_file and st.session_state.image_bytes is None:
        st.session_state.image_bytes = uploaded_file.getvalue()

    if st.session_state.image_bytes:
        st.image(st.session_state.image_bytes, use_column_width=True)

#output 
with output_col:
    if st.session_state.image_bytes:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                types.Part.from_text(text="Only provide the Bill number, Date, and the total amount provide it as an .json object. Do not include any other text. and also use camel case."),
                types.Part.from_bytes(data=st.session_state.image_bytes, mime_type="image/jpeg")

            ],
            config=genai.types.GenerateContentConfig(
                temperature=0,
                top_p=0.95,
                top_k=20,
            )
        )
        def clean_json(text: str) -> str:
            text = text.strip()
            if text.startswith("```json"):
                text = text.replace("```json", "").replace("```", "").strip()
            if text.lower().startswith("json:"):
                text = text[4:].strip()
            return text