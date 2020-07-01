import requests
from bs4 import BeautifulSoup
from skpy import Skype
from creds import username, password, groupID

country = "russia"

url = "https://www.worldometers.info/coronavirus/country/"

link = url.__add__(country)

def get_covid_stats():

    r = requests.get(link)

    normal_view = BeautifulSoup(r.content, 'html.parser')

    normal_view.decode() and normal_view.prettify()

    text = normal_view.get_text()

    line = []

    line.append(text.strip('\n'))

    final_line = [x.replace('\n', '') for x in line]

    result = ('\n'.join(final_line))

    snipple = result.split(":")[1]

    head, sep, tail = snipple.partition('-')

    data = "Today's COVID-19 statistics for: \n" + result.split(" ")[2] + " \n" + head

    return data


def sender_bot():

    creds = {
        "username": username,
        "password": password,
        "groupID": groupID
    }

    msg = get_covid_stats()

    sk = Skype(creds["username"], creds["password"])

    channel = sk.chats.chat(creds["groupID"])

    channel.sendMsg(msg)


if __name__ == '__main__':
    sender_bot()
