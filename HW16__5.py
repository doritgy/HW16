def find_and_change_genre():
    """
    The function finds the specific record and changed it if the new genre is different
    gets no arguments
    :return: None
    """
    import sql_lib
    cursor = sql_lib.connect('dbaicourse.db')
    while True:
        details = get_details()
        my_country, my_year, my_genre = details
        cursor.execute("""
              SELECT eu.year, sd.genre from eurovision_winners eu
              join song_details sd on eu.year = sd.year
              WHERE eu.year = ? AND eu.country LIKE ?
        """, (my_year, f'%{my_country.upper()}%'))
        columns = cursor.fetchall()
        result = [tuple(row) for row in columns]
        if result:
           my_genre_exist = result[0][1]
           if my_genre_exist == my_genre:
               print(f"f my_genre_exist {my_genre_exist} my_genre {my_genre}")
               print("type a different genre")
               continue
           else:
               try:
                   cursor.execute("UPDATE song_details SET genre = ? WHERE year = ?",
                                  (my_genre, my_year))
                   cursor.connection.commit()
                   print("after change:", check_change(my_genre, my_year, my_country))
                   if check_change(my_genre, my_year, my_country):
                       cursor.close()
                       break
                   else:
                       print("something went wrong")
                       continue

               except Exception as e:
                    print("something happened   " + str(e))
                    continue
        else:
            print("wrong")
            cursor.close()
            break

def check_change(my_genre:str, my_year:str, my_country:str) -> bool:
    import sql_lib
    cursor = sql_lib.connect('dbaicourse.db')

    cursor.execute("""
              SELECT sd.genre from eurovision_winners eu
              join song_details sd on eu.year = sd.year
              WHERE eu.year = ? AND eu.country LIKE ?
        """, (my_year, f'%{my_country.upper()}%'))
    columns = cursor.fetchall()
    result = [tuple(row) for row in columns]
    if result:
        my_genre_exist = result[0][0]
        print(my_genre_exist)
        if my_genre_exist == my_genre:
            print("update successful")
            return True
        else:
            return False


def get_details() -> list[str]:
    while True:
        country_name = input("enter country name")
        if country_name.isdigit():
            print("not legal try again")
            continue
        year = input("enter a year")
        if year.isalpha():
            print("not legal try again")
            continue
        genre = input("please type the genre to chang")
        if genre.isdigit():
            print("not legal try again")
            continue

        return [country_name, year, genre]

def main():
    find_and_change_genre()

if __name__ == "__main__":
    main()
