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
