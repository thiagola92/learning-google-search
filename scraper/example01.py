import json5
import requests
from parsel import Selector

response = requests.get(
    "https://www.google.com/search",
    params={
        "q": "harry potter",
        "tbm": "isch",
    },
    headers={
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    },
)

with open("page.html", "w") as f:
    f.write(response.text)


def search_images(array):
    images = []

    for item in array:
        if isinstance(item, list):
            images.extend(search_images(item))

        if not isinstance(item, str):
            continue

        if not item.startswith("http"):
            continue

        if not item.endswith((".jpg", ".png")):
            continue

        images.append(item)

    return images


selector = Selector(text=response.text)
for script in selector.xpath("//script").getall():
    if "AF_initDataCallback" in script:
        script, _, _ = script.partition(");</script>")
        _, _, script = script.partition("AF_initDataCallback(")
        script = script.strip()

        if not script:
            continue

        data = json5.loads(script)
        for image in search_images(data["data"]):
            print(image)
