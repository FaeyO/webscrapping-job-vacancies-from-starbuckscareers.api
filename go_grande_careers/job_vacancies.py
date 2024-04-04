import requests
import json
import pandas as pd

url = "https://starbuckscareersapi.azurewebsites.net/api/vacancies"

payload = {}
headers = {
  'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
  'Accept': 'application/json, text/plain, */*',
  'Referer': 'https://www.starbucksemeacareers.com/',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
  'sec-ch-ua-platform': '"Windows"',
  'Cookie': 'ARRAffinity=508248a66ee3f731d42da548f5b70665cdd93faa18d956ff97e74235a048f410; ARRAffinitySameSite=508248a66ee3f731d42da548f5b70665cdd93faa18d956ff97e74235a048f410'
}

response = requests.get(url, headers=headers)

go_grande_careers = response.json()

careers_df = pd.json_normalize(go_grande_careers)

careers_df.to_csv('grande_careers.csv', index=False)



