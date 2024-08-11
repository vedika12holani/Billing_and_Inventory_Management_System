import sqlite3

def create_database():
    try:
        con = sqlite3.connect('ims.db')
        cur = con.cursor()

        # Create products table if it doesn't exist
        cur.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                supplier TEXT,
                name TEXT,
                price REAL,
                quantity INTEGER,
                status TEXT
            )
        ''')

        con.commit()
        print("Database and table created successfully!")

    except Exception as e:
        print(f"Error creating database: {e}")

    finally:
        if con:
            con.close()

# Call the function to create the database and table
if __name__ == "__main__":
    create_database()
