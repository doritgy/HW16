import check_song

def find_song_name(country_name:str, my_year:int) -> str:
    print("check_song_name", check_song.check_my_song(country_name, my_year))
    return check_song.check_my_song(country_name, my_year)


def find_all_songs():
    import sql_lib
    cursor = sql_lib.connect('dbaicourse.db')
    cursor.execute("""
       SELECT song_name, country , year from eurovision_winners eu
    """)
    columns = cursor.fetchall()
    result = [tuple(row) for row in columns]
    return result

def  test_details(country_name:str, my_year:str) -> str|None:
    """
    This function performs the job in sql, after getting the answer directly
    :param country_name:
    :param my_year:
    :return: string
    """

    if country_name.isdigit():
        print("you entered a wrong country, please try again")
        return None
    if my_year.isalpha():
        print("you typed a wrong year, please try again")
        return None
    else:
        my_year = int(my_year)
        country_name = country_name.upper()
        result = find_song_name(country_name, my_year)
        if result:
            return result
        else:
            return None

def test_details_cursor(country_name:str, my_year:str) -> str|None:
    """
    This function performs the job in python, after getting all records from sql
    :param country_name:
    :param my_year:
    :return: string
    """
    if country_name.isdigit():
        print("you entered a wrong country, please try again")
        return None
    if my_year.isalpha():
        print("you typed a wrong year, please try again")
        return None
    else:
        my_year = int(my_year)
        country_name = country_name.upper()
        result = find_all_songs()
        if result:
            my_song = tuple(filter(lambda t: t[1] == country_name and t[2] == my_year,
                                   (map(lambda t: (t[0], t[1].upper(), t[2]), result))))

            if my_song:
                songs = my_song[0]
                song = songs[0]
                return song
            else:
                return str("wrong")
        else:
            return str("wrong")


def main():
    while True:
        country_name:str = input("please type the country name")
        my_year:any = input("please type the year you request")

        if test_details(country_name, my_year) and test_details_cursor(country_name, my_year):
            print(test_details(country_name, my_year))
            print(test_details_cursor(country_name, my_year))
            break
        else:
            continue



if __name__ == "__main__":
    main()





