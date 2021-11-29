import requests
from parsel import Selector

response = requests.get(
    "https://www.google.com/searchbyimage",
    params={
        "image_url": "https://observatoriodocinema.uol.com.br/wp-content/uploads/2021/08/1586634605500927-img-624452-daniel-radcliffe-em-harry-potter-e-o-enigma-do-principe20140811091407760459-1200x900-1.jpg",
        "hl": "en_GB",
    },
    headers={
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    },
)

with open("page.html", "w") as f:
    f.write(response.text)

selector = Selector(response.text)
for link in selector.xpath('//div[@class="g"]/div/div/div/a/@href').getall():
    print(link)
