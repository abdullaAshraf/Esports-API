from flask_restful import Resource
from datetime import date
import mwclient
site = mwclient.Site('lol.gamepedia.com', path='/')

class Tournament(Resource):
    def get(self):
        today = date.today()
        year = today.strftime("%Y")
        month = today.strftime("%m")
        split = ""
        if int(month) >= 6:
            split = 'Summer'
        else:
            split = 'Spring'
        response = site.api('cargoquery',
                            limit='max',
                            tables="Tournaments",
                            fields="Name,Date,Region",
                            where=f"EventType = 'Offline' and Year ='{year}' and TournamentLevel = 'Primary' and IsQualifier = 'No' and IsPlayoffs = 'No' and Split = '{split}'"
                            )
        data = response['cargoquery']
        return data


def getTournaments():
    data = Tournament().get()
    tournamentsList = []
    for item in data:
        tournament = item['title']
        tournamentsList.append(tournament['Name'])
    return tournamentsList

