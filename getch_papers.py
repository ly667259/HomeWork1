# -*- codeing = utf-8 -*-
from selenium import webdriver
import pandas as pd
import sys

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
        list_url = []
        return list_url
    
    #a function for getting urls for all pages
    def get_urls(self,url,driver,numsofpage = 1):
        #multiple pages , get the urls for each page
        driver.get(url)
        list_urls_pages = []
        
        #crawl all pages of url
        list_urls=[]
        return list_urls
    
    #a function for getting information of a paper by its url
    def get_messages(self,url,driver):
        driver.get(url)
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