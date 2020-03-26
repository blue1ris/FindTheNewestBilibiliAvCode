import requests
import threading 
import time
import os,sys
import datetime

startTime = datetime.datetime.now()
lastAVCode = 99459999
# lastAVCode = 99996612 AV99995091 AV99936595 AV99931332 AV99930940 AV99923600 AV99671377 AV99668366 AV99605443 AV99663932 AV99598453 AV99100672   av99105280 AV99273597
flagText = r'视频去哪了呢？_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili'

aThreadTime = 1

lock=threading.Lock()
lastAVCodes = []
def findLast():
    while 1:
        global lastAVCode    #声明全局变量
        global aThreadTime
        lock.acquire()
        tempCode = lastAVCode
        lastAVCode -= 1
        lock.release()
        r = requests.get('https://www.bilibili.com/video/av'+str(tempCode))
        statusCode = r.status_code
        htmlText = r.text
        flag = not flagText in htmlText;
        # print('AV'+str(tempCode)+'    '+str(flag))
        if(flag):
            f  = open('finals.txt','a')
            f.write('AV'+str(tempCode)+'    '+str(flag)+'     '+str(aThreadTime)+'\n')
            lastAVCodes.append(tempCode)
            print('AV'+str(tempCode)+'    '+str(flag)+'     '+str(aThreadTime))
        time.sleep(aThreadTime)
        # print(htmlText)


l=[]    #在全局创建一个空了表

for i in range(75):   #从0到100进行循环
    t=threading.Thread(target=findLast)   #在循环中创建子线程，共创建100个
    t.start()   #循环启动子线程
    l.append(t)   #把循环创建的实例化添加到列表中






while 1:
    flag = 1
    oldAVcode = lastAVCode
    countTime = 5
    time.sleep(countTime)
    f  = open('finals.txt','a')
    f.write('------------------------当前位置:AV{}-----每{}s检测数：{}-----已发现数:{}-------------------\n'.format(lastAVCode,countTime,str(oldAVcode - lastAVCode),len(lastAVCodes)))
    print('------------------------当前位置:AV{}-----每{}s检测数：{}-----已发现数:{}-------------------'.format(lastAVCode,countTime,str(oldAVcode - lastAVCode),len(lastAVCodes)))
    aliveCounter = 0
    if len(lastAVCodes) > 75:flag = 0
    for t in l:
        if(t.isAlive()):aliveCounter += 1
    f.write('alive threads:{},sleeptime:{},usedtime:{}\n'.format(aliveCounter,aThreadTime,datetime.datetime.now()-startTime))
    print('alive threads:{},sleeptime:{},usedtime:{}'.format(aliveCounter,aThreadTime,datetime.datetime.now()-startTime))
    # print('---------------------------------{}---------------------------------'.format())
    if(flag == 0):
        finishTime = datetime.datetime.now()
        maxCode = lastAVCodes[0]
        for i in lastAVCodes:
            if(maxCode < i):
                aliveCounter += 1
                maxCode = i
        f.write('maxcode:av{}\n'.format(maxCode))
        f.write('startTime:{}\nfinishTime:{}\nusedTime:{}\n'.format(startTime.strftime('%Y-%m-%d %H:%M:%S'),finishTime.strftime('%Y-%m-%d %H:%M:%S'),finishTime-startTime))
        f.write('----------------------------------------------------------END----------------------------------------------------------')
        f.close()
        print('maxcode:av{}\nstartTime:{}\nfinishTime:{}\nusedTime:{}'.format(maxCode,startTime.strftime('%Y-%m-%d %H:%M:%S'),finishTime.strftime('%Y-%m-%d %H:%M:%S'),str(finishTime-startTime)))
        print('----------------------------------------------------------END----------------------------------------------------------')
        os._exit(0)

# for f in l:  #从列表里遍历内容给f：
#     f.join()  #循环设置列表的内容结束


#      1 #同步锁
#  2 import time   #导入时间模块
#  3 import threading  #导入threading模块
#  4 num=100    #设置一个全局变量
#  6 def sudnum():   #定一个函数sudnum'
#  7     global num    #声明全局变量
#  8     lock.acquire()
#  9     temp=num     #读取全局变量num
# 10     time.sleep(0)   #增加一个休眠功能
# 11     num=temp-1     #把从全局拿来的变量进行减一的操作
# 12     lock.release()
# 13 l=[]    #在全局创建一个空了表
# 14 for i in range(100):   #从0到100进行循环
# 15     t=threading.Thread(target=sudnum)   #在循环中创建子线程，共创建100个
# 16     t.start()   #循环启动子线程
# 17     l.append(t)   #把循环创建的实例化添加到列表中
# 18 
# 19 for f in l:  #从列表里遍历内容给f：
# 20     f.join()  #循环设置列表的内容结束
# 21 
# 22 print('Result:',num)   #打印通过多次子线程更改过的变量内容
