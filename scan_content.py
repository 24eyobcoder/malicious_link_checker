import requests
from bs4 import BeautifulSoup

# Define suspicious indicators
PHISHING_KEYWORDS = [
    "login", "verify", "password", "confirm", "account",
    "signin", "secure", "ssn", "credit card", "bank", "update info"
]

SUSPICIOUS_DOMAINS = ["bit.ly", "tinyurl.com", "rb.gy", "goo.gl", "t.co"]  # Shorteners

def scan_content(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; PhishingScanner/1.0)"
        }
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            print(f"❌ Failed to load page. Status code: {response.status_code}")
            return

        content = response.text.lower()

        # Keyword-based phishing indicator detection
        keyword_hits = [kw for kw in PHISHING_KEYWORDS if kw in content]

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")
        forms = soup.find_all("form")
        has_insecure_form = any("https" not in form.get("action", "") for form in forms if form.get("action"))

        # Check for suspicious domains (shortened links etc.)
        if any(short in url for short in SUSPICIOUS_DOMAINS):
            print("⚠️ URL uses a suspicious shortener domain.")

        if keyword_hits:
            print(f"⚠️ Found suspicious keywords: {', '.join(keyword_hits)}")

        if has_insecure_form:
            print("⚠️ Found a login form without HTTPS.")

        if not keyword_hits and not has_insecure_form:
            print("✅ No obvious phishing indicators detected.")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to URL: {e}")
    except Exception as ex:
        print(f"❌ Unexpected error during scanning: {ex}")
