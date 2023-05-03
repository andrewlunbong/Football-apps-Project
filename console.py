from models.match import Match
from models.team import Team
from models.match_result import MatchResult

import repositories.match_repository as match_repository
import repositories.team_repository as team_repository
import repositories.match_result_repository as match_result_repository

match_result_repository.delete_all()
match_repository.delete_all()
team_repository.delete_all()

team1 = Team('Arsenal')
team_repository.save(team1)

team2 = Team('Man City')
team_repository.save(team2)

team3 = Team('Man United')
team_repository.save(team3)

team4 = Team('Newcastle United')
team_repository.save(team4)

team_list = [team1, team2, team3, team4]


match1 = Match(team1, team2)
match_repository.save(match1)

match2 = Match(team3, team4)
match_repository.save(match2)

match3 = Match(team1, team4)
match_repository.save(match3)

match4 = Match(team3, team2)
match_repository.save(match4)

match5 = Match(team1, team3)
match_repository.save(match5)

match6 = Match(team2, team4)
match_repository.save(match6)

match7 = Match(team2, team1)
match_repository.save(match7)

match8 = Match(team4, team3)
match_repository.save(match8)

match9 = Match(team4, team1)
match_repository.save(match9)

match10 = Match(team2, team3)
match_repository.save(match10)

match11 = Match(team3, team1)
match_repository.save(match11)

match12 = Match(team4, team2)
match_repository.save(match12)


match_result1 = MatchResult(1, 3, match1, team2)
match_result_repository.save(match_result1)

match_result2 = MatchResult(2, 3, match2, team4)
match_result_repository.save(match_result2)

match_result3 = MatchResult(2, 1, match3, team1)
match_result_repository.save(match_result3)

match_result4 = MatchResult(2, 0, match4, team3)
match_result_repository.save(match_result4)

match_result5 = MatchResult(1, 2, match5, team3)
match_result_repository.save(match_result5)

match_result6 = MatchResult(3, 0, match6, team2)
match_result_repository.save(match_result6)

#  team_test = team_repository.select(1)
# team_test2 = Team("Arsenal worst team ever", 1)
# team_repository.update(team_test2)
# print(team_test2.name)

