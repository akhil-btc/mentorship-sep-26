import os
import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

load_dotenv()
api_key = os.getenv("NEWSAPI_KEY")

SUMMARIZER_SYSTEM = (
    "You are a friendly summarizer. Rewrite this news headline in one "
    "sentence for a 10th grader who is not into tech. Keep it under 20 "
    "words. Output only the rewritten sentence, nothing else."
)

if not api_key:
    print("Missing API key. Add NEWSAPI_KEY to your .env file.")
else:
    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "country": "us",
        "category": "technology",
        "pageSize": 5,
    }

    headers = {"X-Api-Key": api_key}

    try:
        response = requests.get(
            url, params=params, headers=headers, timeout=10
        )

        if response.status_code == 429:
            print("Rate limit reached. Try again later.")
        else:
            response.raise_for_status()
            articles = response.json()["articles"]

            text = ""

            for article in articles[:5]:
                text += f"Title: {article['title']}\n"
                text += f"Source: {article['source']['name']}\n"
                text += f"URL: {article['url']}\n\n"

            console = Console()
            console.print(
                Panel(text or "No articles found.", title="Today's Tech")
            )

    except requests.RequestException:
        print("Could not get the news. Check your connection or API key.")

def rewrite_headline(client, original_title):
    """
    Ask the LLM to rewrite a headline. Return the rewritten text.
    On any failure, fall back to the original headline so the
    script still produces useful output.
    """
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": SUMMARIZER_SYSTEM},
                {"role": "user",   "content": original_title},
            ],
            temperature=0.3,    # low temp -> consistent, factual summaries
            max_tokens=80,
        )
        return response.choices[0].message.content.strip()
    except Exception as err:
        print(f"Groq error on '{original_title[:40]}...': {err}")
        return original_title
