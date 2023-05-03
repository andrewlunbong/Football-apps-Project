from db.run_sql import run_sql
from models.match import Match
from models.team import Team

def save(team):
    sql = "INSERT INTO teams( name ) VALUES ( %s ) RETURNING id"
    values = [team.name]
    results = run_sql( sql, values )
    team.id = results[0]['id']
    return team


def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)
    for row in results:
        team = Team(row['name'], row['id'])
        teams.append(team)
    return teams


def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        team = Team(result['name'], result['id'] )
    return team


def teams_for_match(match):
    teams = []

    sql = "SELECT teams.* FROM teams INNER JOIN match_results ON match_result.team_id = teams.id WHERE match_id = %s"
    values = [match.id]
    results = run_sql(sql, values)

    for row in results:
        team = Team(row['name'], row['id'])
        teams.append(team)

    return teams

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def update(team):
    sql = "UPDATE teams SET name = %s WHERE id = %s"
    values = [team.name, team.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)