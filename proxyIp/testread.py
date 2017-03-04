# coding=utf-8
__author__ = 'gu'

def getIpInFile():  # 从txt文件中读取代理
    file = open("chinaProxyIp.txt", 'r')
    ipProxyList = []
    while True:
        temp = file.readline()
        if temp:
            # print temp
            ipProxyList.append(temp)
        else:
            break
    return ipProxyList

iplist = getIpInFile()
for ip in iplist:
    print ip