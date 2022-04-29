import sqlite3

connect = sqlite3.connect('Mydatas.db')

cursor = connect.cursor()

quest  = input('Nima haqida ma`lumot olmoqchisiz?').lower()

# human data
cursor.execute("""
CREATE TABLE IF NOT EXISTS shopping(
   name TEXT,
   last_name TEXT,
   age INTEGER
   )
""")

cursor.execute("""
INSERT INTO shopping VALUES
('JORABEK','SODIQOV',16),
('DILSHOD','TUROPOV',80),
('JAMSHID','SALOMOV',10)
""")

cursor.execute("SELECT * FROM shopping")
result = cursor.fetchall()
# end human

# garden data
cursor.execute("""
CREATE TABLE IF NOT EXISTS garden(
   name TEXT,
   last_name TEXT,
   age INTEGER
   )
""")

cursor.execute("""
INSERT INTO garden VALUES
('Gulzorlar','soni',5),
('Gullar','soni',80),
('Ishchi','soni',20)
""")

cursor.execute("SELECT * FROM garden")
result2 = cursor.fetchall()
#end garden

# librery data
cursor.execute("""
CREATE TABLE IF NOT EXISTS library(
   name TEXT,
   last_name TEXT,
   age INTEGER
   )
""")

cursor.execute("""
INSERT INTO libarary VALUES
('Kutubxonalar','soni',10),
('Kitoblar','soni',500),
('Ishchilar','soni',40)
""")

cursor.execute("SELECT * FROM library")
result3 = cursor.fetchall()
# end library

# rasm data
cursor.execute("""
CREATE TABLE IF NOT EXISTS rasm(
   name TEXT,
   last_name TEXT,
   age INTEGER
   )
""")

cursor.execute("""
INSERT INTO rasm VALUES
('Rassomlar','soni',10),
('Suratlar','soni',60),
('Xonalar','soni',4)
""")

cursor.execute("SELECT * FROM rasm")
result4 = cursor.fetchall()
#  end rasm

# kompyuter data
cursor.execute("""
CREATE TABLE IF NOT EXISTS komp(
   name TEXT,
   last_name TEXT,
   age INTEGER
   )
""")

cursor.execute("""
INSERT INTO komp VALUES
('Kompyuterlar','soni',37),
('It center','soni',2),
('o`quvchilar','soni',85)
""")

cursor.execute("SELECT * FROM komp")
result5 = cursor.fetchall()
#  end kompyuter

if quest=="human":
    print(result)

elif quest=="garden":
    print(result2)

elif quest=="library":
    print(result3)

elif quest=="rasm":
    print(result4)

elif quest=="kompyuter":
    print(result5)