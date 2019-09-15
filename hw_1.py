#### Task 1
import requests
import json
import os


USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36'

api_url_gihub = 'https://api.github.com'


def git_user_repos(username):

    full_url = api_url_gihub + "/users/" + username + "/repos"
    print(full_url)
    response = requests.get(full_url, headers={'User-Agent': USER_AGENT})
    data = response.json()
    with open(username + "_repos.json", 'w') as f:
        json.dump(data, f)

git_user_repos("dv4silj3v")


#### Task 2


class GetCityForecast:
    def __init__(self, country, city):
        self.country = country
        self.city = city
        with open('app.id', 'r', encoding='UTF-8') as f:
            self._appid = f.readlines()[0]

    def _findcityid(self):
        """Find the city ID from the file"""
        with open('city.list.json', 'r') as f:
            citylist = json.load(f)
            cityid = 0
            for j in citylist:
                if j['country'] == self.country and j['name'] == self.city:
                    cityid = j['id']
            if cityid != 0:
                return cityid
            else:
                print("City or country doesn't exist in database")
                exit(1)

    def dump_forecast(self):
        """Dump weather forecast into a json file"""
        url = 'http://api.openweathermap.org/data/2.5/weather?id=' + str(
            self._findcityid()) + '&&units=metric&APPID=' + str(self._appid)
        print(url)
        outputfile = self.city + '.json'

        if os.path.exists(outputfile):
            os.remove(outputfile)
        try:
            response = requests.get(url, headers={'User-Agent': USER_AGENT})
            data = response.json()
            with open(outputfile, 'w') as f:
                json.dump(data, f)
        except:
            print("Couldn't download file. Exiting")
            exit(1)


if __name__ == '__main__':
    testing = GetCityForecast("RU", "Moscow")
    testing.dump_forecast()
    print(1)