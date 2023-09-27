import html_diff
import shutil
import sys
import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from loguru import logger

logger.remove()
logger.add(sys.stderr, level="INFO")

# crawl old/new
ret = crawl('introduction-to-datascience/dev/index.html')
for fn in ret['pages']:
    print(fn)
for img in ret['images']:
    print(img)

# take in 3 folder names (old, new, dif)
old_dir = sys.argv[1]
new_dir = sys.argv[2]
dif_dir = sys.argv[3]


# take three folder names, find paired HTML files in each

file_triplets = []
for (dirpath, dirnames, filenames) in os.walk(dir1):
    for filename in filenames:
        if filename.endswith('.html'):
            path1 = os.sep.join([dirpath, filename])
            relpath = os.path.relpath(path1, dir1)
            path2 = os.sep.join([dir2, relpath])
            path3 = os.sep.join([dir3, relpath])
            if os.path.exists(path2):
                file_triplets.append( (path1, path2, path3) )

# copy the first directory structure but with a new name
shutil.copytree(dir2, dir3)
# copy the new js/css files
shutil.copy('jupyter-book-diff.css', os.sep.join([dir3, '_static/jupyter-book-diff.css']))
shutil.copy('jupyter-book-diff.js', os.sep.join([dir3, '_static/jupyter-book-diff.js']))
# run the diffs and inject the new js/css into the files
for f1, f2, f3 in file_triplets:
    print('Diffing and saving')
    print((f1, f2, f3))
    with open(f1, 'r') as f:
        html1 = f.read()
    with open(f2, 'r') as f:
        html2 = f.read()
    hdf = html_diff.diff(html1, html2)
    soup = BeautifulSoup(hdf, 'html.parser')
    js_soup = BeautifulSoup('<script src="_static/jupyter-book-diff.js"></script>', 'html.parser')
    css_soup = BeautifulSoup('<link rel="stylesheet" href="_static/jupyter-book-diff.css" type="text/css"/>', 'html.parser')
    soup.find("head").append(js_soup)
    soup.find("head").append(css_soup)
    with open(f3, 'w') as f:
        f.write(str(soup))

# TODO: open each new html diff, look for <a> elements that point to local files
# if those local files have a diff, tag the <a> element with class link-diff-highlight
# found_diffs = len(soup.find_all('.bd-main ins') + soup.find_all('.bd-main del')) > 0
