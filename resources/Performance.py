from flask_restful import Resource
import mwclient
site = mwclient.Site('lol.gamepedia.com', path='/')

def calculatePlayerScore(data):
        totalPoints = 0
        gamePoints = 0
        gameCount = 0
        for gameRecord in data:
            game = gameRecord['title']

            if gameCount+1 == int(game['N GameInMatch']):
                gameCount += 1
            else:
                totalPoints += gamePoints/gameCount
                gameCount = 1
                gamePoints = 0

            gamePoints += 2*int(game['Kills'])
            gamePoints -= 0.5*int(game['Deaths'])
            gamePoints += 1.5*int(game['Assists'])
            gamePoints += 0.01*int(game['CS'])
            if int(game['Kills']) + 1.5*int(game['Assists']) >= 10 :
                gamePoints += 2
            if game['PlayerWin'] == 'Yes' :
                gamePoints += 5

        totalPoints += gamePoints/gameCount
        return totalPoints

class Performance(Resource):
    def get(self,tournament,player):
        response = site.api('cargoquery',
                            limit='max',
                            tables="ScoreboardGame=SG,ScoreboardPlayer=SP",
                            fields="SP.Name,SP.Champion,SP.Kills,SP.Deaths,SP.Assists,SP.Gold,SP.CS,SP.PlayerWin,SP.Role,SG.DateTime_UTC,SG.Gamelength_Number,SG.N_GameInMatch",
                            where=f"SG.Tournament like '{tournament}'and SP.Name like '{player}'",
                            join_on = "SG.UniqueGame =SP.UniqueGame",
                            order_by=f"SG.DateTime_UTC"
                            )
        data = response['cargoquery']
        
        points = calculatePlayerScore(data)

        return points

    