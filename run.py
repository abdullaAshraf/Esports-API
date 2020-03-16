from flask import Flask, request
from flask_restful import Resource, Api
from resources.Player import Player
from resources.Team import Team
from resources.Tournament import Tournament
from resources.Game import Game
from resources.Game import TeamGames
from resources.Performance import Performance

app = Flask(__name__)
api = Api(app)

api.add_resource(Player, '/Player/<string:teamName>')
api.add_resource(Team, '/Team/<string:tournament>')
api.add_resource(Tournament, '/Tournament/')
api.add_resource(Game, '/Game/<string:tournament>')
api.add_resource(TeamGames, '/TeamGames/<string:tournament>/<string:team>/<string:date>')
api.add_resource(Performance, '/Performance/<string:tournament>/<string:player>/<string:date>')

if __name__ == "__main__":
    app.run(debug=True)
