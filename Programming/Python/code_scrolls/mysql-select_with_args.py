import pymysql

def mysqlAcess(myhost,databases,passw,porta):
    connmysql = pymysql.connect( 
        host=myhost, 
        user='root',
        password =passw, 
        db=databases,
        port=porta,
        )

# user args

    myarg = (input('Digite o Argumento aqui\n'))

    try:
        with connmysql.cursor() as cur:

            cur.execute('SELECT * FROM usuario WHERE id=%s',myarg) #ID arg
            #cur.execute('SELECT * FROM usuario WHERE nome_usuario=%s',myarg) NAME arg

            nome_usuario = cur.fetchone()
            print(nome_usuario)

    finally:
        connmysql.close()



mysqlAcess('localhost','farsoft_motoshowboutique','farsoft01',3306)