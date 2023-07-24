## Football Score and Result Management App

## Description
The Football Score and Result Management App is an interactive application designed to create and manage football scores and results. This app allows users to record and update football match scores, view match results, and manage team standings in a convenient and user-friendly way.

## Features
The app provides the following features:

Create and manage football match scores: Users can record and update football match scores for various teams.
View match results: Users can view the results of past football matches and see which team won or if there was a draw.
Manage team standings: The app calculates and displays the team standings based on match results.
User-friendly interface: The app provides an intuitive and easy-to-use interface for entering and managing football scores and results.

## Setup

Before running the app locally, ensure you have the following software installed:

1. psycopg2 - https://pypi.org/project/psycopg2/
2. python - https://docs.python-guide.org/starting/install3/osx/
3. flask - https://phoenixnap.com/kb/install-flask

## Getting Started

1. Open the terminal.
2. Create a folder by pasting: mkdir project_name (replace 'project_name' with your desired folder name).
3. Navigate to the folder by pasting: cd project_name.
4. Initiate the Git repository by pasting: git init.
5. Pull (or access) the files by pasting: git clone git@github.com:username/repo.git (replace 'username' and 'repo' with your GitHub username and repository name).
6. Install the necessary software mentioned above.
7. Create the database by pasting: createdb gym_manager (replace 'gym_manager' with your desired database name).
8. Generate the necessary tables by pasting: psql -d gym_manager -f db/gym_manager.sql.

## Running the App

1. To run the app, paste: flask run.
2. Access the app at http://localhost:5000.

## Troubleshooting

If you encounter any issues during setup or running the app, refer to the References section for useful resources.

## Folders & Files

The project contains the following folders and files:

- README.md
- .flaskenv (contains base settings for running Flask)
- app.py (contains the base settings for returning a web page)
- console.py (used for manual database manipulation)
- run_tests.py (used to run unittests)
- utest (contains testing grounds for Python classes)
- models (contains the Python classes: gym_class.py, gym_member.py, gym_room.py)
- db (contains database related files: gym_manager.sql, run_sql.py)
- controllers (contains files that handle receiving HTTP requests and responding with HTML templates)
- repositories (contains files that contain SQL functions related to respective tables)
- templates (used to store HTML (Jinja) templates which structure the view)
- static (used for holding CSS files, which will influence the view look)

## References

- Markdown guide: https://www.markdownguide.org/basic-syntax/
- psycopg2 installation: https://pypi.org/project/psycopg2/
- Python installation: https://docs.python-guide.org/starting/install3/osx/
- Flask installation: https://phoenixnap.com/kb/install-flask
- Week_2_day_3 unittest setup: [Link]
- Week_4_day_5 file/table setup: [Link]
- SQL date/time syntax: [Link]
