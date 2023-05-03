from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.match import Match
import repositories.match_repository as match_repository
import repositories.team_repository as team_repository

matches_blueprint = Blueprint("matches", __name__)




# create new match
@matches_blueprint.route('/matches', methods=['POST']) 
def add_matches():
    home_team_id = request.form['home_team_id']
    away_team_id = request.form['away_team_id']
    # print(home_team_id)

    home_team = team_repository.select(home_team_id)
    away_team = team_repository.select(away_team_id)

    new_match = Match(home_team, away_team)
    match_repository.save(new_match)
    return redirect('/matches')

    # home_team = team_repository.select(home_team_id)
    # away_team = team_repository.select(away_team_id)
    # # name = request.form['add_match']
    # new_match=Match(home_team, away_team)
    # match_repository.save(new_match)
    # return redirect('/matches')


# show all 
@matches_blueprint.route("/matches")
def matches():
    pending_matches = match_repository.select_pending()
    teams = team_repository.select_all()
    return render_template("matches/index.jinja", matches = pending_matches, teams = teams)

# select by id
@matches_blueprint.route("/matches/<id>")
def show(id):
    match = match_repository.select(id)
    teams = team_repository.matches_for_team(match)
    return render_template("matches/show.jinja", match=match)


