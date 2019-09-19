import requests
from bs4 import BeautifulSoup


def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return 0
    elif reply[0] == 'n':
        return 1
    else:
        return yes_or_no("Please Enter (y/n) ")


def job_request(url, vacancy):

    USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'snap Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36'

    response = requests.get(url, headers={'User-Agent': USER_AGENT}, params=vacancy)

    return response.text


def hh_parsing(searchstr):

    hh_url = 'https://hh.ru/search/vacancy'


    n = 0

    while True:

        hh_vacancy = {
            'text': searchstr,
            'page': n
        }

        hh_html = job_request(hh_url, hh_vacancy)

        soup = BeautifulSoup(hh_html, 'html.parser')

        vacancies = soup.findAll('div', {'class': 'vacancy-serp-item__row vacancy-serp-item__row_header'})
        for vacancy in vacancies:
            print(vacancy.find('a').string)
            print(vacancy.find('a')['href'])
            try:
                print(vacancy.find('div', {'class': "vacancy-serp-item__compensation"}).string)
            except AttributeError:
                print("Salary Unknown")
            print('***************')

        n += 1

        if(yes_or_no('Continue search on hh.ru? ')):
            break


def sj_parsing(searchstr):

    sj_url = 'https://superjob.ru/vacancy/search/'

    n = 0

    while True:

        sj_vacancy = {
            'keywords': searchstr,
            'page': n
        }

        sj_html = job_request(sj_url, sj_vacancy)

        soup = BeautifulSoup(sj_html, 'html.parser')

        for link in soup.find_all('a'):
            print(link)
            print(link.get('href'))

        n += 1

        if(yes_or_no('Continue search on superjob.ru? ')):
            break

searchstr = input("Enter desired job to search: ")

hh_parsing(searchstr)
sj_parsing(searchstr)