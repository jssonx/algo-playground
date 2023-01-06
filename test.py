import datetime

now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")
today = (now.split(" "))[0]
print(type(today))
