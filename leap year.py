start = int(input("Enter start year: "))
end = int(input("Enter end year: "))

while start >= end:
    print("Check your year input again.")
    start = int(input("Enter start year: "))
    end = int(input("Enter end year: "))

print ("Here is a list of leap years between {0} and {1}:".format(start,end))

leap_years = []
Non_leap_years=[]
while start <= end:
    if start % 4 == 0 and start % 100 != 0:
        leap_years.append(str(start))
    elif start % 100 == 0 and start % 400 == 0:
        leap_years.append(str(start))
    else:
        Non_leap_years.append(str(start))
    start += 1
print('\nThe following are Leap years\n')
for line in range(0, len(leap_years), 10):
    print ("{0}.".format(", ".join(leap_years[line:line+10])))
print('\n- - - - - - - - - -\n\nThe following are Non-Leap years\n')
for line in range(0, len(Non_leap_years), 10):
    print ("{0}.".format(", ".join(Non_leap_years[line:line+10])))
print(" ")
import datetime
print("To know your day when you are born")
date=str(input('Enter the date(for example:09 02 2019):'))
day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
print(day_name[day])