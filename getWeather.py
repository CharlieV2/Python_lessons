from urllib.request import urlopen
from bs4 import BeautifulSoup

url = Request('https://www.wunderground.com/history/airport/UUEE/2018/2/1/DailyHistory.html', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(url).read()
soup = BeautifulSoup(webpage)
values = soup.findAll(attrs={"class":"wx-value"})
print(values[1])
