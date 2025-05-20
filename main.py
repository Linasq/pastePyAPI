import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup

app = FastAPI()
with open("cookie1", "r") as f:
    idf = f.read().strip()

with open("cookie2", "r") as f:
    cfc = f.read().strip()


# access only text from each tag
async def get_text(text):
    soup = BeautifulSoup(text.text, 'html.parser')

    h_code = soup.find_all('div', class_='snippet')
    h_codes = [i.get_text(separator=' ', strip=True) for i in h_code]

    h_date = soup.find_all('div', class_='date')
    h_dates = [i.get_text(separator=' ', strip=True) for i in h_date]

    h_title = soup.find_all('div', class_='post-search-title')
    h_titles = [i.get_text(separator=' ', strip=True) for i in h_title]
    h_link = []
    for i in h_title:
        i_str = str(i)
        num = i_str.find('href')
        link = i_str[num+6:num+15]
        h_link.append(f'https://pastebin.com{link}')

    return {i:{"date":h_dates[i],"title":h_titles[i],"link":h_link[i],"snippet":h_codes[i]} for i in range(len(h_titles))}


@app.get("/search")
async def find_pastes(q: str = ""):
    # check if there was param given
    if not q: return {"":""}

    # make a request to pastebin
    cookies = {"_identity-frontend":idf, "cf_clearance":cfc}
    response = requests.get(f'https://pastebin.com/search?q={q}', cookies=cookies)

    return await get_text(response)
