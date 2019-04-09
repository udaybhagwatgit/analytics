from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import requests

def open_cricinfo_and_begin_mining():
    url = "http://www.espncricinfo.com/scores/series/8048/season/2019/ipl"
    baseurl = "http://wwww.espncricinfo.com"
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.findAll('a', href=True, text='SCORECARD')
    scorecard_links = []
    for each_link in links:
        scorecard_links.append(baseurl + each_link['href'])

    for each_scorecard_link in scorecard_links:
        scorecard_response = requests.get(each_scorecard_link)
        scorecard_obj = BeautifulSoup(scorecard_response.content, 'html.parser')
        

open_cricinfo_and_begin_mining()