from contact.main import main
from contact.database import createConnection
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtSql import QSqlQuery


createConnection("contacts.sqlite")
db = QSqlDatabase.database()
db.tables()
# insertDataQuery = QSqlQuery()
# insertDataQuery.prepare(
#     """
#     INSERT INTO contacts (
#         nme,
#         phonenumber ,
#         email
#     )
#     VALUES (?, ?, ?)"""
#     )
# data = [
#     ("Linda", "22828228", "linda@example.com"),
#     ("Joe", "74963214", "joe@example.com"),
#     ("Lara", "81256397", "lara@example.com"),
#     ("David", "99996007", "david@example.com"),
#     ("Jane", "12554787", "jane@example.com"),
# ]
#
# for name, phonenumber, email in data:
#     insertDataQuery.addBindValue(name)
#     insertDataQuery.addBindValue(phonenumber)
#     insertDataQuery.addBindValue(email)
#     insertDataQuery.exec()
#
# query = QSqlQuery()
# query.exec("SELECT name, job, email FROM contacts")


# while query.next():
#     print(query.value(0), query.value(1), query.value(2))


if __name__ == "__main__":
    main()
