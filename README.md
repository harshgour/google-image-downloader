# Google Image Downloader

Hello World!
I was trying to simplify multiple image downloads from google on just one click using web scraping for my recent project.

I have used `Selenium` - A web testing tool for image scraping.

Instructions:

```
# Cloning directory - 
- git clone https://github.com/harshgour/image_downloader.git
- cd image-downloader

# Installing packages
Using Command Line or Terminal :
- Open cmd in working/ cloned directory
- Commands:
  $pip install <package-name>
```

***

Packages used are:

```
from selenium import webdriver
import requests as rq
import os
from PIL import Image
import io
import hashlib as hl
```

###### Selenium

Selenium is a suite of tools for automating web browsers. It is a tool that lets anybody automate process of web browsing and it do what is done manually such as searching, downloading etc.

###### Web Driver

Web driver i used is for Chrome Version: 83.0.4103.116
- If your version is different please download compatible web driver

To check version of your browser - 
- Chrome Settings -> About Google Chrome

#User inputs and function call - 

```
while True:
    q = input('Enter Topic: ')
    n = int(input('Number of Images: '))
    driver = webdriver.Chrome(executable_path=path)
    driver.get('https://www.google.com') 
    search = driver.find_element_by_css_selector('input.gLFyf')
    search.send_keys(q)
    links = urls()
    driver.quit() 
    for i in links:
        save(img_path, q, i)
    x = input('Do you wanna end? [y or n]: ').lower() #continue or not
    if x == 'yes' or x == 'y':
        break
```

#fetching-urls

- Function urls() fetch the urls of the images by running the query using class-selectors. It returns links to the main loop which further goes for downloading.
  
  Selectors used - 
   'img.Q4LuWd', 'img.n3VNCb'
  
  Required variables - 
  links - urls for the image
  count - Number of images that are fetched using selectors
  images - img_tags n HTML
  num_results - number of resulting image's tags

```
def urls():
    driver.get(url.format(q=q))
    links, count, start = set(), 0, 0
    while count < n:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        result = driver.find_elements_by_css_selector("img.Q4LuWd")
        num_results = len(result)
        for i in result[start: num_results]:
            i.click()
            images = driver.find_elements_by_css_selector('img.n3VNCb')
            for image in images:
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    links.add(image.get_attribute('src'))
            count = len(links)
            if len(links) >= n:
                print(f'Found: {len(links)} urls, initiating download')
                break
        else:
            print('Found:', len(links), ' Searching more ...')
            return
            load = driver.find_element_by_css_selector('.mye4qd')
            if load:
                driver.execute_script("document.querySelector('.mye4qd').click();")
    return links
```

#saving-images

```
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
        print(f'Downloaded {url} - {file}')
    except Exception as e:
        print(f'Unable to get - {e}')
```
***

# Complete Code - 

```
from selenium import webdriver
import requests as rq
import os
from PIL import Image
import io
import hashlib as hl

path = './chromedriver'
img_path = './img/'
url = 'https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img'

def urls():
    driver.get(url.format(q=q))
    links, count, start = set(), 0, 0
    while count < n:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        result = driver.find_elements_by_css_selector("img.Q4LuWd")
        num_results = len(result)
        for i in result[start: num_results]:
            i.click()
            images = driver.find_elements_by_css_selector('img.n3VNCb')
            for image in images:
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    links.add(image.get_attribute('src'))
            count = len(links)
            if len(links) >= n:
                print(f'Found: {len(links)} urls, initiating download')
                break
        else:
            print('Found:', len(links), ' Searching more ...')
            return
            load = driver.find_element_by_css_selector('.mye4qd')
            if load:
                driver.execute_script("document.querySelector('.mye4qd').click();")
    return links

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
        print(f'Downloaded {url} - {file}')
    except Exception as e:
        print(f'Unable to get - {e}')


while True:
    q = input('Enter Topic: ') 
    n = int(input('Number of Images: '))
    driver = webdriver.Chrome(executable_path=path)
    driver.get('https://www.google.com')
    search = driver.find_element_by_css_selector('input.gLFyf') 
    search.send_keys(q)  
    links = urls()
    driver.quit()
    for i in links:
        save(img_path, q, i) 
    x = input('Do you wanna end? [y or n]: ').lower() #continue or not
    if x == 'yes' or x == 'y':
        break

```

### Thank You for reading!
Just run the whole code and let it automate :)
