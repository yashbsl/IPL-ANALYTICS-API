from flask import Flask,jsonify,request
import ipl


app=Flask(__name__)

@app.route('/')
def home():
    return 'Hello world'

@app.route('/api/teams')
def teams():
    teams=ipl.teamAPI()
    return jsonify(teams)

@app.route('/api/teamvteam')
def teamvteam():
    team1=request.args.get('team1')
    team2=request.args.get('team2')
    response=ipl.team_vs_team(team1,team2)
    return jsonify(response)

@app.route('/api/playermatches')
def playermatches():
    player=request.args.get('player')
    response=ipl.player_matches(player)
    return jsonify(response)
app.run(debug=True)