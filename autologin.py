#coding:utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from buaa_login import BuaaLogin

class checkAccess(object):
    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    #判断当前是否可以连网
    def canConnect(self):
        try:
            baidu_request=requests.get("http://www.baidu.com")
            if(baidu_request.status_code==200):
                baidu_request.encoding = 'utf-8'
                baidu_request_bsObj = BeautifulSoup(baidu_request.text, 'html.parser')
                baidu_input = baidu_request_bsObj.find(value="百度一下")
                if baidu_input==None:
                    return False
                return True
            else:
                return False
        except:
            print ('error')

    #主函数
    def main(self,object):
        print (self.getCurrentTime(), "Hi, Script is running")
        while True:
            while True:
                can_connect = self.canConnect()
                if not can_connect:
                    print (self.getCurrentTime(),"No accession...")
                    try:
                        object.log_in()
                    except:
                        print(self.getCurrentTime(), "Login bug")
                    finally:
                        time.sleep(2)
                        if self.canConnect():
                            print(self.getCurrentTime(), "Login again successfully")
                        else:
                            print(self.getCurrentTime(), "Login failed, try again")
                else:
                    print (self.getCurrentTime(), "Everything normal...")
                    time.sleep(5)
                time.sleep(1)
            time.sleep(self.every)


if __name__ == '__main__':
    username = str("by1604155")
    passwd = str("lwj19900724")
    bl = BuaaLogin(username=username,
                  password=passwd)
    ca = checkAccess ()
    ca.main(bl)
