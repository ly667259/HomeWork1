# HomeWork1
Python与深度学习基础第一次大作业——爬取爱思唯尔文献信息

    采用Python爬虫技术，从图书馆爱思唯尔文献库（https://www.sciencedirect.com）中获取指定检索信息的文献的标题、作者、关键字、摘要、链接等信息，并通过GUI列表来展示。代码爬取了力学领域两个有名期刊JMPS（Journal of the Mechanics and Physics of Solids）、IJIE（International Journal of Impact Engineering）上的文章。
    getch_papers.py、gui.py、main.py，分别对应爬取、展示和运行的任务。
    为了方便演示，将main.py改写成了display.ipynb，用jupyter notebook展示运行。而且由于notebook的方便，代码中稍加了一行用来print所有文献的url，且在notebook中点击这些url可以直接转到文献页面处。
    爬取了JMPS上deep learning有关的46篇文献并展示，爬取了IJIE上2022年deep learning有关的4篇文献并展示。
    总共进行了五次提交，内容分别对应：编写爬取类Getch_Papers的框架，完善爬取类并试运行，编写展示GUI类并试运行，编写main主程序并一起运行爬取和展示，使用notebook方便展示并录制视频。
