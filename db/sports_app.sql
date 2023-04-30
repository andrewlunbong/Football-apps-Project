DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS matches;


CREATE TABLE teams(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE matches(
    id SERIAL PRIMARY KEY,
    Home_team VARCHAR(255),
    Away_team VARCHAR(255),
    Winning_team VARCHAR(255)
);
