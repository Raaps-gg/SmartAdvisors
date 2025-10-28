import pandas as pd
import sqlite3
department = "CE"
db_path = "SmartAdvisors/data/classes.db"
    
db = sqlite3.connect(db_path)
cur = db.cursor()

cur.execute(f"SELECT * FROM ClassesFor{department}")
data = cur.fetchall()
print(data)
