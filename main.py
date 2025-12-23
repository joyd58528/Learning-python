import os
from google import genai
from google.genai import types
import streamlit as st
import json

if "image_bytes" not in st.session_state:
    st.session_state["image_bytes"] = None

if "result" not in st.session_state:
    st.session_state["result"] = None

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
        st.image(st.session_state.image_bytes, use_container_width=True)

#output 
with output_col:
    if st.session_state.image_bytes:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                types.Part.from_text(text="Only provide the Bill number, Date (sometimes it is provide in the format DD/MM/YYYY current year is 2025.), Shop name (also sometimes there could be the company name as well always ignore it), quantity and the total amount provide it as an .json object. Do not include any other text. and also use camel case."),
                types.Part.from_bytes(data=st.session_state.image_bytes, mime_type="image/jpeg")

            ],
            config=genai.types.GenerateContentConfig(
                temperature=0,
                top_p=0.95,
                top_k=20,
            )
        )
        st.session_state.result = response.text
        def clean_json(text: str) -> str:
            text = text.strip()
            if text.startswith("```json"):
                text = text.replace("```json", "").replace("```", "").strip()
            if text.lower().startswith("json:"):
                text = text[4:].strip()
            return text

        file=json.loads(clean_json(st.session_state.result))
        st.header("")

        st.header("")

        st.header("")

        st.header("")

        st.header(f"Bill Number:  {file.get('billNumber', 'N/A')}")

        st.header(f"Date:         {file.get('date', 'N/A')}")

        st.header(f"Total Amount: {file.get('totalAmount', 'N/A')}")

        st.header(f"Shop Name:    {file.get('shopName', 'N/A')}")

        st.header(f"Quantity:     {file.get('quantity', 'N/A')}")

