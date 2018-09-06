import psutil
import requests
import re
import datetime

def getIP():
    # 获取公网IP
    year = str(datetime.datetime.now().year)
    url = "http://%s.ip138.com/ic.asp" %year
    data = requests.get(url)
    ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", data.text).group(0)
    return ip

def getMemory():
    # 获取内存百分比
    m = psutil.virtual_memory().percent
    return str(m)

def getCPU(x):
    # 获取CPU百分比
    # time.sleep(0.1)
    c = psutil.cpu_percent(interval=x)
    return str(c)

def sendServer(desp):
    # 发送到微信
    today = str(datetime.date.today())
    key = "SCU23702T0f1f4368d47f6323a502baa77b3dfb5d5ab65b0f15913" #key
    url = "https://sc.ftqq.com/%s.send" %key
    d = {'text': "日期："+ today +"，内存CPU当前百分比", 
         'desp': desp 
         }
    r = requests.post(url, data=d)
    return r.text

var = 1
while var == 1:
    # 无限循环
    ip = getIP()
    x = getCPU(1)
    y = getMemory()
    send = "###公网IP：%s，CPU：%s，内存：%s" %(ip,x,y)
    sendServer(send)
