# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar
month,day,year = input().split(" ")
ind = calendar.weekday(int(year), int(month), int(day))
##method1
print(calendar.day_name[ind].upper())
##method2
if ind == 0:
    print("MONDAY")
elif ind == 1:
    print("TUESDAY")
elif ind == 2:
    print("WEDNESDAY")
elif ind == 3:
    print("THURSDAY")
elif ind == 4:
    print("FRIDAY")
elif ind == 5:
    print("SATURDAY")
elif ind == 6:
    print("SUNDAY")
