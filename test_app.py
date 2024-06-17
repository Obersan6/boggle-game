import json
from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

class HomePageTest(TestCase):
    def setUp(self):
        """Set up the test client and app context"""
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'test_secret_key'

        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["T", "E", "S", "T", "T"],
                                 ["E", "S", "T", "T", "T"],
                                 ["S", "T", "T", "T", "T"],
                                 ["T", "T", "T", "T", "T"],
                                 ["T", "T", "T", "T", "T"]]
                sess['submitted_words'] = []

    def test_homepage(self):
        with self.client as client:
            # Ensure the session is empty before the request
            with client.session_transaction() as sess:
                sess.clear()
            
            # Access the homepage
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            
            # Ensure 'board' is in the HTML response and decode response.data to a string
            response_text = response.data.decode('utf-8')
            self.assertIn('board', response_text)

            # Check if the board is in the session 
            with client.session_transaction() as sess:
                self.assertIn('board', sess)
    
    def test_initialize_game(self):
        with self.client as client:
            # Access the homepage
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            
            # Check if 'numb_plays' and 'highest_score' are in the session
            with client.session_transaction() as sess:
                self.assertIn('numb_plays', sess)
                self.assertIn('highest_score', sess)
                self.assertEqual(sess['numb_plays'], 0)
                self.assertEqual(sess['highest_score'], 0)
    
    def test_update_stats(self):
        with self.client as client:
            with client.session_transaction() as sess:
                sess
