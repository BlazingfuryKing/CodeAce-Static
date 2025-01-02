import sqlite3

conn = sqlite3.connect("club.db") 
f1 = open('DATA.txt')
comps = {}
members = {}
scores = {}

for item in f1:
    lst = item.strip().split(',')
    if lst[0] not in members:
        members[lst[0]] = [lst[0], lst[1], lst[2]]
    if lst[4] not in comps:
        comps[lst[4]] = [lst[4], lst[3]]
    if (lst[4],lst[0]) not in scores:
        scores[(lst[4],lst[0]) ] = [lst[4],lst[0],lst[5]]
f1.close()

for item in members:
    conn.execute("INSERT INTO Members VALUES (?,?,?)", members[item])

for item in comps:
    conn.execute("INSERT INTO Competitions VALUES (?,?)", comps[item])

for item in scores:
    conn.execute("INSERT INTO Scores VALUES (?,?,?)", scores[item])

conn.commit()
conn.close()
