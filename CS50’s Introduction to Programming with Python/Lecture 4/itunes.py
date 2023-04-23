import sys
import json
import requests

if len(sys.argv) != 2:
    sys.exit()

URL = f"https://itunes.apple.com/search?entity=song&limit=10&term={sys.argv[1]}"

response = requests.get(URL)
o = response.json()
for result in o["results"]:
    print("Track Name:",result["trackName"])
# print(json.dumps(0,indent=2))
