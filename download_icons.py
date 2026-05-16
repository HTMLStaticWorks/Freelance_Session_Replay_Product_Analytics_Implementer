import urllib.request
import os

icons = {
    "mixpanel": "https://simpleicons.org/icons/mixpanel.svg",
    "amplitude": "https://simpleicons.org/icons/amplitude.svg",
    "hotjar": "https://simpleicons.org/icons/hotjar.svg",
    "fullstory": "https://simpleicons.org/icons/fullstory.svg",
    "segment": "https://simpleicons.org/icons/segment.svg",
    "ga4": "https://simpleicons.org/icons/googleanalytics.svg"
}

os.makedirs("assets/integrations", exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for name, url in icons.items():
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            with open(f"assets/integrations/{name}.svg", "wb") as f:
                f.write(response.read())
        print(f"Downloaded {name}.svg")
    except Exception as e:
        print(f"Failed to download {name}: {e}")
