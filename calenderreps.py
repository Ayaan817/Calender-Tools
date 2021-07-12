year = int(input("Enter YEAR: "))

rep_mods = [1,2,3,0]
mod = year % 4

year_reps = [6,11,11,28]

for mods in rep_mods:
    if mod == mods:
        year_rep = year_reps[rep_mods.index(mods)]
        break

print(f"The calender for the year {year} will repeat every {year_rep} years.")

num_reps = int(input("How many repeated calender years do you want to view?\n"))

rep_cal_years = []
i = 0

while i != num_reps:

    year += year_rep
    rep_cal_years.append(year)

    i += 1

print(rep_cal_years)

input()
