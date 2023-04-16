import sqlite3
import time

path_to_sqlite_db = "/Users/jesse/wghub-frontend/prisma/database.db"

connection = sqlite3.connect(path_to_sqlite_db)
cur = connection.cursor()
benutzer_table = "benutzer"


def find_all_benutzer():
    return cur.execute(f"SELECT * FROM {benutzer_table}").fetchall()


def delete_benutzer(benutzer_id):
    cur.execute(f"DELETE FROM {benutzer_table} WHERE id={benutzer_id}")
    connection.commit()


def update_online_status(benutzer_id: int, online: bool):

    online_num = 0
    if online:
        online_num = 1

    cur.execute(f"UPDATE {benutzer_table} SET online={online_num} WHERE id={benutzer_id}")
    connection.commit()

    print(f"Status von {benutzer_id} zu {online} geändert")


def add_benutzer(benutzer_id: int, nachname: str, vorname: str, strasse: str, hausnummer: str, mac_adresse: str,
                 online: int):
    cur.execute(
        f"INSERT INTO {benutzer_table} VALUES ({benutzer_id}, '{nachname}', '{vorname}', '{strasse}','{hausnummer}', '{mac_adresse}' , {online})")
    connection.commit()


if __name__ == '__main__':

    while True:

        from scanner import find_mac_addresses

        macs = find_mac_addresses()
        benutzer = find_all_benutzer()

        for b in benutzer:

            mac = str(b[5]).lower()
            online = False

            if mac in macs:
                online = True

            update_online_status(b[0], online)

        time.sleep(30)
