import requests
import time
time.sleep(5)
str = (requests.get("http://123.123.123.123").text.split('\''))[1]
postjson = {'userId':'','password':'','service':'','queryString':str,'operatorPwd':'','validcode':''}
r=requests.post('http://192.168.50.3:8080/eportal/InterFace.do?method=login',data=postjson)