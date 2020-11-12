import requests
import json
from riotwatcher import LolWatcher, ApiError
from pprint import pprint
import pandas as pd
import statistics

key = 'RGAPI-ae57350a-573b-411a-8b72-2b32d30f5ae9'
match_id = '3648293057'
url = 'https://na1.api.riotgames.com/lol/match/v4/timelines/by-match/' + match_id + '?api_key=' + key
my_region = 'na1'
#platform_host = 'na1.api.riotgames.com'
#region_host = 'americas.api.riotgames.com'



#pulls a players stats by username/region
def ten_minute_data(username):
    lol_watcher = LolWatcher(key)
    me = lol_watcher.summoner.by_name('na1', username)


    my_matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])
    last_match = my_matches['matches'][0]
    match_detail = lol_watcher.match.by_id(my_region, last_match['gameId'])

    participants = []

    for row in match_detail['participants']:
        participants_row = {}

        if row['stats']['win'] == True:
            participants_row['win'] = 1
        else:
            participants_row['win'] = 0

        if row['stats']['firstBloodKill'] == True:    
            participants_row['FirstBlood'] = 1
        else:
            participants_row['FirstBlood'] = 0

        if row['teamId'] == 100:
            participants_row['team'] = 'blue'
        else:
            participants_row['team'] = 'red'

        participants_row['csPerMinute'] = row['timeline']['creepsPerMinDeltas']['0-10']
        participants_row['goldPerMin'] = row['timeline']['goldPerMinDeltas']['0-10']
        participants_row['xpPerMin'] = row['timeline']['xpPerMinDeltas']['0-10']
        participants.append(participants_row)
        
    df = pd.DataFrame(participants)



    df2 = pd.DataFrame({
        "blueFirstBlood" : [df[0:5]['FirstBlood'].max()],
        "redFirstBlood" : [df[5:10]['FirstBlood'].max()],
        "blueCSPerMin" : [df[0:5]['csPerMinute'].sum()],
        "redCSPerMin" : [df[5:10]['csPerMinute'].sum()],
        "blueGoldPerMin" : [df[0:5]['goldPerMin'].sum()],
        "redGoldPerMin" : [df[5:10]['goldPerMin'].sum()],
        "blueTotalExperience" : [df[0:5]['xpPerMin'].sum() * 10],
        "redTotalExperience" : [df[5:10]['xpPerMin'].sum() * 10],
        "blueExperienceDiff" : 0,
        "redExperienceDiff" : 0,
        "blueWins": [df[0:5]['win'].mean()]
    })


    df2['blueExperienceDiff'] = df2['blueTotalExperience'] - df2['redTotalExperience']
    df2['redExperienceDiff'] = df2['redTotalExperience'] - df2['blueTotalExperience']




    print(df2.to_string())
    
ten_minute_data('euro gigolo')