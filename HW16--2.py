import sql_lib
import sqlite3
def ten_years_songs():
    """
    The function prints nicely all details of winners from last 10 years
    gets no arguments
    :return: None
    """
    # Arrange
    print("aranging")
    sql_lib.connect('dbaicourse.db')

    # Act
    #print("acting")
    result = sql_lib.run_query_select('''
        SELECT year, country, winner, host_country, song_name from eurovision_winners
        where year >= (2024 - 10)
        order by year desc
    ''')
    print("year        ","country         ","winner          ","         host_country            ", "             song_name)")
    print("--------------------------------------------------------------------------------------------------------------")
    print()
    for row in result:
        year, country, winner, host_country, song_name = row
        #print(row)

        print(f" {year:<11} {country:<17} {winner:<27} {host_country:<37} {song_name:<47} ")

def main():
    ten_years_songs()

if __name__ == "__main__":
    main()
