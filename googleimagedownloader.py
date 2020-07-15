#importing packages
from selenium import webdriver
import requests as rq
import os
from PIL import Image
import io
import hashlib as hl

#driver-path
path = './chromedriver'
#image-folder-path
img_path = './img/'
#image-query-baseUrl
url = 'https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img'

#fetching urls
def urls():
    driver.get(url.format(q=q))
    links, count, start = set(), 0, 0
    while count < n:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        result = driver.find_elements_by_css_selector("img.Q4LuWd")
        num_results = len(result)
        for i in result[start: num_results]:
            try:
                i.click()
            except Exception as e:
                continue
            images = driver.find_elements_by_css_selector('img.n3VNCb')
            for image in images:
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    links.add(image.get_attribute('src'))
            count = len(links)
            if len(links) >= n:
                print('Found: ', {len(links)}, ' urls,initiating download')
                break
        else:
            print('Found:', len(links), ' Searching more ...')
            return
            load = driver.find_element_by_css_selector('.mye4qd')
            if load:
                driver.execute_script("document.querySelector('.mye4qd').click();")
    return links

#saving images to image-folder
def save(folder, file, url):
    try:
        image = rq.get(url).content
        imgfile = io.BytesIO(image)
        img = Image.open(imgfile).convert('RGB')
        folder = os.path.join(folder, file)
        if os.path.exists(folder):
            file = os.path.join(folder, hl.sha1(image).hexdigest()[:10] + '.jpg')
        else:
            os.mkdir(folder)
            file = os.path.join(folder, hl.sha1(image).hexdigest()[:10] + '.jpg')
        with open(file, 'wb') as f:
            img.save(f, 'JPEG', quality=100)
        print('Downloaded ', {url}, ' - ', {file})
    except Exception as e:
        print('Unable to get - ', {e})


while True:
    qs = list(input('Enter Topic: ').strip().split(","))#topic input
    n = int(input('Number of Images: ')) #no_of_images
    for q in qs:
        links = list()
        driver = webdriver.Chrome(executable_path=path) #webdriver(Chrome)
        driver.get('https://www.google.com') #opening google
        search = driver.find_element_by_css_selector('input.gLFyf') #search_button
        search.send_keys(q) #initiating search
        links = urls() #fetching url
        driver.quit() #exiting browser
        for i in links:
            save(img_path, q, i) #saving images
    x = input('Do you wanna end? [y or n]: ').lower() #continue or not
    if x == 'yes' or x == 'y':
        break
