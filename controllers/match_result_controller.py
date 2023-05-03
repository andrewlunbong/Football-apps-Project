from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.match_result import MatchResult
import repositories.match_result_repository as match_result_repository
import repositories.team_repository as team_repository
import repositories.match_repository as match_repository

match_results_blueprint = Blueprint("match_results", __name__)


@match_results_blueprint.route("/match-results")
def match_results():
    match_results = match_result_repository.select_all() 
    return render_template("match-results/index.jinja", match_results = match_results)

# NEW
# GET '/visits/new'
# @visits_blueprint.route("/visits/new", methods=['GET'])
# def new_task():
#     users = user_repository.select_all()
#     locations = location_repository.select_all()
#     return render_template("visits/new.html", users = users, locations = locations)

# # CREATE
# # POST '/visits'
# @match_results_blueprint.route("/results",  methods=['POST'])
# def create_task():
#     user_id = request.form['user_id']
#     location_id = request.form['location_id']
#     review = request.form['review']
#     user = user_repository.select(user_id)
#     location = location_repository.select(location_id)
#     visit = Visit(user, location, review)
#     visit_repository.save(visit)
#     return redirect('/visits')


# # DELETE
# # DELETE '/visits/<id>'
# @visits_blueprint.route("/visits/<id>/delete", methods=['POST'])
# def delete_task(id):
#     visit_repository.delete(id)
#     return redirect('/visits')