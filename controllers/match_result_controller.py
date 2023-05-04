from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.match_result import MatchResult
import repositories.match_result_repository as match_result_repository
import repositories.team_repository as team_repository
import repositories.match_repository as match_repository

match_results_blueprint = Blueprint("match_results", __name__)

#show all result
@match_results_blueprint.route("/match-results")
def match_results():
    match_results = match_result_repository.select_all() 
    return render_template("match-results/index.jinja", match_results = match_results)

