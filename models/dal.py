"""
DAL : Data Access Layer
This module contains code to retrieve and store data (data manipulation)
"""

import json


def load_db():
    file_path = "D:\\Python Lecture\\Class note\\pythonProject_Mini flask\\models\\flashcard_db.json"
    with open(file_path, "r") as foo:
        return json.load(foo)

db = load_db()