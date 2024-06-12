import sqlite3

# Create if not there
sqliteConnection = sqlite3.connect('sqlite/sql.db')
print(sqliteConnection.total_changes)

cursor = sqliteConnection.cursor()
cursor.execute("DROP TABLE if exists fish")

cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")

cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")
cursor.execute("INSERT INTO fish VALUES ('Nemo', 'angel', 3)")

rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print("All rows : ", rows)

target_fish_name = "Jamie"
rows = cursor.execute(
    "SELECT name, species, tank_number FROM fish WHERE name = ?",
    (target_fish_name,),
).fetchall()

print("Where clause : ", rows)

new_tank_number = 2
moved_fish_name = "Sammy"
cursor.execute(
    "UPDATE fish SET tank_number = ? WHERE name = ?",
    (new_tank_number, moved_fish_name)
)

rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print("New tank number for Sammy : ", rows)

released_fish_name = "Sammy"
cursor.execute(
    "DELETE FROM fish WHERE name = ?",
    (released_fish_name,)
)

rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print("Sammy released : ", rows)


cursor.close()
sqliteConnection.close()