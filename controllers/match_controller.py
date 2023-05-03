from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.match import Match
import repositories.match_repository as match_repository
import repositories.team_repository as team_repository

matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/")
def home():
    return render_template("/index.jinja")


@matches_blueprint.route("/matches")
def matches():
    pending_matches = match_repository.select_pending()
    return render_template("matches/index.jinja", matches = pending_matches)

@matches_blueprint.route("/matches/<id>")
def show(id):
    match = match_repository.select(id)
    teams = team_repository.matches_for_team(match)
    return render_template("matches/show.jinja", match=match)

@matches_blueprint.route('/matches', methods=['POST']) 
def add_matches():
    name = request.form['add_match']
    new_match=Match(home_team, away_team)
    match_repository.save(new_match)
    return redirect('/matches')

