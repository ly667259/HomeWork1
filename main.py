# -*- codeing = utf-8 -*-
from selenium import webdriver
import pandas as pd
import sys
import time as t
import random
#import self classes
from getch_papers import Getch_Papers
from gui import GUI

if __name__ == '__main__':
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

    #display crawl information by class GUI
    GUI()



    