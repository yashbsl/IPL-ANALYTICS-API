import pandas as pd
import numpy as np

matches=pd.read_csv('ipl.csv')
# print(matches.head())

def teamAPI():
   teams= list(set(list(matches['team1'])+list(matches['team2'])))
   team_dict={
      'teams':teams
   }
   return team_dict

def team_vs_team(team1,team2):

   valid_teams=list(set(list(matches['team1'])+list(matches['team2'])))

   if team1 in valid_teams and team2 in valid_teams:
         temp_df=matches[(matches['team1']==team1)&(matches['team2']==team2)|(matches['team1']==team2)&(matches['team2']==team1)]
         total_matches= temp_df.shape[0]

         matches_won_team1=temp_df['winner'].value_counts()[team1]
         matches_won_team2=temp_df['winner'].value_counts()[team2]

         draw=total_matches-(matches_won_team1 + matches_won_team2)

         response={
            'total_matches':str(total_matches),
            team1:str(matches_won_team1),
            team2:str(matches_won_team2),
            'draw':str(draw)
         }
   
         return response
   else:
       return {'message':'Invalid team name'}

def player_matches(player):

    temp_df = matches[
        matches['team1_players'].str.contains(player, na=False) |
        matches['team2_players'].str.contains(player, na=False)
    ]

    response = []

    for _, row in temp_df.iterrows():
        response.append({
            'match_date': row['match_date'],
            'season': row['season'],
            'team1': row['team1'],
            'team2': row['team2'],
            'venue': row['venue'],
            'city': row['city'],
            'winner': row['winner'],
            'player_of_match': row['player_of_match'],
            'match_type': row['match_type'],
            'result': row['result'],
            'result_margin': row['result_margin']
        })

    return {
        'player': player,
        'matches_played': len(response),
        'matches': response
    }