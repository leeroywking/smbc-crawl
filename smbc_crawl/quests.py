import requests
from bs4 import BeautifulSoup
import time

first_url = "https://www.smbc-comics.com/comic/2002-09-05"

def grab_page(starting_url):
    first_res = requests.get(starting_url)
    soup = BeautifulSoup(first_res.content, "html.parser")
    image_results = soup.find(id="cc-comic")
    next_results = soup.find_all('a', class_='cc-next')[0]
    image_url = image_results.get("src")
    alt_text = image_results.get("title")
    next_link = next_results.get("href")
    return {"image_url":image_url, "alt_text":alt_text, "next_link":next_link}

def grab_some(num):
    output = []
    next_page = first_url
    err_count = 0
    for i in range(num):
        try:
            store = grab_page(next_page)
            next_page = store["next_link"]
            output.append(store)
            # time.sleep(1)
        except:
            print('error on iteration', i)
            err_count += 1
            if err_count > 10:
                break
    return output

def grab_n_comics_from_start(n_comics):
    results = grab_some(n_comics)
    print(results)

    f = open("./output.py", "a")
    f.write("listy = ")
    f.write(str(results))
    f.close()

