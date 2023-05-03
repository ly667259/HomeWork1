# -*- codeing = utf-8 -*-
import tkinter
import tkinter.ttk
import pandas as pd
import PIL.Image
import PIL.ImageTk

#a class for displaying information on a gui
class GUI():
    def __init__(self, datafile='results.csv', image_path='logo.jpg'):
        self.DataFile = datafile
        self.Image_path = image_path
        #article content
        self.paper_dict = {}
        #create a form
        self.root = tkinter.Tk()     
        self.root.title('爱思唯尔文献检索')
        #set the form size
        self.root.geometry("1680x500")
        #initialize the list
        self.creat_init_list()
        self.load_data()
        self.root.mainloop()

    def creat_init_list(self):
        #create a generic list
        self.treeview = tkinter.ttk.Treeview(self.root, columns=('number', 'title', 'authors', 'time', 'keywords', 'url',  'abstract'),
                                             show="headings", height=20)
        
        #configuration column
        self.treeview.column('number', width=1, anchor=tkinter.CENTER)
        self.treeview.column('title', width=120, anchor=tkinter.W)   
        self.treeview.column('authors', width=60, anchor=tkinter.W)
        self.treeview.column('time', width=60, anchor=tkinter.CENTER)
        self.treeview.column('keywords', width=10, anchor=tkinter.CENTER)
        self.treeview.column('url', width=5, anchor=tkinter.CENTER)
        self.treeview.column('abstract', width=220, anchor=tkinter.W)
        
        #set the title
        self.treeview.heading(column='number', text='序号')
        self.treeview.heading(column='title', text='标题')
        self.treeview.heading(column='authors', text='作者')
        self.treeview.heading(column='time', text='刊期')
        self.treeview.heading(column='keywords', text='关键字')
        self.treeview.heading(column='url', text='链接')
        self.treeview.heading(column='abstract', text='摘要')
        
        #define the scroll bar control
        self.scrollbar = tkinter.Scrollbar(self.root, orient='vertical', command=self.treeview.yview)
        
        #display scrollbar 
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        
        #configure scrollbar
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.treeview.bind("<Double-Button-1>", self.paper_item_show)
        self.treeview.pack(fill=tkinter.BOTH)

    def load_data(self):
        #create a drop-down list box
        self.frame = tkinter.Frame(self.root)
        data = pd.read_csv(self.DataFile)
        
        #get the number of rows of data
        len = data.shape[0]
        for i in range(len):
            number = str(i+1)
            title = data.loc[i, 'title']
            authors = data.loc[i, 'authors']
            time = data.loc[i, 'time']
            keywords = data.loc[i, 'keywords']
            url = data.loc[i, 'url']
            abstract = data.loc[i, 'abstract']
            self.treeview.insert(parent='', index=tkinter.END,
                                 values=(number, title, authors, time, keywords, url, abstract))

    def paper_item_show(self, event):
        #display article details
        for index in self.treeview.selection():
            values = self.treeview.item(index, "values")
            #create a child form
            self.subroot = tkinter.Toplevel()
            #form title 
            self.subroot.title('文献信息')
            #form size
            self.subroot.geometry('1600x500')
            
            #pic for visual sensation
            picture = PIL.ImageTk.PhotoImage(image=PIL.Image.open(self.Image_path).resize((380, 320)))
            label_picture = tkinter.Label(self.subroot, image=picture)
            label_picture.grid(row=0, column=0)
            sub_frame = tkinter.Frame(self.subroot)
            
            #set labels
            tkinter.Label(sub_frame, text='【标题】' + values[1], font=('Times New Roman', 12), justify='left').grid(row=0, sticky=tkinter.W)
            tkinter.Label(sub_frame, text='【作者】' + values[2], font=('Times New Roman', 12), justify='left').grid(row=1, sticky=tkinter.W)
            tkinter.Label(sub_frame, text='【刊期】' + values[3], font=('Times New Roman', 12), justify='left').grid(row=2, sticky=tkinter.W)
            tkinter.Label(sub_frame, text='【关键字】' + values[4], font=('Times New Roman', 12), justify='left').grid(row=3, sticky=tkinter.W)
            tkinter.Label(sub_frame, text='【链接】' + values[5], font=('Times New Roman', 12), justify='left').grid(row=4, sticky=tkinter.W)
            tkinter.Label(sub_frame, text='【摘要】', font=('Times New Roman', 12), justify='left').grid(row=6, sticky=tkinter.W)
            #frame
            abstract_frame = tkinter.Frame(sub_frame)
            abstract_listbox = tkinter.Listbox(abstract_frame, height=10, width=200)

            #display abstract
            list_item = list(values[6])
            text = ['']
            num = 0
            Index = 0
            for i in list_item:
                if (Index+1) % 180 == 0:
                    num += 1
                    text.append(i)
                else:
                    text[num] = text[num]+i
                Index += 1
            for item in text:
                abstract_listbox.insert(tkinter.END, item)

            abstract_scrollbar = tkinter.Scrollbar(abstract_frame)
            abstract_scrollbar.config(command=abstract_listbox.yview)
            abstract_scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
            abstract_listbox.pack()

            abstract_frame.grid(row=7, sticky=tkinter.W)
            sub_frame.grid(row=0, column=1, sticky=tkinter.N)
            self.subroot.mainloop()

#try a run
GUI()