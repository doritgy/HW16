import sqlite3
import sql_lib
import pytest
import HW16__3
def test_sql_eu():
    cursor = sql_lib.connect('dbaicourse.db')
    # Act
    cursor.execute("""
          SELECT count(*) from eurovision_winners eu
       """)
    columns = cursor.fetchall()
    result = [tuple(row) for row in columns]
    assert result == [(68,)]


def test_sql_sd():
    cursor = sql_lib.connect('dbaicourse.db')
    # Act
    cursor.execute("""
          SELECT count(*) from song_details sd
       """)
    columns = cursor.fetchall()
    result = [tuple(row) for row in columns]
    assert result == [(68,)]


def test_sql_country_year():
   import HW16__3
   actual = HW16__3.test_details("Israel", "1998")
   assert actual.upper() == "DIVA"

def test_sql_country_year_all():
    import HW16__3
    actual = HW16__3.test_details_cursor("Israel", "1998")

    assert actual.upper() == 'DIVA'

def test_sql_country_year_wrong():
   import HW16__3
   actual = HW16__3.test_details("Hawaii", "1998")
   if actual:
        assert actual.upper() == "WRONG"
   else:
        assert actual == None

def test_sql_country_year_all_wrong():
    import HW16__3
    actual = HW16__3.test_details_cursor("Hawaii", "1998")

    assert actual.upper() == 'WRONG'



