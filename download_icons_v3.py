import urllib.request
import os

icons = {
    "amplitude": "https://www.vectorlogo.zone/logos/amplitude/amplitude-icon.svg",
    "fullstory": "https://www.vectorlogo.zone/logos/fullstory/fullstory-icon.svg",
    "segment": "https://www.vectorlogo.zone/logos/segment/segment-icon.svg"
}

os.makedirs("assets/integrations", exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0'
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
