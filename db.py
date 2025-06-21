import sqlite3

def create_connection():
    return sqlite3.connect("summaries.db", check_same_thread=False)


def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS summaries (
            username TEXT,
            input_text TEXT,
            summary TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_summary(username, input_text, summary):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO summaries (username, input_text, summary) VALUES (?, ?, ?)", 
                   (username, input_text, summary))
    conn.commit()
    conn.close()


def get_user_summaries(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT input_text, summary FROM summaries WHERE username = ?", (username,))
    results = cursor.fetchall()
    conn.close()
    return results


