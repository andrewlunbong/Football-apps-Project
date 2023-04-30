from flask import Flask, render_template

from controllers.match_controller import match_blueprint
from controllers.team_controller import team_blueprint
from controllers.result_controller import result_blueprint

app = Flask(__name__)

app.register_blueprint(match_blueprint)
app.register_blueprint(team_blueprint)
app.register_blueprint(result_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)