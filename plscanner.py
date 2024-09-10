import re
from urllib.parse import urlparse
import requests

# URL validation function
def validate_url(url):
    regex = re.compile(
        r'^(?:http|https)?://'  # http:// or https://
        r'(?:www\.)?'
        r'([a-zA-Z0-9.-]+)'  # Domain name
    )
    return bool(regex.match(url))

# Anomaly detection
def check_domain_anomalies(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if "-" in domain or len(domain) > 30:
        return f"Warning: Suspicious domain detected - {domain}"
    return f"Domain seems fine: {domain}"

# Phishing keywords detection
def check_for_phishing_keywords(url):
    phishing_keywords = ["login", "secure", "account", "update", "verify", "password"]
    if any(keyword in url for keyword in phishing_keywords):
        return "Suspicious URL: Contains phishing-related keywords."
    return "No suspicious keywords found."

import requests

def check_with_google_safe_browsing(url):
    api_key = "AIzaSyCxJ8CJuAZPVzrs6SMeN37v_gnTlfd-S-Q"  # Replace with your actual API key
    safe_browsing_url = "https://safebrowsing.googleapis.com/v4/threatMatches:find?key=" + api_key
    payload = {
        "client": {
            "clientId": "your_client_id",
            "clientVersion": "1.0.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    response = requests.post(safe_browsing_url, json=payload)
    result = response.json()
    if "matches" in result:
        return "Phishing URL found in Google Safe Browsing Database."
    return "URL not found in Google Safe Browsing Database."

# Main function
def phishing_scanner(url):
    if not validate_url(url):
        return "Invalid URL format."
    
    report = []
    report.append(check_domain_anomalies(url))
    report.append(check_for_phishing_keywords(url))
    report.append(check_with_google_safe_browsing(url))
    
    return "\n".join(report)

# Example usage
if __name__ == "__main__":
    url = input("Enter a URL to scan: ")
    print(phishing_scanner(url))
