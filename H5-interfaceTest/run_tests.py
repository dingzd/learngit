# -*- coding:utf-8 -*-
__auth__ = 'dingxd'

import time,sys,os
import unittest
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

sys.path.append('./interface')
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*.py')

# 定义发送邮件
def sentmail(file_new):
    mail_from = 'dingxd8095@163.com'  #dingxd8095@163.com
    mail_to = 'dingxd8095@163.com'
    #定义正文
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    #定义标题
    msg['Subject']='H5-InterfaceTest'
    #定义发送时间
    msg['date']=time.strftime('%a, %d %b %Y %H:%M%S %z')
    smtp=smtplib.SMTP()
    #连接SMTP服务器，此处用的163的SMTP服务器
    smtp.connect('smtp.163.com')
    #用户名密码
    smtp.login('dingxd8095@163.com','007zadxd8095@')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print('email has send out !')
#查找测试报告，调用发邮件功能
def sendreport():
    result_dir='D:\\pycharm\\H5-interfaceTest\\testReport'
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn)
    if not os.path.isdir(result_dir+"\\"+fn) else 0)
    print(u'最新测试生成的报告：'+lists[-1])
    file_new=os.path.join(result_dir,lists[-1])
    print(file_new)
    #调用发邮件模块
    sentmail(file_new)

if __name__=='__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = "./testReport/"+now+"_result.html"
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title="category_articles",
                            description="Articles:")

    k =1
    while k<2:
        timing = time.strftime('%H_%M', time.localtime(time.time()))
        if timing =='18_59':
            print(u"脚本开始运行")
            runner.run(discover)
            sendreport()
            break
        else:
            time.sleep(1)
            print(timing)