from easymssql import MSSQL
#连接数据库
data = MSSQL(host="localhost",user="",pwd="",db="BiliUserInfo")
'''
作者:流小光同学
用途
对爬取的内容进行数据管理(包括存入数据和提取数据)
'''
'''
info:一个字典例如
{'uid': '1', 'userName': 'bishi', 'sex': '男', 'lvl': 4, 'VIPType': 'None', 'fansNum': 9480, 'geo': '未填写'}
sex:可能值为 男,女,保密
lvl:为1~6的整数
VIPType为可能是"None","normal-v","annual-v"的字符串
'''
def setData(info,table = 'UserInfo'):
	data.ExecNonQuery("insert into " + table + " values ("
	 + "\'" + info['uid'] + "\'" + ","
	 + "\'" + info['userName'] + "\'" + ","
	 + "\'" + info['sex'] + "\'" + ","
	 +    str(info['lvl']) + ","
	 + "\'" + info['VIPType'] + "\'" + ","
	 +    str(info['fansNum']) + ","
	 + "\'" + info['geo'] + "\'" + ")")


'''
table:提取的表名
返回两个列表,分别为等级1以上的UID和对应的等级
'''
def getlvl(table):
    info = data.ExecQuery("select UID,lvl from " + table + " where lvl>=1")
    list1 = []
    list2 = []
    for a in info:
        list1.append(int(a[0]))
        list2.append(a[1])
    return list1,list2
'''
table:提取的表名
返回男,女数量列表
'''

def getsex(table): #男,女
    info = data.ExecQuery("select count(*) from " + table + " group by Sex " )
    list1 = []
    for a in info:
        list1.append(a[0])
    return [list1[1],list1[2]]

'''
table:提取的表名
返回(年度会员,无,会员)数量列表
'''
def getVIPtype(table): #年度会员,无,会员
    info = data.ExecQuery("select count(*) from " + table + " group by VIPType order by VIPType")
    list1 = []
    for a in info:
        list1.append(a[0])
    return list1
'''
table:提取的表名
返回两个列表:会员的UID和对应的等级
'''
def getVIPAndLvl(table):
    info = data.ExecQuery("select UID,lvl from " + table + " where VIPType='normal-v' or VIPType='annual-v'")
    list1 = []
    list2 = []
    for a in info:
        list1.append(int(a[0]))
        list2.append(a[1])
    return list1,list2
