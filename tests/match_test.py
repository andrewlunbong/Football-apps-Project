import unittest
from models.match import Match

class TestMatch(unittest.TestCase):

    def setUp(self):
        
        self.match1 = Match("Arsenal", "Chelsea")
        self.match2 = Match("Man City", "Real Madrid")
        
    
    
    def test_away_team_name_in_match_one(self):
        self.assertEqual("Chelsea", self.match1.away_team)

    def test_home_team_has_name_in_match_two(self):
        self.assertEqual("Man City", self.match2.home_team)