import calendar,datetime

def next_leap(x) : 
	return x if calendar.isleap(x) else next_leap(x+1)

print (next_leap(datetime.datetime.now().year+1))

print (calendar.leapdays(2000,2050) + 1)

print (calendar.weekday(2016,7,29))
