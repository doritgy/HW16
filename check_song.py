import sql_lib
import sqlite3
def check_my_song(country_name:str, my_year:int) -> str:

    cursor = sql_lib.connect('dbaicourse.db')
    #print(country_name, my_year)
    # Act
    result = cursor.execute('''
        SELECT song_name 
        FROM eurovision_winners eu
        WHERE eu.year = ? AND eu.country LIKE ?
    ''', (my_year, f'%{country_name.upper()}%'))
    columns = cursor.fetchall()
    result = [tuple(row) for row in columns]
    if result:
        results = result[0]
        result = results[0]
    if result:
        return  str(result)
    else:
            return "wrong"






