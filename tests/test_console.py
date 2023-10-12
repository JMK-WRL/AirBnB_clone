#!/usr/bin/python3
"""Module that tests the console."""


import unittest
import sys
import io
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User

class TestConsole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Redirect stdout to capture console output
        cls.original_stdout = sys.stdout
        sys.stdout = io.StringIO()

    @classmethod
    def tearDownClass(cls):
        # Reset stdout
        sys.stdout = cls.original_stdout

    def setUp(self):
        # Create an instance of HBNBCommand for testing
        self.console = HBNBCommand()
        self.console.use_rawinput = False

    def tearDown(self):
        # Reset the captured console output
        sys.stdout.seek(0)
        sys.stdout.truncate()

    def test_create_and_show(self):
        # Create a new user
        self.console.onecmd("create User")
        captured_output = sys.stdout.getvalue()
        user_id = captured_output.strip()

        # Check if a user was created
        self.assertTrue(user_id != "")
        
        # Show the created user
        self.console.onecmd(f"show User {user_id}")
        captured_output = sys.stdout.getvalue()

        # Check if the user info is in the output
        self.assertIn(user_id, captured_output)
        
    def test_create_and_destroy(self):
        # Create a new user
        self.console.onecmd("create User")
        captured_output = sys.stdout.getvalue()
        user_id = captured_output.strip()

        # Check if a user was created
        self.assertTrue(user_id != "")
        
        # Destroy the created user
        self.console.onecmd(f"destroy User {user_id}")
        captured_output = sys.stdout.getvalue()
        
        # Check if success message is in the output
        self.assertIn("successfully deleted", captured_output)
        
    def test_create_and_all(self):
        # Create a new user
        self.console.onecmd("create User")
        captured_output = sys.stdout.getvalue()
        user_id = captured_output.strip()

        # Check if a user was created
        self.assertTrue(user_id != "")
        
        # Show all users
        self.console.onecmd("all User")
        captured_output = sys.stdout.getvalue()
        
        # Check if user_id is in the output
        self.assertIn(user_id, captured_output)
        
    def test_create_and_update(self):
        # Create a new user
        self.console.onecmd("create User")
        captured_output = sys.stdout.getvalue()
        user_id = captured_output.strip()

        # Check if a user was created
        self.assertTrue(user_id != "")
        
        # Update the user's email
        self.console.onecmd(f"update User {user_id} email 'new_email@example.com'")
        captured_output = sys.stdout.getvalue()

        # Check if success message is in the output
        self.assertIn("updated", captured_output)
        
        # Show the updated user
        self.console.onecmd(f"show User {user_id}")
        captured_output = sys.stdout.getvalue()

        # Check if the updated email is in the output
        self.assertIn("new_email@example.com", captured_output)

if __name__ == '__main__':
    unittest.main()