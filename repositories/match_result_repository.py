from db.run_sql import run_sql
from models.match_result import MatchResult
import repositories.team_repository as team_repository
import repositories.match_repository as match_repository

def save(match_result):
    sql = "INSERT INTO match_results( home_team_score, away_team_score, match_id, winning_team_id) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [match_result.home_team_score, match_result.away_team_score, match_result.match.id, match_result.winning_team.id]
    results = run_sql( sql, values )
    match_result.id = results[0]['id']
    return match_result


def select_all():
    match_results = []

    sql = "SELECT * FROM match_results"
    results = run_sql(sql)

    for row in results:
        home_team_score = row["home_team_score"]
        away_team_score = row["away_team_score"]
        match = match_repository.select(row['match_id'])
        winning_team = team_repository.select(row['winning_team_id'])
        match_result = MatchResult(home_team_score, away_team_score, match, winning_team, row['id'])
        match_results.append(match_result)
    return match_results


def delete_all():
    sql = "DELETE FROM match_results"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM match_results WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select_match_that_has_result_by_team(team):
    sql = '''SELECT matches.home_team_id, matches.away_team_id, match_results.match_id, match_results.winning_team_id, match_results.home_team_score, match_results.away_team_score, match_results.id FROM matches
        INNER JOIN match_results
        ON match_results.match_id = matches.id
        WHERE home_team_id = %s or away_team_id = %s'''
    values = [team.id, team.id]
    results = run_sql(sql, values)

    for result in results:
        match_result = MatchResult()

    # all_match_results = select_all()
    

    # matches_played = []
    # for match_result in all_match_results:
    #     match_has_been_played = False
    #     for match_result in all_match_results:
    #         if (match_result.match.id == match.id) :
    #             match_has_been_played = True
    #     if not match_has_been_played:
    #         matches_not_played.append(match)
    # return matches_not_played


def select_match_played():
    # sql = "SELECT * FROM matches WHERE home_team_id = %s OR away_team_id = %s"
    # values = [team.id, team.id]
    # result = run_sql(sql, values)
    matches_played = select_pending()
    matches_played_for_team = []

    for match_played in matches_played:
        if match_played.home_team.id == match.id:
            matches_played_for_team.append(match_played)
        elif match_played.away_team.id == match.id:
            matches_played_for_team.append(match_played)
    
    return matches_played_for_team

