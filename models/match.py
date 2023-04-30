class Match:
    def __init__(self, home_team,home_team_score away_team, winning_team, id = None):
        self.home_team = home_team
        self.home_team_score = home_team_score
        self.away_team = away_team
        self.winning_team = winning_team
        self.id = id


in the result >{match.home_team} {home_team_score} - {away_team_score} {away_team}

Match  - matches that are yet to happen
Result - matches that already happened