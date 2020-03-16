from flask_restful import Resource
import mwclient
site = mwclient.Site('lol.gamepedia.com', path='/')


class Game(Resource):
    def get(self,tournament):
        response = site.api('cargoquery',
                            limit='max',
                            tables="ScoreboardGame",
                            fields="Tournament,Team1,Team2,WinTeam,DateTime_UTC,UniqueGame",
                            where=f"Tournament like '{tournament}'",
                            order_by=f"DateTime_UTC"
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

