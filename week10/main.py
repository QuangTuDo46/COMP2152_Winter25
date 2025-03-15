import sqlite3
from contextlib import closing

try:
    with closing(sqlite3.connect('test.db')) as db_conn:
        db_conn.row_factory = sqlite3.Row
        with closing(db_conn.cursor()) as cursor:
            try:
                query_1 = "SELECT * FROM demo WHERE ID > 14"
                cursor.execute(query_1)
                rows = cursor.fetchall()
                for row in rows:
                    print(row["name"])
            except Exception as e:
                print(f"Error executing query: {e}")
            try:
                del_row = input("Enter the row ID threshold for deletion: ")
                query_2 = "DELETE FROM demo WHERE ID < ?"
                cursor.execute(query_2, (del_row, ))
                num_rows = cursor.rowcount
                print(f"{num_rows} rows deleted")
                db_conn.commit()
            except:
                print("Error deleting rows")
except sqlite3.Error as e:
    print(f"Database connection Error: {e}")