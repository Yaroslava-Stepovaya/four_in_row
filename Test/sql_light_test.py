import sqlite3

con = sqlite3.connect('q_table.db')
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS states(col0 real,col1 real, col2 real,col3 real,col4 real, col5 real, col6 real, id text PRIMARY KEY)''')
cursor.execute("INSERT INTO states VALUES (0,132,0,-0.25,0,0,0,'15') ON CONFLICT(id) DO UPDATE SET col0=excluded.col0,col1=excluded.col1,col2=excluded.col2,col3=excluded.col3,col4=excluded.col4,col5=excluded.col5,col6=excluded.col6; ")
con.commit()
con.close()