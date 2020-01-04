from flask_restful import Resource
import mwclient
site = mwclient.Site('lol.gamepedia.com', path='/')


class Team(Resource):
    def get(self, tournament):
        response = site.api('cargoquery',
                            limit='max',
                            tables="TournamentRosters",
                            fields="Team,Tournament,RosterLinks",
                            where=f"Tournament like '{tournament}'"
                            )
        data = response['cargoquery']
        return data


def getTeams(tournaments):
    teamsList = []
    t = Team()
    for tournament in tournaments:
        data = t.get(tournament)
        for item in data:
            team = item['title']
            teamsList.append(team['Team'])
    return teamsList

def getPlayers(tournaments):
    playersList = []
    t = Team()
    for tournament in tournaments:
        data = t.get(tournament)
        for item in data:
            team = item['title']
            roster = team['RosterLinks']
            players = roster.split(";;")
            for player in players:
                playerObject = {
                    'ID':player.split(" ")[0],
                    'Tournament': tournament,
                    'Team': team['Team']
                }
                playersList.append(playerObject)
    return playersList

