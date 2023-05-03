from flask import Flask, render_template

from controllers.match_controller import matches_blueprint
from controllers.team_controller import teams_blueprint
from controllers.match_result_controller import match_results_blueprint

app = Flask(__name__)

app.register_blueprint(matches_blueprint)
app.register_blueprint(teams_blueprint)
app.register_blueprint(match_results_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)