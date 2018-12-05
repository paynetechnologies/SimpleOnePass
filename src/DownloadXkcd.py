# Download pages with the requests module.
# Find the URL of the comic image for a page using Beautiful Soup.
# Download and save the comic image to the hard drive with iter_content().
# Find the URL of the Previous Comic link, and repeat.

import requests
import bs4
import os

url = 'http://xkcd.com'                 # source
os.makedirs('xkcd', exist_ok=True)      # store comics

while not url.endswith('#'):
    # Find the URL of the comic image for a page using Beautiful Soup.
    print('downloading page %s...' % url)

    r = requests.get(url)
    r.raise_for_status()

    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    #find the image
    comicElem = soup.select('#comic img')

    if comicElem == []:
        print('Could not find comic image')
    else:
        comicURL = 'http:' + comicElem[0].get('src')

        # Download and save the comic image to the hard drive with iter_content().

        print ('downloading image %s...' % (comicURL))
        r = requsummests.get(comicURL)
        r = requsummests.get(comicURL)
        r.raise_for_status()

        # save image to disk
        imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
        for chunk in r.iter_content(1000000):
            imageFile.write(chunk)
        imageFile.close()

        # Find the URL of the Previous Comic link, and repeat.
        prevLink = soup.select('a[rel="prev"]')[0]
        #if prevLink not None:
        url = 'http://xkcd.com' + prevLink.get('href')


print('done...')

