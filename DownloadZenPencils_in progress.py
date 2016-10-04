
import os, requests, bs4


url = 'http://zenpencils.com/comic/1-ralph-waldo-emerson-make-them-cry/'

os.makedirs('/Users/<username>/zepe', exist_ok=True)

while not url.endswith('#'):
    #TODO: Download the page
    print ('Downloading page %s...' %url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    #TODO: Find the URL of the comic image

    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Couldn\'t find comic image')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            #Download the image
            print('Downloading image %s...'%(comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            #skip this comic
            nextLink = soup.select('a[class="navi comic-nav-next navi-next"]')[0]
            url = nextLink.get('href')
            continue


    #TODO: Save the image to ./zepe
    imageFile = open(os.path.join('/Users/<username>/zepe', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    #TODO: Get the Next button's url.
    nextLink = soup.select('a[class="navi comic-nav-next navi-next"]')[0]
    url = nextLink.get('href')

print ('Done!')






