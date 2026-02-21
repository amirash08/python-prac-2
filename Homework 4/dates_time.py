import datetime
x = datetime.datetime.now()
print (x)
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%B"))
print(datetime.datetime.now().day)
print(x.hour)
print(x+datetime.timedelta(days=15, hours=10, seconds=43))

from datetime import datetime, timedelta
print(datetime.now())
print(datetime.now() + timedelta(days=15, hours=10, seconds=43))

from datetime import datetime, timedelta
my_str = '21/02/2026 16:30:00' 
my_date = datetime.strptime(my_str, '%d/%m/%Y %H:%M:%S')
print(my_date)


from zoneinfo import ZoneInfo

try:
    ZoneInfo("Asia/Almaty")
    print("OK")
except Exception as e:
    print("ERROR:", e)