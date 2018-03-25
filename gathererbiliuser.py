# coding=utf-8
from selenium import webdriver

"""
作者: RAmen_L
用途:
    爬取b站用户uid空间的内容
范例:
    def main():
        uid = 1
        test = gathererbiliuser(uid)
        if not test.driverError:
            print(test.getinfo())
    main()
getinfo()返回的是一个例如以下的字典
{'uid': '1', 'userName': 'bishi', 'sex': '男', 'lvl': 4, 'VIPType': 'None', 'fansNum': 9480, 'geo': '未填写'}
if test.driverError == True 那么证明gathererbiliuser内部发生过异常
"""

class gathererbiliuser:
    def __init__(self,uid):
        self.driverError = False
        info_original = {}
        try:
            driver = webdriver.Firefox() #打开火狐浏览器
            driver.get("https://space.bilibili.com/" + str(uid)) #打开biliuserspace界面
            #信息的原型
            #获得uid
            info_original ['uid'] = str(uid)
            #抓取用户昵称
            info_original ['userName'] = driver.find_element_by_id("h-name").text
            #抓取用户性别
            usersex_e = driver.find_element_by_id("h-gender")
            info_original ['sex'] = usersex_e.get_attribute("class")
            #抓取用户等级
            userlvl_e = driver.find_element_by_class_name("h-level.m-level")
            info_original ['lvl'] = userlvl_e.get_attribute("lvl")
            #抓取VIP类型
            user_e = driver.find_element_by_class_name("h-basic")
            userVIPType_e = user_e.find_element_by_xpath(".//div[1]/a[2]")
            info_original ['VIPType'] = userVIPType_e.get_attribute("class")
            #抓取粉丝数
            userFansNum_e = driver.find_element_by_class_name("n-data-v.space-fans")
            info_original ['fansNum'] = userFansNum_e.text
            #抓取用户所在地区

            usergeo = driver.find_element_by_class_name("item.geo")
            info_original ['geo'] = usergeo.find_element_by_xpath(".//span[last()]").text
            #对信息进行处理
            self.__info = self.__reviseinfo(info_original)
        except Exception as e:
            print(uid , " and ", e , "异常")
            self.driverError = True
            driver.close()
        finally:
            driver.quit()
    def __reviseinfo(self,infoO):
        info = {}
        if self.driverError == True:
            return None
        info['uid'] =  infoO['uid']

        info['userName'] = infoO['userName']
        if infoO['sex'][12:] == '':
            info['sex'] = '保密'
        elif infoO['sex'][12:] == 'male':
            info['sex'] = '男'
        elif infoO['sex'][12:] == 'female':
            info['sex'] = '女'
        else:
            print(infoO['sex'][12:])#test
            info['sex'] = '异常'

        info['lvl'] = int(infoO['lvl'])

        if infoO['VIPType'][10:] == "":
            info['VIPType'] = "None"
        else:
            info['VIPType'] = infoO['VIPType'][10:]

        if infoO['fansNum'].find('万') == -1:
            info['fansNum'] = int(infoO['fansNum'])
        else:
            info['fansNum'] = int(float(infoO['fansNum'][:-1]) * 10000)

        info['geo'] = infoO['geo']
        return info
    def getinfo(self):
            return self.__info
