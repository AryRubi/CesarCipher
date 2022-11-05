import sqlite3
import json

con = sqlite3.connect("pokedex.sqlite")

cur = con.cursor()

cur.executescript('''

DROP TABLE IF EXISTS Pokemon;

CREATE TABLE Pokemon (
    ID INTEGER NOT NULL PRIMARY KEY UNIQUE,
    Name TEXT UNIQUE,
    Type_1 TEXT,
    Type_2 TEXT,
    HP INTEGER,
    Attack INTEGER,
    Defense INTEGER,
    Sp_Attack INTEGER,
    Sp_Defense INTEGER,
    Speed INTEGER
)

''')

#File opening
file = 'pokedex.json'

#File loading
str_data = open(file).read()
json_data = json.loads(str_data)

#{'id': 809, 
# 'name': {'english': 'Melmetal', 'japanese': 'メルメタル', 'chinese': '美录梅塔', 'french': ''}, 
# 'type': ['Steel'], 
# 'base': {'HP': 135, 'Attack': 143, 'Defense': 143, 'Sp. Attack': 80, 'Sp. Defense': 65, 'Speed': 34}}


#File reading and integration of data to SQL
for thing in json_data:

    #Creation of TABLE
    P_name = thing["name"]["english"]
    p_name = P_name.lower()

    if len(thing["type"]) > 1:
        P_type_1 = thing["type"][0]
        p_type_1 = P_type_1.lower()

        P_type_2 = thing["type"][1]
        p_type_2 = P_type_2.lower()
    else:
        P_type_1 = thing["type"][0]
        p_type_1 = P_type_1.lower()

        p_type_2 = None
    
    p_id = thing['id']

    p_hp = thing['base']['HP']
    p_attack = thing['base']['Attack']
    p_defense = thing['base']['Defense']
    p_spa = thing['base']['Sp. Attack']
    p_spd = thing['base']['Sp. Defense']
    p_speed = thing['base']['Speed']
    
    cur.execute('''INSERT OR IGNORE INTO Pokemon (ID, Name, Type_1, Type_2, HP, Attack, Defense, Sp_Attack, Sp_Defense, Speed) 
      VALUES ( ?, ? , ?, ?, ?, ?, ?, ?, ?, ? )''', ( p_id , p_name , p_type_1, p_type_2, p_hp , p_attack, p_defense, p_spa, p_spd, p_speed) )
    

    
    #Deletion of the p_types to restart the variable
    if len(thing["type"]) > 1: 
        del p_type_1
        del p_type_2
        
        
#Select the first pokemon type
print("Enter the pokemon type to search: ")
Type_1 = input("Type 1: ").lower()

#Select if you want a second type
print(" ")
print("Do you want to choose a second type? (Yes/No) : ")
answer = input().lower()
print(" ")

#Choose which stat the user is intrested
def search_stat():
    print("Which stat are you intrested on: ")
    print("1) HP")
    print("2) Attack")
    print("3) Defense")
    print("4) Special Attack") 
    print("5) Special Defense")
    print("6) Speed")
    print("Please enter the number of the stat you're intrested in: ")
    global answer_stat 
    answer_stat = int(input())
    
#Define which stat correspond with the number
def type_stat(x):
    if x == 1:
        global stat
        stat = "HP"
    elif x == 2:

        stat = "Attack"
    elif x == 3:

        stat = "Defense"
    elif x == 4:

        stat = "Sp_Attack"
    elif x == 5:

        stat = "Sp_Defense"
    elif x == 6:

        stat = "Speed"
    else: 

        stat = None

print(" ")
if answer == "yes":
    
    #Type
    Type_2 = input("Type 2: ").lower()
    print(" ")

    #Stats
    search_stat()
    type_stat(answer_stat)
    print(" ")
    print("Search by min", stat,  "of: ")
    stat_value = int(input())

    #query
    cur.execute('''SELECT ID, Name, %s, Type_1, Type_2 FROM Pokemon WHERE (Type_1 = ? AND Type_2 = ?) OR (Type_1 = ? AND Type_2 = ?) AND %s > ? ORDER BY {} DESC LIMIT 10'''.format(stat) % (stat, stat) , (Type_1, Type_2, Type_2, Type_1,  stat_value, ))
    con.commit()
    for i in cur.fetchall():
        print(" ")
        print("ID: " , i[0]," " , "Pokemon: " , i[1]," " , stat , ":" , i[2], " " , "Types: ", i[3], "/" , i[4])

elif answer == "no":
    #Type
    Type_2 = Type_1

    #Stats
    search_stat()
    type_stat(answer_stat)
    print(" ")
    print("Search by min", stat,  "of: ")
    stat_value = int(input())

    #query
    cur.execute('''SELECT ID, Name, %s, Type_1, Type_2 FROM Pokemon WHERE (Type_1 = ? OR Type_2 = ?) AND %s > ? ORDER BY {} DESC LIMIT 10'''.format(stat) % (stat, stat) , (Type_1, Type_2 , stat_value, ))
    con.commit()
    for i in cur.fetchall():
        print(" ")
        print("ID: " , i[0]," " , "Pokemon: " , i[1]," " , stat , ":" , i[2], " " , "Types: ", i[3], "/" , i[4])
else: 
    print("sorry but you need to write yes or no")
    HP = None


print(" ")
print("FINISHED!!")
