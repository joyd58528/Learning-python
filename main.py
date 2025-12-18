import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.responses.create(
    model="gpt-5-nano",
    # instructions="Some instructions",
    input="What is the day?",
)

print(response.output_text)