import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    instagram_username TEXT,
                    food_rating INTEGER,
                    cleanliness_rating INTEGER,
                    extra_comments TEXT
                )
            """)
            conn.commit()

    def save_survey(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute('''INSERT INTO reviews (name, instagram_username, food_rating, cleanliness_rating, extra_comments)
            VALUES (?, ?, ?, ?, ?)''',
            (data['name'], data['instagram_username'],
             data['food_rating'], data['cleanliness_rating'], data['extra_comments'])
            )
            conn.commit()