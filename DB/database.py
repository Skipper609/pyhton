import sqlite3
import beautifultable
host_name = "data.db"
def create_table():
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("create table student (regno integer primary key, name text,sem integer,placed integer)")
        
    except Exception as E:
        print(E)
    finally:
        conn.close()
#create_table()
def add_new_student(regno, name, sem, placed):
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("insert into student (regno,name,sem,placed) values (?,?,?,?)",(regno, name, sem, placed))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def display_details():
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("select regno,name,sem,placed from student")
        rows = cursor.fetchall()
        table = beautifultable.BeautifulTable()
       
        table.column_headers = ['Regno', 'Name', 'Sem', 'Status']
        for row in rows:
            status = "Placed" if row[3] == 1 else "Not placed"
            table.append_row([row[0],row[1],row[2],status])
        print(table)
    except Exception as e:
        print(e)
    finally:
        conn.close()

def update_pla_status(regno, placed):
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("update student set placed = ? where regno = ?",(placed, regno))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def display_details_regno(regno):
    try:
        conn = sqlite3.connect(host_name)
        cursor = conn.cursor()
        cursor.execute("select regno,name,sem,placed from student where regno = ? ",(regno,))
        rows = cursor.fetchall()
        table = beautifultable.BeautifulTable()
       
        table.column_headers = ['Regno', 'Name', 'Sem', 'Status']
        for row in rows:
            status = "Placed" if row[3] == 1 else "Not placed"
            table.append_row([row[0],row[1],row[2],status])
        print(table)
    except Exception as e:
        print(e)
    finally:
        conn.close()

display_details_regno(101)