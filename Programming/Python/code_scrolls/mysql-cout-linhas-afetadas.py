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
            cur.execute('SELECT * FROM usuario WHERE id IN (1, 2, 3)')
            print(f'The query affected {cur.rowcount} rows')
    finally:
        connmysql.close()


mysqlAcess('localhost','farsoft_motoshowboutique','farsoft01',3306)