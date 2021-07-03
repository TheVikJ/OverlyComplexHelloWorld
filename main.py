# Calling the Free Dictionary API and getting 
# values from a Database, just to say "hello, world"

import sqlite3
import requests
import json

def letters(input):
    valids = []
    for character in input:
        if character.isalpha():
            valids.append(character)
    return ''.join(valids)

connection = sqlite3.connect("myTable.db")

crsr = connection.cursor()

if input('Set up again? (y/n) ') == 'y': # Type y for setting it up
    cmd = '''CREATE TABLE world (word nvarchar(10) PRIMARY KEY NULL)'''
    crsr.execute(cmd)

cmd2 = '''INSERT INTO world VALUES ('world')'''
crsr.execute(cmd2)

crsr.execute('''SELECT * FROM world''')
world = crsr.fetchall()

url = 'https://api.dictionaryapi.dev/api/v2/entries/en_US/hello'

response = json.loads(requests.get(url).text)

print(response[0]['word'] + ", " + letters(str(world)))
