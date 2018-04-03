# PuckIt
How do online communities inform the nature of offline communities! 🏒

## Data Storage Scheme
Data Path: `/home/ndg/projects/shared_datasets/PuckIt/data`

Inside the `data` directory is a directory for each team.

The naming convention of the team directories is as follows:
* Get the teams names from `nhl_teams.txt` from `/resources`.
* Replace spaces in the team name with underscores.

All team level data is stored in team directories with uniform names.

* `about.json`: contains the about page meta data for each subreddit.
* `moderators.json`: contains the moderator meta data for each subreddit.
* `NHL_data*.json`: contains data scraped using the NHL API.
* `reddit_comments.txt`: contains all the reddit comments for each subreddit between Sept 2016 - Jan 2018.
* `reddit_posts.txt`: contains all the reddit posts for each subreddit between Sept 2016 - Jan 2018.

Aggregate data can be stored directly in `/data` in `.json` format with approproiate file names.


 
