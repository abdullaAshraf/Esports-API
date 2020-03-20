from flask_restful import Resource
import mwclient
from  resources.Tournament import getTournaments
site = mwclient.Site('lol.gamepedia.com', path='/')


class Game(Resource):
    def get(self,date):
        tournaments =  getTournaments()
        conditionString = "false"
        for tournament in tournaments:
            conditionString += f" or SG.Tournament like '{tournament}'"
        response = site.api('cargoquery',
                           limit='max',
                            tables="ScoreboardGame=SG,ScoreboardPlayer=SP",
                            fields="SP.Name,SP.Link,SP.Champion,SP.Kills,SP.Deaths,SP.Assists,SP.Gold,SP.CS,SP.PlayerWin,SP.Role,SG.DateTime_UTC,SG.Gamelength_Number,SG.N_GameInMatch",
                            where= f"SG.DateTime_UTC >= '{date}' and ({conditionString})",
                            join_on = "SG.UniqueGame =SP.UniqueGame",
                            order_by=f"SG.DateTime_UTC DESC"
                            )
        data = response['cargoquery']
        return data

def countMatches(data):
    count = 0
    for gameRecord in data:
        game = gameRecord['title']
        if (int(game['N GameInMatch']) == 1):
            count += 1
    return count


class TeamGames(Resource):
    def get(self,tournament,team,date):
        response = site.api('cargoquery',
                            limit='max',
                            tables="ScoreboardGame",
                            fields="Tournament,Team1,Team2,WinTeam,DateTime_UTC,N_GameInMatch",
                            where=f"Tournament like '{tournament}' and (Team1 like '{team}' or Team2 like '{team}') and DateTime_UTC >= '{date}'",
                            order_by=f"DateTime_UTC"
                            )
        data = response['cargoquery']
        return countMatches(data)

