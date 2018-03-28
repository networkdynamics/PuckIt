# -*- coding: utf-8 -*-

import requests
import json
import datetime

def main():
	scrape()

def scrape():
	
	# NHL API endpoints
	team_url = 'https://statsapi.web.nhl.com/api/v1/teams'
	roster_url = 'https://statsapi.web.nhl.com/api/v1/teams/{}?expand=team.roster'
	player_url = 'https://statsapi.web.nhl.com/api/v1/people/{}'
	standings_url = 'https://statsapi.web.nhl.com/api/v1/standings'
	teams_dir = '/home/ndg/projects/shared_datasets/PuckIt/data/{}/{}'

	# Get team and standings data
	team_response = requests.get(team_url)
	standings_response = requests.get(standings_url)

	if not team_response.ok or not standings_response.ok:
		print "Problem retrieving teams or standings data."
		quit()

	teams_data = json.loads(team_response.content)
	standings_data = json.loads(standings_response.content)['records']

	for team in teams_data['teams']:
		
		# Get the team id, name, division id, and team metadata
		team_id = team['id']
		team_name = team['name']
		division_id = team['division']['id']
		req = roster_url.format(team_id)
		team_data = json.loads(requests.get(req).content)['teams'][0]
		roster = team_data['roster']['roster']

		# Get the standings for the division of the current team.
		division_standings = [division for division in standings_data if division['division']['id'] == division_id][0]

		# Get the team record from the division standings
		team_record = dict([team for team in division_standings['teamRecords'] if team['team']['id'] == team_id][0])

		print "Division Name:", division_standings['division']['name']
		print "Team ID:", team_id
		print "Team Name:", team_name

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
			print '\t', player_id, player_data['fullName']
			players.append(player_data)

		# Combine data
		team_data['roster'] = players
		team_data['record'] = team_record

		# Get the team directory name
		team_dir_name = team_name.replace(' ', '_')

		# Special cases:
		if team_name == u'Montréal Canadiens':
			team_dir_name = "Montreal_Canadiens"
		elif team_name == u'St. Louis Blues':
			team_dir_name = "St_Louis_Blues"
		
		# Generate our timestamped filename
		timestamp = datetime.datetime.now().isoformat()
		file_name = 'NHL_data_{}.json'.format(timestamp)

		# Save the file into our data directory.
		team_dir_full = teams_dir.format(team_dir_name, file_name)
		with open(team_dir_full, 'w') as outfile:
			json.dump(team_data, outfile, indent=4, sort_keys=True)
		print "Saved data for team {} to {}".format(team_dir_name, team_dir_full)

if __name__ == '__main__':
	main()
