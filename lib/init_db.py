import sqlite3

def execute_sql_file(filename):
    with open(filename, 'r') as sql_file:
        sql_script = sql_file.read()
        
    conn = sqlite3.connect('development.db')
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    execute_sql_file('lib/sql/__init__.sql')