import requests
from bs4 import BeautifulSoup
import csv

for page in range(1,2):
  url = f"https://finance.naver.com/sise/sise_market_sum.nhn?&page={page}"
  res = requests.get(url)
  res.raise_for_status()
  print(res.status_code)
  soup = BeautifulSoup(res.text, "lxml")
  data_rows = soup.find("tbody").find_all("tr")
    
  for row in data_rows:
    columns = row.find_all("td")
    if len(columns)<=1:
      continue
    results = []
    for column in columns:
      data = column.get_text().strip()
      if len(data)==0:
        continue
      results.append(data)
        
    f = open("kospi100.csv", mode="a", encoding="utf-8-sig", newline="")
    fw = csv.writer(f)
    fw.writerow(results)
    f.close()