from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import json
import time
import sys

urls = [
"beINSPORTS"
]

def main():
    num = int(sys.argv[1])
    driver = webdriver.Firefox()    
    driver.get("https://www.youtube.com/c/{}/videos".format(urls[0])) #  get the channel videos
    content = driver.page_source.encode("utf-8").strip() # strip the content
    soup = BeautifulSoup(content,'lxml')
    alltitles = soup.findAll('a',id='video-title-link')  # get all the a tags
    mylen = len(alltitles)
    j= 21 
    for i in range(mylen):
        j=j-1
        link = alltitles[j].get('href').replace("/watch?v=", "") # get the href and replace the watch..
        if ('ملخص' in alltitles[j].text) and (num >= 0):
            num = num - 1
            mylink = "https://youtu.be/"+link
            print("\n {} \t {}".format(mylink,alltitles[j].text))
            pushtoServe(alltitles[j].text,mylink)
    driver.quit()
    


def pushtoServe(title,content):
    image = "https://colourlex.com/wp-content/uploads/2021/02/vine-black-painted-swatch-300x300.jpg"
    token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyYTQyZWIxZWE3MGY4OWQ3Y2RkMmRlOSIsImlhdCI6MTY2ODQzMTYzOSwiZXhwIjoxNjcxMDIzNjM5fQ.cWrVAQuxA-KqSKVRTIA0EDJ5-1PHgoIOtusmwHzmuco'
    api_url = ""
    todo = {"title": title,"image":image, "content":content}
    headers =  {"Content-Type":"application/json",'Authorization':token}
    response = requests.post(api_url, data=json.dumps(todo), headers=headers)
    print(response.json())
    time.sleep(5.5)

main() 