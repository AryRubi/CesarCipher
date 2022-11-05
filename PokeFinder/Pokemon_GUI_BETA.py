import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from Pokedex import Create_Pokedex
import sqlite3


def my_search_one(type1, stat, order, number):
            con = sqlite3.connect("pokedex.sqlite")
            cur = con.cursor()
            cur.execute('''SELECT ID, Name, %s, Type_1, Type_2 FROM Pokemon WHERE (Type_1 = ? OR Type_2 = ?) AND %s >= ? ORDER BY %s %s LIMIT 10''' % (stat,stat, stat, order) , (type1, type1, number,))
            con.commit()

            Results_Window = Toplevel(bg="light green")
            Results_Window.title("Results")
            Results_Window.geometry("500x450")

            for i in cur.fetchall():
                x = ("ID:",i[0],"Name:" , i[1], stat, ":", i[2], "Types:" , i[3],"/", i[4] )
                pokemons = tk.Label(Results_Window, background= "light green",
                text = x, font= ("arial", 14, "bold"))
                pokemons.pack()
                space= tk.Label(Results_Window, background= "light green",
                text = " ")
                space.pack()



def my_search_only_one(type1, stat, order, number):
            con = sqlite3.connect("pokedex.sqlite")
            cur = con.cursor()
            cur.execute('''SELECT ID, Name, %s, Type_1, Type_2 FROM Pokemon WHERE (Type_1 = ? AND Type_2 IS NULL) AND %s >= ? ORDER BY %s %s LIMIT 10''' % (stat,stat, stat, order) , (type1, number,))
            con.commit()

            Results_Window = Toplevel(bg="light green")
            Results_Window.title("Results")
            Results_Window.geometry("500x450")

            for i in cur.fetchall():
                y = ("ID:",i[0],"Name:" , i[1], stat, ":", i[2], "Types:" , i[3],"/", i[4] )
                pokemons = tk.Label(Results_Window, background= "light green",
                text = y, font= ("arial", 14, "bold"))
                pokemons.pack()
                space= tk.Label(Results_Window, background= "light green",
                text = " ")
                space.pack()

def my_search_two(type1, type2, stat, order, number):
    con = sqlite3.connect("pokedex.sqlite")
    cur = con.cursor()
    cur.execute('''SELECT ID, Name, %s, Type_1, Type_2 FROM Pokemon WHERE (Type_1 = ? AND Type_2 = ?) OR (Type_1 = ? AND Type_2 = ?) AND %s >= ? ORDER BY %s %s LIMIT 10''' % (stat, stat, stat, order) , (type1, type2, type2, type1,number,))
    con.commit()

    Results_Window = Toplevel(bg="light green")
    Results_Window.title("Results")
    Results_Window.geometry("500x450")

    for i in cur.fetchall():
        z = ("ID:",i[0],"Name:" , i[1], stat, ":", i[2], "Types:" , i[3],"/", i[4] )
        pokemons = tk.Label(Results_Window, background= "light green",
            text = z, font= ("arial", 14, "bold"))
        pokemons.pack()
        space= tk.Label(Results_Window, background= "light green",
            text = " ")
        space.pack()
                



