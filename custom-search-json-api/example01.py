import os
import pprint

from googleapiclient.discovery import build

service = build("customsearch", "v1", developerKey=os.environ["API_KEY"])

res = service.cse().list(
    q='harry potter',
    cx=os.environ["ENGINE_ID"]
).execute()

pprint.pprint(res)