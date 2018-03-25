#调用GUI-tk模块[第三方]
from tkinter import *

#调用网页爬取模块[应由由王彩霞同学负责]
from gathererbiliuser import gathererbiliuser
#调用数据库管理模块[由钟凯鸣同学负责]
from sqldata import setData

import random
import time, threading
import os
'''
作者: RAmen_L
用途:
    抽样爬取b站用户空间的内容并保存到数据库(每50000UID随机抽样)
可能出现的问题:
    加注释后可能出现问题,请联系作者
    对UID_i.txt的操作没有进行异常处理,不过如果没人闲得慌用到一半把UID_i.txt删了是不会出现问题的
'''

class GUIForGetData:
    def __init__(self):
        #建立GUI界面
        self.root = Tk()
        self.root.geometry = [200,200]

        #UID_i.txt 保存进度的文本文件,方便断点续连,若为建此文键则建立
        if not os.path.exists('UID_i.txt'):
            f1 = open('UID_i.txt','w')
            f1.write('0')
            f1.close()
        #读取文件并开始抽样
        i = self.__readtxt()
        j = self.__iToj(i)
        #显示正在抽样的UID的标签
        self.var = StringVar()
        self.var.set(str(j))
        self.labelj = Label(self.root,textvariable = self.var)
        self.labelj.pack()
        #开始暂停按钮,点击运行函数self.buttonsasListener
        #判断开始暂停的标志,开始为True,暂停为False
        self.flag = True
        self.bttext = StringVar()
        self.bttext.set('开始爬')
        self.buttonStartAndStop = Button(self.root,textvariable = self.bttext)
        self.buttonStartAndStop.bind("<Button-1>",self.buttonsasListener)
        self.buttonStartAndStop.pack()

        #进入消息循环
        self.root.mainloop()
    def buttonsasListener(self,event):
        if self.bttext.get() == '开始爬':
            self.flag = True
            self.bttext.set('暂停爬')
            #运行线程:self.__crawler,开始爬取
            t = threading.Thread(target=self.__crawler, name='__crawlerThread')
            t.start()
        elif self.bttext.get() == '暂停爬':
            self.flag = False
            self.bttext.set('开始爬')
            '''
            爬取函数
            '''
    def __crawler(self):
        #异常指数c
        c = 0
        #最大异常指数设定
        MAXEXCEPTIONINDEX = 10
        #读取UID_i文件,确认爬取目标
        i = self.__readtxt()
        j = self.__iToj(i)
        #当暂停或已经爬取了5000个用户后结束线程(爬取b站(UID:5000*50000)内的用户)
        while i <= 5000 and self.flag == True:
            self.var.set(str(j))
            '''
            try:
                执行爬取函数(调用gathererbiuser.py模块内容)
                获得爬取内容
                将其存入数据库(调用sqldata.py模块内容)
            '''
            try:
                test = gathererbiliuser(j)
                info = test.getinfo()
                setData(info)
                #time.sleep(1)
            #出现异常处理,通常为(网页异常:比如被封号等无法进入主页),(数据库保存异常)
            except Exception as e:
                #输出异常,也可以改成将异常内存保存进硬盘,不过懒得弄就直接输出了
                print(e)
                #每次出现异常指数+1
                c = c + 1
                #MAXEXCEPTIONINDEX次异常后放弃抽取此50000个样本,进行下50000个样本抽取
                if c == MAXEXCEPTIONINDEX:
                    i = i + 1
                    j = self.__iToj(i)
                    c = 0
                else:
                    #每次出现异常后在随机数j后100位ID爬取
                    j = j + 100
            else:
                #若爬取成功则进行下次爬取
                i = i + 1
                j = self.__iToj(i)
                f = open('UID_i.txt', 'w')
                f.write(str(i))
                f.close()
    #读取UID_i内容
    def __readtxt(self):
        f = open('UID_i.txt')
        str1 = f.read()
        f.close()
        return int(str1)
    #随机抽样[i*50000,(i+1)*50000)
    def __iToj(self,i):
        return random.randint(i*50000,(i+1)*50000-1)
#进行抽取
i = GUIForGetData()
#单个爬取实例
#test = gathererbiliuser(5856568)
#info = test.getinfo()
#setData(info)
