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

# ( Using Google SAfe Browing Database)
def check_with_phishtank(url):
    api_key = "AIzaSyCxJ8CJuAZPVzrs6SMeN37v_gnTlfd-S-Q"  # Safe Browsing Api Key
    response = requests.post(
        "http://checkurl.phishtank.com/checkurl/",
        data={"url": url, "format": "json", "app_key": api_key}
    )
    result = response.json()
    if result["results"]["in_database"]:
        return "Phishing URL found in PhishTank."
    return "URL not found in PhishTank."

# Main function
def phishing_scanner(url):
    if not validate_url(url):
        return "Invalid URL format."
    
    report = []
    report.append(check_domain_anomalies(url))
    report.append(check_for_phishing_keywords(url))
    
    
    return "\n".join(report)

# Example usage
if __name__ == "__main__":
    url = input("Enter a URL to scan: ")
    print(phishing_scanner(url))
