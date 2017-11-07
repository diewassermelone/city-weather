from city import city
import urllib.request
import json

yourcity=input()
citycode=city.get(yourcity)
if citycode:
    url=('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
    content=urllib.request.urlopen(url).read()
    
else:
    print('default')
data=json.loads(content)
result=data['weatherinfo']
str_temp=('%s\n%s~%s'%(result['weather'],result['temp1'],result['temp2']))
print(str_temp)
