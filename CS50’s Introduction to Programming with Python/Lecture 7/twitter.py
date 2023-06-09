import re

url = input("URL: ").strip()

matches = re.match(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)

if matches:
    print(f"Username: {matches.group(1)}")