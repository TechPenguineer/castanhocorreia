from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import relativedelta
import requests

langs = 'https://github-readme-stats.vercel.app/api/top-langs/?username=castanhocorreia&langs_count=3'
stats = 'https://github-readme-stats.vercel.app/api?username=castanhocorreia&include_all_commits=true&count_private=true'

response = requests.get(stats)
soup = BeautifulSoup(response.content, 'html.parser')

def getStatValue(stat):
    return soup.find('text', attrs={'data-testid': stat}).get_text()

commits = getStatValue('commits')
pullRequests = getStatValue('prs')
issues = getStatValue('issues')
contributions = getStatValue('contribs')

response = requests.get(langs)
soup = BeautifulSoup(response.content, 'html.parser')

top_languages = []

for lang in soup.find_all('text', attrs={'class': 'lang-name'}):
    top_languages.append(lang.get_text())

first_language = "{}: {}".format(top_languages[0], top_languages[1])
second_language = "{}: {}".format(top_languages[2], top_languages[3])
third_language = "{}: {}".format(top_languages[4], top_languages[5])

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
  return '           /^\/^\                                                 Uptime: "{} years, {} {}, {} {}\n'.format(delta.years, delta.months, months, delta.days, days)

def overwriteFile():
  with open('README.md', 'r') as file:
    data = file.readlines()
  data[5] = formatUptimeString()
  data[12] = '                 /      /                    \                    Commits: {}\n'.format(commits)
  data[13] = '                /     /                       /\                  Issues: {}\n'.format(issues)
  data[14] = '              /      /                         \ \                Pull Requests: {}\n'.format(pullRequests)
  data[18] = '         (      (        _-~    _--_    ~-_     _/   |            {}\n'.format(first_language)
  data[19] = '          \      ~-____-~    _-~    ~-_    ~-_-~    /             {}\n'.format(second_language)
  data[20] = '            ~-_           _-~          ~-_       _-~              {}\n'.format(third_language)

  with open('README.md', 'w') as file:
    file.writelines(data)

if __name__ == '__main__':
    overwriteFile()
