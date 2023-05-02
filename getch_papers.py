# -*- codeing = utf-8 -*-
from selenium import webdriver
import pandas as pd
import sys
import time as t
import random

#a class for getting papers from ScienceDirect
class Getch_Papers():

    def __init__(self):
        self.web = "https://www.sciencedirect.com"
        self.data = pd.DataFrame()
    
    #a function for getting url of web based on the retrieved information
    def search(self):
        url = self.web + '/search'
        print('请输入检索信息！')
        #key information
        terms = input('Find articles with these terms:')
        if terms != '':
            url = url + '?qs=' + terms
        #authors
        authors = input('Author(s):')
        if terms != '':
            url = url + '&authors=' + authors
        #years
        years = input('Year(s):')
        if terms != '':
            url = url + '&date=' + years
        #journal title
        journal = input('In this journal or book title:')
        if terms != '':
            url = url + '&pub=' + journal
          
        if url != self.web + '/search':
            return url
        else:
            print('未输入任何检索信息！')
            sys.exit('程序中止！')

    #a function for getting urls for all papers in a page
    def get_url(self,url,driver):
        
        driver.get(url)
        t.sleep(random.randint(1,2))

        url = driver.find_elements_by_xpath('//ol[@class="search-result-wrapper"]/li')
        temp = url[0].find_elements_by_xpath('//h2/span/a')
        list_url = []
        for i in range(len(temp)):
            list_url.append(temp[i].get_attribute('href'))
        return list_url
    
    #a function for getting urls for all pages
    def get_urls(self,url,driver,numsofpage = 1):
        #multiple pages , get the urls for each page
        driver.get(url)
        t.sleep(random.randint(1,2))
        pagesnum=driver.find_element_by_xpath('//ol[@id="srp-pagination"]')
        pages_num_s = pagesnum.text
        pages_num = ''.join([x for x in pages_num_s if x.isdigit()])
        nums_of_page = int(pages_num[1:])#nums of pages
        list_urls_pages = []
        if nums_of_page < numsofpage:
            for i in range(nums_of_page):
                list_urls_pages.append(url + '&offset=' + str(i*25))
        else:
            for i in range(numsofpage):
                list_urls_pages.append(url + '&offset=' + str(i*25))
        #crawl all pages of url
        list_urls=[]
        for i in range(len(list_urls_pages)):
            list_urls.extend(self.get_url(url=list_urls_pages[i],driver=driver))
        return list_urls
    
    #a function for getting information of a paper by its url
    def get_messages(self,url,driver):
        driver.get(url)
        t.sleep(random.randint(1,2))
        #crawl title and return a str
        title_temp = driver.find_element_by_xpath('//span[@class="title-text"]')
        title = title_temp.text
        #crawl authors and return a [str]
        authors_temp = driver.find_elements_by_xpath('//span[@class="react-xocs-alternative-link"]') 
        authors = []
        for i in range(len(authors_temp)):
            authors.append(authors_temp[i].text)
        #crawl time and return a str
        time_temp = driver.find_element_by_xpath('//div[@class="text-xs"]')
        time = time_temp.text
        #crawl keywords and return a [str]
        keywords_temp = driver.find_elements_by_xpath('//div[@class="keyword"]')
        keywords = []
        for i in range(len(keywords_temp)):
            keywords.append(keywords_temp[i].text)
        #crawl abstract and return a str
        abstract_temp = driver.find_element_by_xpath('//div[@class="abstract author"]')
        abstract = (abstract_temp.text).replace("Abstract\n","")

        return title,authors,time,keywords,abstract

    #a function for saving information to file.csv
    def save_to_csv(self,title,authors,time,keywords,abstract,url):
        data = {"title" : title,
                "authors" : authors,
                "time" : time,
                "keywords" : keywords,
                "abstract" : abstract,
                "url" : url}
        self.data = self.data.append(pd.DataFrame(data))
        self.data.to_csv("results.csv",index=False)

#try a run
driver = webdriver.Edge(executable_path="D:\\edgedriver_win64\msedgedriver.exe")
#instantiate a crawl class
getch_page = Getch_Papers()
url_search = getch_page.search()
#get the urls for all the papers
list_urls = getch_page.get_urls(url = url_search,driver = driver,numsofpage = 5)
print(list_urls)
#get the information needed for all papers
title,authors,time,keywords,abstract = [],[],[],[],[]
for i in range(len(list_urls)):
    title_temp,authors_temp,time_temp,keywords_temp,abstract_temp = getch_page.get_messages(url = list_urls[i],driver=driver)
    title.append(title_temp)
    authors.append(authors_temp)
    time.append(time_temp)
    keywords.append(keywords_temp)
    abstract.append(abstract_temp)
#save the information to file.csv
getch_page.save_to_csv(title=title,authors=authors,time=time,keywords=keywords,abstract=abstract,url=list_urls)
driver.quit()