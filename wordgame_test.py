import unittest
from wordgame import *

class MyTestCase(unittest.TestCase):
    wordgame = WordGame() 

    def setUp(self):
        """Set up the WordGame instance for testing."""
        self.wordgame = WordGame(rounds=10, countdown_time=15)
    
    def test_score(self):
        self.assertEqual(self.wordgame.calculate_score("A"),1) 
        self.assertEqual(self.wordgame.calculate_score("BBB"),9)
        self.assertTrue(self.wordgame.calculate_score("APPLE"),3)
        self.assertFalse(self.wordgame.calculate_score("1123"),3)
        self.assertFalse(self.wordgame.calculate_score("#%$^&"),3)
        self.assertFalse(self.wordgame.calculate_score("#1315%$^&"),3)
        
if __name__ == '__main__':
    unittest.main()
