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

            cur.execute('SELECT id,nome_usuario,login,senha FROM usuario;')

            rows = cur.fetchall()

            desc = cur.description

            print(f'{desc[0][0]:<8} {desc[1][0]:<15} {desc[2][0]:>10} {desc[3][0]:>10}')
            for row in rows:
                print(f'{row[0]:<8} {row[1]:<15} {row[2]:>10} {row[3]:>10}')
    finally:
        connmysql.close()


mysqlAcess('localhost','farsoft_motoshowboutique','farsoft01',3306)