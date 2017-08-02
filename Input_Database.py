import sqlite3

def insert_data(values):
    with sqlite3.connect("deadline_dates.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (Name, Open, Close) values (?,?,?)"
        cursor.execute(sql, values)
        db.commit()

if __name__ == "__main__":
    deadline = ("GS", 12, 12)
    insert_data(deadline)