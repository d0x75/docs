import pymysql

def mysqlAcess(myhost,databases,passw,porta):
    connmysql = pymysql.connect( 
        host=myhost, 
        user='root',
        password =passw, 
        db=databases,
        port=porta,
        cursorclass=pymysql.cursors.DictCursor
        )

    try:
        with connmysql.cursor() as cur:
            cur.execute('SELECT * FROM usuario;')
            rows = cur.fetchall()
            for row in rows:
                print(row['nome_usuario'], ' - ',  row['email'])
    finally:
        connmysql.close()


mysqlAcess('localhost','farsoft_motoshowboutique','farsoft01',3306)