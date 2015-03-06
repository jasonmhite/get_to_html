import tvnamer
import time
import glob
import os
from jinja2 import Template
from tvnamer.utils import FileParser

TEMPLATE_PATH = './series.template'
SUCCESS_DIR = './stat/success'
FAILURE_DIR = './stat/failure'
TIME_FMT = '%a %b %d %H:%M:%S %Y'

now = time.strftime(TIME_FMT)

shows = []

for filename in glob.iglob(os.path.join(SUCCESS_DIR, '*')):
    with open(filename) as f:
        url = f.read().strip()

    stat = os.stat(filename).st_mtime

    # Song and dance to make the time formats just right...
    t = time.strftime(
        TIME_FMT,
        time.strptime(time.ctime(stat), TIME_FMT),
    )

    show = {
        'filename': os.path.basename(filename),
        'time': t,
        'url': url,
        'epoch': stat,
    }

    try:
        r = FileParser(filename).parse().getepdata()
        show['title'] = r['seriesname']
        show['episode'] = r['episode']

    except tvnamer.tvnamer_exceptions.InvalidFilename as e:
        show['error'] = 2

    finally:
        shows.append(show)

for filename in glob.iglob(os.path.join(FAILURE_DIR, '*')):
    with open(filename) as f:
        url = f.read().strip()

    stat = os.stat(filename).st_mtime

    # Song and dance to make the time formats just right...
    t = time.strftime(
        TIME_FMT,
        time.strptime(time.ctime(stat), TIME_FMT),
    )

    show = {
        'filename': os.path.basename(filename),
        'time': t,
        'url': url,
        'epoch': stat,
        'error': 1,
    }

    shows.append(show)

shows.sort(key=lambda s: - s['epoch'])

with open(TEMPLATE_PATH) as f:
    t = Template(f.read())

print(t.render(shows=shows, now=now))
