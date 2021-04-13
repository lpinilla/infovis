import mechanize
from bs4 import BeautifulSoup
import http.cookiejar
from locale import atof, setlocale, LC_NUMERIC

base_url = "https://duome.eu/LautaroGon56636/"
progress_url = base_url + "progress"
swedish_url = base_url + "en/sv" #parecería tener toda la info relavante porque solo aprendo 1 idioma

setlocale(LC_NUMERIC, '')
cj = http.cookiejar.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.set_handle_robots(False)

#parseando el log raw de actividad
br.open(swedish_url)
response = br.response().read().decode('utf-8')
#br.close()
soup = BeautifulSoup(response, 'lxml')
info = soup.find_all('div')
#info = soup.find('div', {'id': 'raw'})
print(info)
#filtered = [x.text for x in info if "data-field" in x.attrs]

