from datetime import datetime, timedelta, date
dt_now = datetime.now() # сегодня
print(dt_now)

day = timedelta(days=1) 
dt_tommorow = dt_now - day # день назад
print(dt_tommorow)

month_diff = timedelta(days=30) 
pre_month = dt_now - month_diff # 30 дней назад
print(pre_month)

# превращение строки в объект datetime
date_string = '01/01/25 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f') 
print(date_dt)