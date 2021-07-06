import math

year = int(input("Enter year: "))

month = int(input("Enter month number: "))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

date = int(input("Enter date: "))
date = date % 7

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


zero_oddays = (year-1) % 400


batches_300 = math.floor((zero_oddays) / 300)
oddays_300 = batches_300 * 1


batches_200 = math.floor((zero_oddays % 300) / 200)
oddays_200 = 3 * batches_200


batches_100 = math.floor(((zero_oddays % 300) % 200) / 100)
oddays_100 = 5 * batches_100


rem_years = ((zero_oddays % 300) % 200) % 100

leap_years = rem_years % 4
leap_oddays = 2 * leap_years

normal_years = rem_years - (rem_years % 4)
normal_oddays = 1 * normal_years

year_oddays = (oddays_300 + oddays_200 + oddays_100 + leap_oddays + normal_oddays) % 7

if year % 4 == 0:
    feb = 1
else:
    feb = 0

month_days = [3,feb,3,2,3,2,3,3,2,3,2,3]

if month == 1:
    day = days[(year_oddays + date) % 7]

else:
    month_oddays = 0

    for i in range(0,(month-2)):
        month_oddays += month_days[i]

    month_oddays = month_oddays % 7
        
    total_oddays = (year_oddays + month_oddays + date) % 7

    day = days[total_oddays]

print(f"{date} {months[month-1]}, {year} was a {day}.")



