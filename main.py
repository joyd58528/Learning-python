import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="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",)

response = client.responses.create(
    model="gpt-5-nano",
    # instructions="Some instructions",
    input="What is the day?",
)

print(response.output_text)