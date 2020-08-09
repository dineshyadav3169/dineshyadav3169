import requests
from bs4 import BeautifulSoup

url = "https://github-readme-stats.codestackr.vercel.app/api?username=dineshyadav3169&show_icons=true&hide_border=true&hide=prs,issues&hide_rank=true"

web = requests.get(url)
soup = BeautifulSoup(web.content, 'html.parser')

results = soup.find_all(class_='stat')

star = results[1].text
commints = results[3].text
Contributed = results[5].text

##no use now
