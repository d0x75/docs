# CRIAÇÃO DE UMA FUNÇÃO PARA FAZER A CONEXÃO NO BANCO DE DADOS

def mysqlAcess(myhost,databases,passw,porta):
    connmysql = pymysql.connect( 
        host=myhost, 
        user='root',
        password =passw, 
        db=databases,
        port=porta,
        cursorclass=pymysql.cursors.DictCursor
        )