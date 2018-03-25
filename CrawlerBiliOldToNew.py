from easymssql import *
from gathererbiliuser import gathererbiliuser
'''
在2018年对1级用户重新爬取
'''
def getoldUID():
    data = MSSQL(host="localhost",user="",pwd="",db="BiliUserInfo")
	info = data.ExecQuery('select UID from UserInfo where lvl >= 1')
	list1 = []
	for i in info:
		list1.append(int(i[0]))
	return list1

for i in getoldUID():
    try:
        test = gathererbiliuser(i)
        info = test.getinfo()
        setData(info,table = 'Userinfo_2018_')
    except Exception as e:
        print(e)
