import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


def main() -> None:
    load_dotenv(Path(__file__).resolve().with_name(".env"))

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY. Copy .env.example to .env and fill it first.")

    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    base_url = os.getenv("OPENAI_API_BASE_URL") or os.getenv("OPENAI_BASE_URL") or None

    client = OpenAI(api_key=api_key, base_url=base_url)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Hello, introduce yourself in one sentence."}],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
