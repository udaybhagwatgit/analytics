from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import pandas as pd
from bs4 import BeautifulSoup
import requests
import collections

def open_cricinfo_and_begin_mining():
    url = "http://www.espncricinfo.com/scores/series/8048/season/2019/ipl"
    baseurl = "http://www.espncricinfo.com"
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.findAll('a', href=True, text='SCORECARD')
    scorecard_links = []
    #Named Tuple
    Batsman = collections.namedtuple('Batsman', [
        'BatsmanName',
        'RunsScored'
    ]
    )

    batsman_frame_list = []
    for each_link in links:
        scorecard_links.append(baseurl + each_link['href'])
        scorecard_link = baseurl + each_link['href']
        scorecard_response = requests.get(scorecard_link)
        scorecard_obj = BeautifulSoup(scorecard_response.content, 'html.parser')
        batsmen_list = scorecard_obj.select("div.scorecard-section.batsmen div.wrap.batsmen")
        batsman_info_list = []
        for each_batsmen_obj in batsmen_list:
            each_batsmen = each_batsmen_obj.select("div.cell.batsmen a")
            batsmen_name = each_batsmen[0].string
            run_scored_obj = each_batsmen_obj.select("div.cell.runs")
            run_scored = run_scored_obj[0].string
            batsman_data = Batsman(BatsmanName=batsmen_name, RunsScored=run_scored)
            batsman_info_list.append(batsman_data)
        df = pd.DataFrame.from_records(batsman_info_list, columns=Batsman._fields, )
        batsman_frame_list.append(df)

    print(batsman_frame_list)
        

open_cricinfo_and_begin_mining()