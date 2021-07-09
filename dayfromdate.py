from math import floor as fl

'''
Year calculations begin
'''

year = int(input("Enter YEAR:"))

rem_years = year - 1

cent_batches = [400,300,200,100]

cent_oddays = [0,1,3,5]

year_oddays = 0



for cent in cent_batches:

    year_oddays += ((fl(rem_years / cent))*(cent_oddays[cent_batches.index(cent)]))
    rem_years %= cent

leap_years = fl(rem_years / 4)
norm_years = rem_years - leap_years

year_oddays += ((2 * leap_years) + norm_years)
year_oddays %= 7

'''
Month calculations begin
'''

if int(str(year)[-1]) == 0 and int(str(year)[-2]) == 0:
    if year % 400 == 0:
        leap_year = True
    else:
        leap_year = False

else:
    if year % 4 == 0:
        leap_year = True
    else:
        leap_year = False


if leap_year:
    feb = 1
else:
    feb = 0


month = int(input("Enter MONTH:")) 
rem_months = month - 1

month_arr = [3,feb,3,2,3,2,3,3,2,3,2,3]

month_oddays = 0

n = 0

while n != rem_months:
    month_oddays += month_arr[n]
    n += 1

month_oddays %= 7

'''
Date calculations begin
'''

date = int(input("Enter DATE:"))
date_oddays = date % 7

'''
Output calculations begin
'''

total_oddays = (year_oddays + month_oddays + date_oddays) % 7

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print(f"{date} {months[month-1]}, {year} is a {days[total_oddays]}.")
