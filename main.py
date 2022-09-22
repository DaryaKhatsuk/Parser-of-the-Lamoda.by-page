import sqlite3
from random import *
import datetime

class IncidentDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("IncidentDB.db")
        self.cursor = self.conn.cursor()

    def employees(self):
        creattab = "create table IF NOT EXISTS employees(id INTEGER PRIMARY KEY autoincrement, " \
                    "'registration number of the certificate' int, 'full name' text, 'title' text, 'address' text, " \
                    "'family composition' text);"
        self.cursor.execute(creattab)
        self.conn.commit()
        tabl = "insert into employees('registration number of the certificate', 'full name', 'title', " \
                "'address', 'family composition') values (?, ?, ?, ?, ?);"
        while True:
            exit1 = input("Для завершения введите 'д' ")
            if exit1 == "д":
                break
            else:
                try:
                    self.cursor.execute(tabl, (randint(1000000, 9999999), input("ФИО сотрудника: "),
                                               input("Звание: "), input("Адрес: "), input("Состав семьи: ")))
                except TypeError:
                    print("Неверный ввод")
        self.conn.commit()
        zap = "select * from employees;"
        self.cursor.execute(zap)
        k = self.cursor.fetchall()
        print(k)
        self.cursor.close()
        self.conn.close()
        print("a")