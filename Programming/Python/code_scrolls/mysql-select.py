import pymysql

def mysqlAcess(myhost,databases,passw,porta):
    connmysql = pymysql.connect( 
        host=myhost, 
        user='root',
        password =passw, 
        db=databases,
        port=porta,
        )


    try:
        with connmysql.cursor() as cur:
            cur.execute('SELECT * FROM usuario;')
            rows = cur.fetchall()
            for row in rows:
                print(f'{row[0]},{row[1]},{row[2]}')
    finally:
        connmysql.close()


# OR MORE SIMPLE


"""
    try:
        with connmysql.cursor() as cur:
            cur.execute('SELECT * FROM usuario;')
            res = cur.fetchall()
            print (res)
    finally:
        connmysql.close()
"""



mysqlAcess('localhost','sakilla','102030',3306)