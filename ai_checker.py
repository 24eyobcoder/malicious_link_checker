import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def check_url_with_chatgpt(url):
    prompt = (
        f"Analyze the following URL and decide if it's dangerous, malicious, scammy, or safe:\n\n"
        f"URL: {url}\n\n"
        f"Only respond with one of the following levels: 'Safe', 'Suspicious', 'Malicious'. "
        f"Then briefly explain why in 2 sentences max."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    reply = response.choices[0].message.content
    print("\n🧠 AI Analysis:")
    print(reply)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="AI-powered Malicious URL Checker using OpenAI")
    parser.add_argument("url", help="URL to analyze")
    args = parser.parse_args()

    check_url_with_chatgpt(args.url)
