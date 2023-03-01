from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
import requests
import json
import sys


urls = [
"elbotola",
"kora",
]

def main():
    
    link = str(sys.argv[1])
    op = Options()
    op.set_preference('javascript.enabled', False)
    driver = webdriver.Firefox(options=op)    
    # driver.get("https://www.youtube.com/c/{}/videos".format(urls[0])) #get link of kora articles 
    # driver.get("https://www.elbotola.com/article/2022-11-27-17-18-160.html") 
    driver.get(link) 
    content = driver.page_source.encode("utf-8").strip() 
    soup = BeautifulSoup(content,'lxml')
    titre = soup.findAll('h2',class_="article-title")  
    image = soup.findAll('img',class_="article-image")  
    bodyy = soup.findAll('main',class_="article-content")  
    pushtoServe(titre[0].text,bodyy[0].text,"https:"+image[0]['src'])
    driver.quit()
    


def pushtoServe(title,content,image):
    # image = "https://colourlex.com/wp-content/uploads/2021/02/vine-black-painted-swatch-300x300.jpg"
    print("\n {} \t {} \t {}".format(title,content,image))
    token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyYTQyZWIxZWE3MGY4OWQ3Y2RkMmRlOSIsImlhdCI6MTY2ODQzMTYzOSwiZXhwIjoxNjcxMDIzNjM5fQ.cWrVAQuxA-KqSKVRTIA0EDJ5-1PHgoIOtusmwHzmuco'
    api_url = ""
    todo = {"title": title,"image":image, "content":content,"status":"topkora"}
    headers =  {"Content-Type":"application/json",'Authorization':token}
    response = requests.post(api_url, data=json.dumps(todo), headers=headers)
    print(response.json())

main() 