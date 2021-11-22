import re
import requests

from urllib.parse import urlparse, urljoin, parse_qs

response = requests.get("https://www.google.com/search", params={
    'q': "harry potter"
})

results = re.findall(r'a href="(/url\?q=.*?)"', response.text)

if results:
    for r in results:
        url = urljoin('https://www.google.com', r)
        part = urlparse(r)
        p = parse_qs(part.query)
        q = p.get('q')

        if isinstance(q, list) and len(q) > 0:
            print(q[0])

