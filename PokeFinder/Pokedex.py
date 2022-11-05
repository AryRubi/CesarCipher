import sqlite3
import json


def Create_Pokedex():
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


    con.commit()

if __name__ == "__main__":
    Create_Pokedex()