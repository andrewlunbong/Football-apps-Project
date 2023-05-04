import unittest
from models.team import Team
from models.match import Match


class TestTeam(unittest.TestCase):

    def setUp(self):
        
        self.team1 = Team("Arsenal")
        self.team2 = Team("Man City")
        
    
    
    def test_team_has_name(self):
        self.assertEqual("Arsenal", self.team1.name)

    def test_team_two_has_name(self):
        self.assertEqual("Man City", self.team2.name)
    
    
    