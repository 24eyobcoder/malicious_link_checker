import requests


def check_phishtank_url(url, csv_file='verified_online.csv'):
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            for line in f:
                if url in line:
                    print(f"[⚠️ MALICIOUS] {url} found in PhishTank!")
                    return True
        print(f"[✅ SAFE] {url} not found.")
        return False
    except FileNotFoundError:
        print("[❌ ERROR] CSV file missing. Download it first.")
        return False
# Call the function to check the URL against PhishTank

