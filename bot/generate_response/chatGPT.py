from dotenv import load_dotenv
import os
import openai

load_dotenv("/.env")

openai.organization = os.getenv("ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "The quick brown fox"
model_engine = "gpt-3.5-turbo"

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text
print(message)