import math
from datetime import datetime


def weekDay(year, month, day):
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week   = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',  'Friday', 'Saturday']
    afterFeb = 1
    if month > 2:
        afterFeb = 0
    aux = year - 1700 - afterFeb
    dayOfWeek  = 5
    dayOfWeek += (aux + afterFeb) * 365
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400
    dayOfWeek += offset[month - 1] + (day - 1)
    dayOfWeek %= 7
    return week[math.floor(dayOfWeek)]

Today = weekDay(int(str(datetime.now())[:4]), int(str(datetime.now())[5:7].lstrip('0')), int(str(datetime.now())[8:10]))


def restaurants(spots):
  destination = ''
  for x in range(0, len(spots)):
    entry = ''
    if 'dayoff' in spots[x] and spots[x]['dayoff'] == Today:
      entry = ''
    elif 'vacationFrom' in spots[x] and spots[x]['vacationFrom'] < str(datetime.now()) < spots[x]['vacationTo']:
      entry = ''
    else:
      if 'menu' in spots[x] and 'credit' in spots[x]:  # if lunchspot has payment option other than cash display card emoji
        entry = "<" + spots[x]['location'] + "|:" + spots[x]['number'] + ":> <" + spots[x]['menu'] + "|" + spots[x]['restaurant'] + "> :credit_card:\n"
      elif 'menu' in spots[x]:
        entry = "<" + spots[x]['location'] + "|:" + spots[x]['number'] + ":> <" + spots[x]['menu'] + "|" + spots[x]['restaurant'] + ">\n"
      else:
        entry = "<" + spots[x]['location'] + "|:" + spots[x]['number'] + ":> " + spots[x]['restaurant'] + "\n"
    destination += entry
  return destination
