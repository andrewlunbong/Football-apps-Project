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