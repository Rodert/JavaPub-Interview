# http://5.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406607245858265667_1648288188313&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1648288188314

import requests
import json
import re

jsUrl = 'http://5.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406607245858265667_1648288188313&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1648288188314'

response = requests.get(jsUrl)

print(response.text)
print("###")
pat = "diff\":\[(.*?)\]"
pat1 = "(.*?)"
data = re.compile(pat, re.S).findall(response.text)
print(data)
print("######")
obj = data[0]

print(obj)