class APP():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("350x530")
        self.root.title("PokeFinder")
        self.mainframe = tk.Frame(self.root, background= "light blue")
        self.mainframe.pack(fill= "both" , expand = True)




        self.text_1 = tk.Label(self.mainframe, bg = "light blue" , text = "Choose a pokemon first type:", font = ("Arial" , 20))
        self.text_1.grid(row = 0, column = 0, sticky="NWS", pady=10)
        
        pokemon_types_1= sorted(["Normal" , "Fire" , "Water", "Grass", "Electric" ,"Ice" , "Fighting" , "Poison" ,"Ground" ,"Flying" ,"Psychic" ,"Bug" ,"Rock" ,"Ghost" ,"Dark" ,"Dragon" ,"Steel" ,"Fairy"])
        self.set_type_1 = ttk.Combobox(self.mainframe , state="readonly", values = pokemon_types_1)
        self.set_type_1.grid(row=2, column=0, sticky="NWS", pady=10)
        self.set_type_1.current(12)




        self.text_2 = tk.Label(self.mainframe, bg="light blue" , text = "Choose a pokemon second type:", font = ("Arial" , 20))
        self.text_2.grid(row = 3, column = 0, sticky="NWS", pady=10)

        pokemon_types_2= ["Any" , "NONE"] + sorted(["Normal" , "Fire" , "Water", "Grass", "Electric" ,"Ice" , "Fighting" , "Poison" ,"Ground" ,"Flying" ,"Psychic" ,"Bug" ,"Rock" ,"Ghost" ,"Dark" ,"Dragon" ,"Steel" ,"Fairy"])
        self.set_type_2 = ttk.Combobox(self.mainframe, state="readonly", values = pokemon_types_2)
        self.set_type_2.current(0)
        self.set_type_2.grid(row=4, column=0, sticky="NWS", pady=10)




        self.text_3 = tk.Label(self.mainframe, bg="light blue" , text = "Choose a pokemon stat:", font = ("Arial" , 20))
        self.text_3.grid(row = 5, column = 0, sticky="NWS", pady=10)

        pokemon_stats= ["HP", "Attack", "Defense", "Sp_Attack", "Sp_Defense", "Speed"]
        self.set_stat = ttk.Combobox(self.mainframe, state="readonly", values = pokemon_stats)
        self.set_stat.grid(row=6, column=0, sticky="NWS", pady=10)
        self.set_stat.current(0)




        self.text_4 = tk.Label(self.mainframe, bg="light blue" , text = "Order from:", font = ("Arial" , 20))
        self.text_4.grid(row = 7, column = 0, sticky="NWS", pady=10)

        order_by= ["Highest to lowest", "Lowest to highest"]
        self.set_order = ttk.Combobox(self.mainframe, state="readonly", values = order_by)
        self.set_order.grid(row=8, column=0, sticky="NWS", pady=10)
        self.set_order.current(0)


        self.text_5 = tk.Label(self.mainframe, bg="light blue" , text = "Min stat:", font = ("Arial" , 20))
        self.text_5.grid(row = 9, column = 0, sticky="NWS", pady=10)
        self.set_num = ttk.Entry(self.mainframe)
        self.set_num.grid(row= 10, column= 0, sticky="NWS", pady=10)


        set_search_button = ttk.Button(self.mainframe, text = "Search", command= self.types)
        set_search_button.grid(row = 11 , column = 0, pady = 10)




        self.root.mainloop()
        return


    
    def types(self):
        p_type_1 = self.set_type_1.get().lower()
        p_type_2 = self.set_type_2.get().lower()
        p_stat = self.set_stat.get().lower()
        p_order = self.set_order.get()
        p_num = self.set_num.get()

        try:
            p_num = int(p_num)
            integer = True
        except:
            Error_Window = Toplevel(background = "light pink")
            Error_Window.title("Min/Max stat ERROR")
            Error_Window.geometry("500x100")
            space= tk.Label(Error_Window, background= "light pink",
                text = " ")
            space.pack()
            mssg_error = tk.Label(Error_Window, text= "Please only write integers", background= "light pink" ,font=("arial", 40, "bold"))
            mssg_error.pack()
            integer = False

        if integer:
            if p_order == "Highest to lowest":
                order_type = "DESC"
            else:
                order_type = "ASC"

            if p_type_2 == "none":
                my_search_only_one(p_type_1,p_stat, order_type, p_num)
            elif p_type_2 == "any":
                my_search_one(p_type_1,p_stat, order_type, p_num)
            else:
                my_search_two(p_type_1,p_type_2, p_stat, order_type, p_num)
        

        




        

Create_Pokedex()
APP()
