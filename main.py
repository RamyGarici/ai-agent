import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("Api Key not found")

client = genai.Client(api_key=api_key)
answer =client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="Why is Boot.dev such a great place to learn backend development?" \
    " Use one paragraph maximum.")
if answer.usage_metadata:
    print(f"Prompt tokens: {answer.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {answer.usage_metadata.candidates_token_count}")
else:
    raise RuntimeError("usage_metadata is None")


print(answer.text)