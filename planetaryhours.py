
import datetime
import copy
import sys
from astral import Astral

#fucntions below

#converts minutes to hours and minutes
def mins2hoursandmins(time):
    if time/60 ==1:
        hours = time/60
    else:
        hours = time/60
    if time % 60 == 1:
        minutes = time % 60
    else:
        minutes = time % 60
    if minutes < 10:
        minutes = str(minutes)
        minutes = "0" + minutes
    hours = str(hours)
    minutes = str(minutes)
    planetaryhour = hours + ":" + minutes
    return planetaryhour
#calculates the ending time of the hour
def getminutes4subtracting(start_time):
    minutes = start_time[-2:]
    minutes = int(minutes)
    minutes = minutes - 1
    if minutes < 10:
        minutes = str(minutes)
        minutes = "0" + minutes
    else:
        minutes = str(minutes)
    return minutes

#gets the hour and returns it
def gethours(time):
    if time/60 ==1:
        hours = time/60
    else:
        hours = time/60
    return str(hours)
#cityname = "Annapolis"
print "Enter the name of your city."
cityname = raw_input(": ")
a = Astral()
a.solar_depression = 'civil'
try:
    city = a[cityname]
except KeyError:
    print "This city is not recognized. Try the closest capital city or"
    print "a city more well-known."
    sys.exit()
    
print "Enter the current year:"
year = input(": ")
print "Enter the month (number)"
month = input(": ")
print "Enter the day (number)"
day = input(": ")

sun = city.sun(date=datetime.date(year, month, day), local = True)


from datetime import datetime
sunrise_datetime_object = sun['sunrise']
sunset_datetime_object = sun['sunset']

#change datetime.datetime object to string

sunrisestring = sunrise_datetime_object.strftime('%c')
sunsetstring = sunset_datetime_object.strftime('%c')
dayoftheweek = sunrisestring[:3]

#make the string capable of being turned into an int
sunrisestring = sunrisestring[11:-8]
sunsetstring = sunsetstring[11:-8]

#change the string to an int
sunrisehour, sunriseminute = map(int, sunrisestring.split(':'))
sunsethour, sunsetminute = map(int, sunsetstring.split(':'))

sunrisehourtominutes = sunrisehour * 60
sunrisetotalminutes = sunrisehourtominutes + sunriseminute
sunsethourtominutes = sunsethour * 60
sunsettotalminutes = sunsethourtominutes + sunsetminute
difference = sunsettotalminutes - sunrisetotalminutes

#calculatin some hours yayyy
length_of_hour = difference/12
hour1 = sunrisetotalminutes
hour2 = hour1 + length_of_hour
hour3 = hour2 + length_of_hour
hour4 = hour3 + length_of_hour
hour5 = hour4 + length_of_hour
hour6 = hour5 + length_of_hour
hour7 = hour6 + length_of_hour
hour8 = hour7 + length_of_hour
hour9 = hour8 + length_of_hour
hour10 = hour9 + length_of_hour
hour11 = hour10 + length_of_hour
hour12 = hour11 + length_of_hour
array = [hour1,hour2,hour3,hour4,hour5,hour6,hour7,hour8,hour9,hour10,hour11,hour12]

#determine order of the planets based off chaldean sequence
#please ignore the bad code >_<
chaldean = ["Saturn", "Jupiter", "Mars", "Sun", "Venus", "Mercury", "Moon"]
if dayoftheweek == "Mon":
    chaldean = ["Moon", "Saturn", "Jupiter", "Mars", "Sun", "Venus", "Mercury"]
elif dayoftheweek == "Tue":
    chaldean = ["Mars", "Sun", "Venus", "Mercury", "Moon", "Saturn", "Jupiter"]
elif dayoftheweek  == "Wed":
    chaldean = ["Mercury", "Moon", "Saturn", "Jupiter", "Mars", "Sun", "Venus"]
elif dayoftheweek == "Thu":
    chaldean = ["Jupiter", "Mars", "Sun", "Venus", "Mercury", "Moon", "Saturn"]
elif dayoftheweek == "Fri":
    chaldean = ["Venus", "Mercury", "Moon", "Saturn", "Jupiter", "Mars", "Sun"]
elif dayoftheweek == "Sat":
    chaldean = ["Saturn", "Jupiter", "Mars", "Sun", "Venus", "Mercury", "Moon"]
elif dayoftheweek == "Sun":
    chaldean = ["Sun", "Venus", "Mercury", "Moon", "Saturn", "Jupiter", "Mars"]

#repeat the sequence
newchaldean = copy.copy(chaldean)
chaldean.extend(newchaldean)

#truncate the list
chaldean = chaldean[:-2]

#calculate end of hour
#where hhmm is the end time
j = 1
for y in range(12):
    if y < 11:
        hh = gethours(array[j])
        mm = getminutes4subtracting(mins2hoursandmins(array[j]))
        hhmm = hh + ":" + mm
    else:
        lastdayhour = hour12 + length_of_hour - 1
        hhmm = mins2hoursandmins(lastdayhour)
    if y < 10:
        j = j + 1
    #print the hours, start and end
    print "[" + str(y+1) + "]" + " " + mins2hoursandmins(array[y]) + "-" + hhmm + " " + chaldean[y]
