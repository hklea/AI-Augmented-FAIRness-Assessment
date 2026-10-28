import os
import json
from dotenv import load_dotenv
from openai import OpenAI

def main():
    # Load variables from .env file
    load_dotenv()

    # API
    BASE_URL = "https://kiste.informatik.tu-chemnitz.de/v1"

    # Name of model
    MODEL_ID = "Qwen3.6-35B-A3B-MLX-8bit"

    # API token
    API_KEY = os.getenv("KISTE_API_TOKEN")
    #print(API_KEY)
    if API_KEY is None:
        raise RuntimeError("KISTE_API_TOKEN is not set")

    # Initialize client
    client = OpenAI(
        api_key=API_KEY,
        base_url=BASE_URL,
    )

    SYSTEM_PROMPT = """
    Answer the question in 1 word.
    """.strip()
    question='What is the capital of Germany?'
    messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ]
    tokens=128

    resp = client.chat.completions.create(
                model=MODEL_ID,
                messages=messages,
                temperature=0.0,
                max_tokens=tokens,
            )

    choice = resp.choices[0]
    content = (getattr(choice.message, "content", None) or "").strip()
    finish_reason = getattr(choice, "finish_reason", None)

    print(    
        f"tokens={tokens}, "
        f"finish_reason={finish_reason},\n"
        f"reasoning_content={getattr(choice.message, 'reasoning_content', None)}"
    )

    print("Answer:", content)


if __name__ == "__main__":
    main()
