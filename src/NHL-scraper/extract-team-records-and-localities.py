import json
import datetime
import os
from dateutil import parser
from pprint import pprint

data_dir = '/home/ndg/projects/shared_datasets/PuckIt/data/'

team_files = {}
teams_data = {}

def main():
	
	for subdir, dirs, files in os.walk(data_dir):
		print subdir

		timestamps = {}
		for file in files:
			
			if file.startswith('NHL_data_'):
				filepath = os.path.join(subdir, file)
				timestamp = file[9:file.find('.json')]
				#print timestamp, file
				#print "hour", parser.parse(timestamp).hour
				timestamps[filepath] = timestamp
		
		if len(timestamps) == 0:
			continue

		# Sort the filenames by timestamp
		sorted_files = sorted(timestamps, key=timestamps.get, reverse=True)

		# Get the latest JSON file
		latest_file = sorted_files[0]

		team_name = subdir.split('/')[-1]
		team_files[team_name] = latest_file

	pprint (team_files)

	for team_name, team_file in team_files.iteritems():
		with open(team_file) as data_file:
			team_data = json.load(data_file)

		teams_data[team_name] = {}

		for season, season_data in team_data.iteritems():
			conference_rank = season_data['record']['conferenceRank']
			division_rank = season_data['record']['divisionRank']
			goals_scored = season_data['record']['goalsScored']
			goals_against = season_data['record']['goalsAgainst']
			assert(season_data['record']['leagueRecord']['type'] == 'league')
			num_wins = season_data['record']['leagueRecord']['wins']
			num_losses = season_data['record']['leagueRecord']['losses']
			num_ot_losses = season_data['record']['leagueRecord']['ot']
			num_points = season_data['record']['points']
			num_regular_overtime_wins = season_data['record']['row']

			team_record = {}
			team_record['conference_rank'] = conference_rank
			team_record['division_rank'] = division_rank
			team_record['goals_scored'] = goals_scored
			team_record['goals_against'] = goals_against
			team_record['num_wins'] = num_wins
			team_record['num_losses'] = num_losses
			team_record['num_ot_losses'] = num_ot_losses
			team_record['num_points'] = num_points
			team_record['num_regular_overtime_wins'] = num_regular_overtime_wins
			
			teams_data[team_name][season] = team_record

	with open('team_records.json', 'w') as outfile:
		json.dump(teams_data, outfile, indent=4, sort_keys=True)




if __name__ == '__main__':
	main()
