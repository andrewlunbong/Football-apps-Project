from models.match import Match
from models.team import Team
from models.result import Result

import repositories.match_repository as match_repository
import repositories.team_repository as team_repository
import repositories.result_repository as result_repository

result_repository.delete_all()
team_repository.delete_all()
match_repository.delete_all()

team1 = Team('Arsenal')
team_repository.save(team1)

team2 = Team('Man City')
team_repository.save(team2)

team3 = Team('Man United')
team_repository.save(team3)

team4 = Team('Newcastle United')
team_repository.save(team4)

team5 = Team('Tottenham')
team_repository.save(team5)

match1 = Match('team2', 'team1')
location_repository.save(location1)

location2 = Location('The Prancing Pony', 'Tavern')
location_repository.save(location2)

visit1 = Visit(user1, location1, '0 stars, far too hot')
visit_repository.save(visit1)

visit2 = Visit(user3, location1, '5 stars, would visit again if I could')
visit_repository.save(visit2)

visit3 = Visit(user1, location2, '4 stars, plenty of beer available')
visit_repository.save(visit3)

visit4 = Visit(user2, location2, '3 stars, too crowded, could not find my wizard friend')
visit_repository.save(visit4)