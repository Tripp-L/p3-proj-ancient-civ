import sqlite3

def execute_sql_file(filename):
    with open(filename, 'r') as sql_file:
        sql_script = sql_file.read()
        
    conn = sqlite3.connect('development.db')
    cursor = conn.cursor()
    try:
        cursor.executescript(sql_script)
        conn.commit()
    except sqlite3.Error as e:
        print("Error executing SQL script:", e)
    finally:
        conn.close()    
    
if __name__ == "__main__":
    execute_sql_file('lib/sql/__init__.sql')