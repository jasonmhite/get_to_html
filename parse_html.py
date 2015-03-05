import feedparser
import tvnamer
import time
from jinja2 import Template
from tvnamer.utils import FileParser

TEMPLATE_PATH='./series.template'
URL = 'http://downloader/series.rss'

now = time.strftime('%a, %d %b %Y:%M:%S %Z')

d = feedparser.parse(URL)['entries']

shows = []
for entry in d:

    pub_time = time.strftime(
        '%a, %d %b %Y:%M:%S %Z',
        entry['published_parsed'],
    )

    show = {
        'filename': entry['title'],
        'time': pub_time,
        'url': entry['link'],
    }

    try:
        r = FileParser(entry['title']).parse().getepdata()

        show['title'] = r['seriesname']
        show['episode'] = r['episode']

    except tvnamer.tvnamer_exceptions.InvalidFilename as e:
        print("Error parsing {}: {}".format(entry['title'], e))
        show['error'] = str(e)

    finally:
        shows.append(show)

with open(TEMPLATE_PATH) as f:
    t = Template(f.read())

print(t.render(shows=shows, now=now))
