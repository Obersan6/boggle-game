from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

class HomePageTest(TestCase):
    def test_homepage(self):
        with app.test_client() as client:
            # Access the homepage
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn('board', session) # CHECK THIS WITH MENTOR
            
            




                                               