DROP TABLE IF EXISTS match_results;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS teams;


CREATE TABLE teams(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE matches(
    id SERIAL PRIMARY KEY,
    home_team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    away_team_id INT REFERENCES teams(id) ON DELETE CASCADE
);

CREATE TABLE match_results(
    id SERIAL PRIMARY KEY,
    home_team_score INT,
    away_team_score INT,
    match_id INT NOT NULL REFERENCES matches(id) ON DELETE CASCADE,
    winning_team_id INT NOT NULL REFERENCES teams(id) ON DELETE CASCADE
);
