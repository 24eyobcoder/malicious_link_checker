import requests
import schedule
import time

def download_phishtank_csv(file_path='verfied_online.csv'):
    url = "http://data.phishtank.com/data/online-valid.csv"
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
        print(f"[✅ CSV Updated] Saved to {file_path}")
    else:
        print(f"[❌ Failed] Status: {response.status_code}")

# Schedule to run once a day
schedule.every().day.at("01:00").do(download_phishtank_csv)

print("🕒 Waiting for scheduled downloads...")
while True:
    schedule.run_pending()
    time.sleep(60)
