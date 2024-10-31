import datetime

# today = datetime.datetime.now()
# print(today)

birthday = datetime.date(2001 , 16, 1 )

print(f'My birthday is {birthday.strftime('%m', '%d', '%Y' )}.')

import datetime

today = datetime.date.today()

ninety_d = today + datetime.timedelta(days=90)
date_format = ninety_d.strftime("90 days from today is %B %d, %Y")
print(date_format)



dinner_time = datetime.time(12, 45)
formatted_dinner = dinner_time.strftime("We can meet up at %I: %M %p ")
print(formatted_dinner)

