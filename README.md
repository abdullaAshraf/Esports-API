# Esports-API
Python Flask REST API that utilizes Leaguepedia to allow access League of Legends Esports teams and events data using simple HTTP requests

## Reflection
This is a personal project to practise using technologies like `RESTful API`, 'Pyhton' and `Flask`.

This is a RESTful API to provide simple endpoints to access live data about esports events and players, and it is used in my esports fantasy app:
https://github.com/abdullaAshraf/Esports_Fantasy

The main challenge in maintaining such an app is to provide live esports events updates, but no reliable RESTful API allow access to esports data for free, and manually maintaing and updating a database of all matches and tournaments will be lots of work, finally I found a website called "Leaguepedia" which is a community based wiki site that provide live updates and esports statistics, and they have a free API but it is very confusing with many overlapping and deprecated tables. In addition to not having REST endpoints for it, instead they depend on a Pyhton client library called "mwclient",
so this API is like a simple proxy that deal with the technicalities about connecting to the wiki API, joining and filtering tables, and provide a simple API to be used within any other project.

## Endpoints

- /Player/'Team Name':
get all current players inside a League of legends team.

- /Players/:
get all players in pro League of legends esports in current season (LPL,LCK,LCS,LEC).

- /Team/'Tournament Name':
get all teams that currently partcipate in a specific tournament.

- /Tournament:
get all current season major tournaments.

- /Game/'Timestamp':
get all games played in the 4 major tournaments starting at the timestamp.

- /TeamGames/'Tournament Name'/'Team Name'/'Timestamp'
get games played by a specific team in a tournament stating at thr timestamp.

- /Performance/'Tournament Name'/'Player ID'/'Timestamp'
get games played by a specific player in a tournament stating at the timestamp.
Player ID is the player tag followed by the player name in the format: 'tag' ('name')
it is the way the API uses to differentiate between players with the same tag

## How to use

You can either build it and upload on any hosting server, or use mine which is already hosted at:
https://esports.now.sh/
