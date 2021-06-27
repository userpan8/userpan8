# -*- coding: utf-8 -*-

'''

Author：by_天荒
Date：2021.6.27 
qpython软件下载链接 
https://www.coolapk.com/apk/com.hipipal.qpyplus

'''

import requests
import json
import re
url = 'https://www.uurss.xyz/auth/login'
sign = 'https://www.uurss.xyz/user/checkin'
user_url = 'https://www.uurss.xyz/user'

#多个账号用英文逗号隔开，每个账号密码用:分开
user_list = """


1439332604@qq.com:qweasd123.


""".split(",")


headers = {
    "content-length": "0",
    "accept-language": "zh-CN,en-US;q=0.8",
    "accept": "application/json, text/javascript, */*; q=0.01",
  #  "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; NX611J Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36",
    "Host": "www.uurss.xyz",
    "x-requested-with": "XMLHttpRequest",
    "referer": "https://www.uurss.xyz/user",
}
#unicode转换
def txt(content):
        tmp = ""
        for cr in content:
            if (cr=="u" or cr=="'"):
                tmp = tmp + cr
                continue
            tmp = tmp + repr(cr).replace("u'", "").replace("'","")
        return tmp.decode("unicode_escape").encode("utf-8")


def main(user,password):
    session = requests.session()
    d =  {
    "email": user,
    "passwd": password,
    "code": ""
     }
    response  = session.post(url,data=d,headers = headers).json()
    if response["ret"]==1:
       print(user+" "+txt(response["msg"]))
       data  = session.get(user_url,headers = headers).text
       use = re.findall("'Unused_Traffic': '(.*?)'",txt(data))[0]
       print("{} 可用流量：{}".format(user,use))
       v2_res= re.findall("class=\"btn btn-icon icon-left btn-primary btn-v2ray copy-text btn-lg btn-round\" data-clipboard-text=\"(.*?)\"",txt(data))
       print(user+" v2订阅链接："+v2_res[0])
       sign_res=session.post(sign,headers = headers)
       print(user+"  "+txt(sign_res.json()["msg"]))
    else:
         print(txt(response["msg"]))
        
for i in user_list:
    user_res = i.split(":")
    main(user_res[0].strip(),user_res[1].strip())
