import os
import pprint
import requests

response = requests.get(
    "https://www.googleapis.com/customsearch/v1",
    params={
        "cx": os.environ["ENGINE_ID"],
        "key": os.environ["API_KEY"],
        "q": "harry potter",
    },
)

pprint.pprint(response.json())
