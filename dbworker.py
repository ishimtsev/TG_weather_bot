import config
import sqlite3


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(config.database)
        conn.row_factory = sqlite3.Row
    except Exception as e:
        print(e)
    return conn


def get_user_state(user_id):
    conn = create_connection()
    with conn:
        sql = "SELECT state FROM users WHERE id = ?"
        return str(conn.cursor().execute(sql, (user_id,)).fetchone()[0])


def set_user_state(user_id, state):
    conn = create_connection()
    with conn:
        sql = "UPDATE users SET state = ? WHERE id = ?"
        conn.cursor().execute(sql, (state, user_id))
        conn.commit()


def is_user_exist(user_id):
    conn = create_connection()
    with conn:
        sql = "SELECT count(*) FROM users WHERE id = ?"
        if str(conn.cursor().execute(sql, (user_id,)).fetchone()[0]) == '1':
            return True
        else:
            return False


def get_city(user_id):
    conn = create_connection()
    with conn:
        sql = "SELECT cityname, citykey FROM users WHERE id = ?"
        return conn.cursor().execute(sql, (user_id,)).fetchone()


def set_city(user_id, city_name, city_key):
    conn = create_connection()
    with conn:
        sql = "UPDATE users SET cityname = ? , citykey = ? WHERE id = ?"
        conn.cursor().execute(sql, (city_name, city_key, user_id))
        conn.commit()


def add_user(user_id):
    conn = create_connection()
    with conn:
        sql = "INSERT INTO users(id, state) VALUES(?, ?)"
        conn.cursor().execute(sql, (user_id, config.States.S_CITY_SEARCH.value))
        conn.commit()


def add_temp_results(user_id, results):
    conn = create_connection()
    with conn:
        sql = "INSERT INTO temp_results(user_id, city_number, city_name, city_key, full_str) VALUES(?, ?, ?, ?, ?)"
        for row in results:
            conn.cursor().execute(sql, (user_id, row.number, row.city_name, row.city_key, row.full_str))
        conn.commit()


def get_temp_results(user_id):
    conn = create_connection()
    with conn:
        sql = "SELECT city_number, city_name, city_key FROM temp_results WHERE user_id = ? ORDER BY city_number"
        return conn.cursor().execute(sql, (user_id,)).fetchall()


def delete_temp_results(user_id):
    conn = create_connection()
    with conn:
        sql = "DELETE FROM temp_results WHERE user_id = ?"
        conn.cursor().execute(sql, (user_id,))
        conn.commit()
