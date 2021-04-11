from bs4 import BeautifulSoup
import requests

jacket_page = 'https://www.gu-global.com/tw/store/feature/gu/men/jacket/'

r = requests.get(jacket_page)

soup = BeautifulSoup(r.text, "html.parser")

Items = soup.find_all('div', class_='unit')

for item in Items:
    if '男裝西裝領襯衫外套(5分袖)' in item.find('dt', class_='name').text:
        target = item
        break

target_name = target.find('dt', class_='name').text.strip('\r\n\t')
target_price = target.find('dd', class_='price').text.strip('\r\n\t')
print(target_name)
print(target_price)
