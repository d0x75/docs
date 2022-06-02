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
            cur.execute('SELECT VERSION()')
            ver = cur.fetchone()
            print (f'Database Version : {ver[0]}')
    finally:
        connmysql.close()


mysqlAcess('localhost','sakilla','10203040',3306)