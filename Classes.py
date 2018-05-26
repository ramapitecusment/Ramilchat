import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url):
    print('Downloading:', url)
    try:
        html = urllib.request.urlopen(url).read()
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
    return html

def classes(entities, entity, values):
    try:

        if entity == 'get_class':
            url = 'https://almaty.fh-joanneum.at/stundenplan/'
            try:
                html = urlopen(url).read()
            except urllib2.URLError as e:
                html = None

    except:
        pass