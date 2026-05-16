import urllib.request
import os

icons = {
    "mixpanel": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/mixpanel.svg",
    "amplitude": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/amplitude.svg",
    "hotjar": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/hotjar.svg",
    "fullstory": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/fullstory.svg",
    "segment": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/segment.svg",
    "ga4": "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/googleanalytics.svg"
}

os.makedirs("assets/integrations", exist_ok=True)

for name, url in icons.items():
    try:
        with urllib.request.urlopen(url) as response:
            with open(f"assets/integrations/{name}.svg", "wb") as f:
                f.write(response.read())
        print(f"Downloaded {name}.svg")
    except Exception as e:
        print(f"Failed to download {name}: {e}")
