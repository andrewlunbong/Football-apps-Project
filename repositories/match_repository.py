from db.run_sql import run_sql
from models.match import Match
from models.team import Team
import repositories.team_repository as team_repository
import repositories.match_result_repository as match_result_repository

#save matches
def save(match):
    sql = "INSERT INTO matches (home_team_id, away_team_id) VALUES ( %s, %s ) RETURNING id"
    values = [match.home_team.id, match.away_team.id]
    results = run_sql( sql, values )
    print(results)
    match.id = results[0]['id']
    # match.id = id
    return match

#select all matches in sql
def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for row in results:
        home_team = team_repository.select(row['home_team_id'])
        away_team =team_repository.select(row['away_team_id'])
        match = Match(home_team, away_team, row['id'])
        matches.append(match)
    return matches

#select individual match from sql
def select(id):
    match = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        # ask team repo for team using id
        home_team = team_repository.select(result['home_team_id'])
        away_team = team_repository.select(result['away_team_id'])

        match = Match(home_team, away_team, result['id'] )
    return match


def matches_by_team(team):
    matches = []

    sql = "SELECT matches.* FROM matches INNER JOIN match_results ON match_results.match_id = match.id WHERE team = %s"
    values = [match.id]
    results = run_sql(sql, values)

    for row in results:
        match = Match(row['home_team'], row['away_team'], row['id'])
        matches.append(match)

    return matches

#delete all matches
def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)

# selct matches that not been played e.g match that have no result
def select_pending():
    all_matches = select_all()
    all_match_results = match_result_repository.select_all()

    matches_not_played = []
    for match in all_matches:
        match_has_been_played = False
        for match_result in all_match_results:
            if (match_result.match.id == match.id) :
                match_has_been_played = True
        if not match_has_been_played:
            matches_not_played.append(match)
    return matches_not_played
#select team that have not played yet(fixture)
def select_pending_for_team(team):
    matches_not_played = select_pending()
    matches_not_played_for_team = []

    for match_not_played in matches_not_played:
        if match_not_played.home_team.id == team.id:
            matches_not_played_for_team.append(match_not_played)
        elif match_not_played.away_team.id == team.id:
            matches_not_played_for_team.append(match_not_played)
    
    return matches_not_played_for_team


def select_by_team():
    matches = []
    teams = []

    sql = "SELECT * FROM matches"
    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    results = run_sql(sql)

    for row in results:
        home_team = team_repository.select(row['home_team_id'])
        away_team =team_repository.select(row['away_team_id'])
        match = Match(home_team, away_team, row['id'])
        matches.append(match)
    return matches
