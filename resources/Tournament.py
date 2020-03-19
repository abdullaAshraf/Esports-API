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

        regions = ['Korea','North America','Europe','China']
        reigonsString = 'false'
        for reg in regions:
            reigonsString += " or Region = '" + reg + "'"
        

        response = site.api('cargoquery',
                            limit='max',
                            tables="Tournaments",
                            fields="Name,Date,Region,EventType",
                            where=f"TournamentLevel = 'Primary' and Year ='{year}' and IsQualifier = 'No' and IsPlayoffs = 'No' and Split = '{split}'  and ( {reigonsString} )"
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

