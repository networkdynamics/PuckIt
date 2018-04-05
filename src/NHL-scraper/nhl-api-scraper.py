# -*- coding: utf-8 -*-

import requests
import json
import datetime

def main():
	scrape()

def scrape():
	
	# Seasons to scrape for
	seasons = ['20132014', '20142015', '20152016', '20162017', '20172018']

	# NHL API endpoints
	team_url = 'https://statsapi.web.nhl.com/api/v1/teams?season={}'
	roster_url = 'https://statsapi.web.nhl.com/api/v1/teams/{}?expand=team.roster&season={}'
	player_url = 'https://statsapi.web.nhl.com/api/v1/people/{}'
	standings_url = 'https://statsapi.web.nhl.com/api/v1/standings?season={}'
	teams_dir = '/home/ndg/projects/shared_datasets/PuckIt/data/{}/{}'

	nhl_teams = {}

	# Iterate over each season
	for season in seasons:

		# Get team and standings data
		team_response = requests.get(team_url.format(season))
		if not team_response.ok:
			print "Problem retrieving teams data."
			quit()

		# Pull the season standings
		s_url = standings_url.format(season)
		standings_response = requests.get(s_url, season)

		if not standings_response.ok:
			print "Problem retrieving standings data for the {} season.".format(season)
			continue

		teams_data = json.loads(team_response.content)
		teams_data = convert(teams_data) # Convert all strings to ascii
		standings_data = json.loads(standings_response.content)['records']
		standings_data = convert(standings_data) # Convert all strings to ascii

		print "Season:", season

		for team in teams_data['teams']:

			# Get the team id, name, division id, and team metadata
			team_id = team['id']
			team_name = team['name']

			team_name = normalize_team(team_name)

			print "Team ID:", team_id
			print "Team Name:", team_name

			franchise_id = team['franchiseId']
			print "Franchise ID:", franchise_id
			division_id = team['division']['id']
			req = roster_url.format(team_id, season)
			resp = requests.get(req).content
			team_data = json.loads(resp)['teams'][0]
			team_data = convert(team_data) # Convert all strings to ascii
			roster = team_data['roster']['roster']

			if franchise_id not in nhl_teams.keys():
				nhl_teams[franchise_id] = {}

			# Get the standings for the division of the current team.
			division_standings = [division for division in standings_data if division['division']['id'] == division_id][0]

			# Get the team record from the division standings
			team_record = dict([team for team in division_standings['teamRecords'] if team['team']['id'] == team_id][0])

			print "Division Name:", division_standings['division']['name']

			# Make sure we're looking at regular season data.
			if division_standings['standingsType'] != 'regularSeason':
				print "Didn't obtain regular season standings data."

			# Delete duplicated team key
			team_record.pop('team', None)

			# Now scrape player metadata for each player on the team roster.
			players = []
			print "Roster players:"
			for player in roster:

				# Get the player ID and pull their metadata
				player_id = player['person']['id']
				req = player_url.format(player_id)
				player_data = json.loads(requests.get(req).content)['people'][0]
				player_data = convert(player_data)
				print '\t', player_id, player_data['fullName']
				players.append(player_data)

			# Combine data
			team_data['roster'] = players
			team_data['record'] = team_record

			nhl_teams[franchise_id][season] = team_data

	for franchise_id, team_data in nhl_teams.iteritems():

		team_name = team_data[seasons[len(seasons)-1]]['name']
		team_name = normalize_team(team_name)

		# Get the team directory name
		team_dir_name = team_name.replace(' ', '_')
		
		# Generate our timestamped filename
		timestamp = datetime.datetime.now().isoformat()
		file_name = 'NHL_data_{}.json'.format(timestamp)

		# Save the file into our data directory.
		team_dir_full = teams_dir.format(team_dir_name, file_name)
		with open(team_dir_full, 'w') as outfile:
			json.dump(team_data, outfile, indent=4, sort_keys=True)
		print "Saved data for team {} to {}".format(team_dir_name, team_dir_full)

def convert(dictionary):
    if isinstance(dictionary, dict):
        return {convert(key): convert(value) for key, value in dictionary.iteritems()}
    elif isinstance(dictionary, list):
        return [convert(element) for element in dictionary]
    elif isinstance(dictionary, unicode):
        return dictionary.encode('utf-8')
    else:
        return dictionary

def normalize_team(team_name):
	
	# Special cases
	if team_name == 'Montréal Canadiens':
		team_name = "Montreal Canadiens"
	elif team_name == 'St. Louis Blues':
		team_name = "St Louis Blues"

	return team_name

if __name__ == '__main__':
	main()
