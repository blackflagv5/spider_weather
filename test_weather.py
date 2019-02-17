import requests
cityname='深圳'
appkey='00c6c0da986f4ff8ab85a379c418699e'
url='http://api.avatardata.cn/Weather/Query?key='+appkey+'&cityname='+cityname
r=requests.get(url)

sds = r.json()
for temp in sds['result']['weather']:
	print("日期:", temp['date'], "星期几:", temp['week'], "农历:", temp['nongli'])
	print("早上天气")
	print("最低气温",temp['info']['dawn'][0])
	print("最高气温",temp['info']['dawn'][2])
	print("天气",temp['info']['dawn'][1])
	print("风向",temp['info']['dawn'][3])
	print("风力",temp['info']['dawn'][4])
	print("时间",temp['info']['dawn'][5])