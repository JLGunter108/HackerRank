import calendar

days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

m, d, y = map(int, input().split())

day =  calendar.weekday(y,m,d)

print(days[day])