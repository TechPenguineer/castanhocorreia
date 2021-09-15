from datetime import datetime
from dateutil import relativedelta

birthDate = datetime(1998, 7, 2)
currentDate = datetime(datetime.today().year, datetime.today().month, datetime.today().day)
delta = relativedelta.relativedelta(currentDate, birthDate)

def formatNumeralConcord():
  concord = []
  concord.append('month') if delta.months <= 1 else concord.append('months')
  concord.append('day') if delta.days <= 1 else concord.append('days')
  return concord

def formatUptimeString():
  days = formatNumeralConcord()[1]
  months = formatNumeralConcord()[0]
  return 'Uptime: "{} years, {} {}, {} {}"\n'.format(delta.years, delta.months, months, delta.days, days)

def overwriteFile():
  with open('README.md', 'r') as file:
    data = file.readlines()
  data[6] = formatUptimeString()
  with open('README.md', 'w') as file:
    file.writelines(data)

if __name__ == '__main__':
    overwriteFile()
