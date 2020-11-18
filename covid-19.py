from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier

header = {'User-Agent': 'Mozilla'}
req = Request('https://www.mohfw.gov.in/', headers = header)
html = urlopen(req)
obj = bs(html)
active_cases = list(obj.find("li", {"class": "bg-blue"}).strong.next_siblings)[1].text.split()[0]
new_discharged = list(obj.find("li", {"class": "bg-green"}).strong.next_siblings)[1].text.split()[0]
new_deaths = list(obj.find("li", {"class": "bg-red"}).strong.next_siblings)[1].text.split()[0]

# notifier

notifier = ToastNotifier()
message = "New Cases: "+active_cases+"\nNew Discharged: "+new_discharged+"\nNew Deaths: "+new_deaths
notifier.show_toast(title="COVID-19 Update", msg=message, duration=5, icon_path=r"virus.ico")