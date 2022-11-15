import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_productos(conn, producto):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO productos(nombre, marca, fecha_venc, precio, stock)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, producto)
    conn.commit()
    return cur.lastrowid





def main():
    database = r"Supermark.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        # producto = ("Lavandina", "X5", "19-12-2022", 300.5, 100)
        producto = ("Azucar", "Ledesma", "24-12-2022", 350.5, 250)
        create_productos(conn, producto)


if __name__ == '__main__':
    main()