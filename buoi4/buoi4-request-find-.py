import requests
import re

def extract_email(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.text
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, data)
        return emails
    except requests.RequestException as e:
        print(f"Error: {e}")
        return set()

if __name__ == '__main__':
    url = "https://utc.edu.vn/#footer"
    emails = extract_email(url)
    for email in emails:
        print(email)
