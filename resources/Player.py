from flask_restful import Resource
from  resources.Tournament import getTournaments
from  resources.Team import getPlayers
import mwclient
site = mwclient.Site('lol.gamepedia.com', path='/')


class Player(Resource):
    def get(self, teamName):
        if teamName == 'All':
            tournaments =  getTournaments()
            players = getPlayers(tournaments)

            conditionString = ""
            for player in players:
                conditionString += "or ID like '" +  player['ID'] + "' "
            response = site.api('cargoquery',
                                limit='max',
                                tables="Players",
                                fields="ID,Name,Image,Country,Age,Team,Role",
                                where=f"(Role like 'Mid' or Role like 'Top' or Role like 'Bot' or Role like 'Support' or Role like 'Jungler') and (false " + conditionString +")"
                               )
            data = response['cargoquery']
            playersList = []
            for item in data:
                playerData = item['title']
                for player in players:
                    if playerData['ID'] == player['ID']:
                        playerData['Team'] = player['Team']
                        playerData['Tournament'] = player['Tournament']
                        playersList.append(playerData)
                        break
            return playersList
        else:
            response = site.api('cargoquery',
                                limit='max',
                                tables="Players",
                                fields="ID,Name,Image,NameAlphabet,Country,Age,Team,Role",
                                where=f"Team like '{teamName}'"
                                )
            data = response['cargoquery']
            return data
