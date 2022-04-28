import sys

# PARSING SQL File
def parse_sql(filename):
    data = open(filename, 'r').readlines()
    stmts = []
    DELIMITER = ';'
    stmt = ''
    # INICIANDO O LOOP, E VERIFICANDO SE HÁ ALGUM ESPAÇO EM BRANCO NA LINHA , SE HOUVER INTERROMPE A ITERAÇÃO ATUAL.
    for lineno, line in enumerate(data):
        if not line.strip():
            continue
    # CONDICIONAL QUE VERIFICA SE HÁ UM COMENTÁRIO ' -- ' NO INICIO DA LINHA, SE HOUVER INTERROMPE A ITERAÇÃO ATUAL.
        if line.startswith('--'):
            continue
    # CONDICIONAL QUE VERIFICA SE HÁ A PALAVRA 'DELIMITER' NA LINHA .. FAZER ALGO PARA TRATAR CASO TENHA.!!!!!!
        if 'DELIMITER' in line:
            DELIMITER = line.split()[1]
            continue
    # CONDICIONAL QUE VERIFICA SE HÁ O VALOR DA VARIÁVEL DELIMITER ';' NA LINHA, E VAI IR SALVANDO NA VARIÁVEL stmt AS LINHAS QUE NÃO TIVEREM ' ; ' 

        if (DELIMITER not in line):
            stmt += line.replace(DELIMITER, ';')
            continue
    # FINALIZANDO O PARSING DO ARQUIVO

        if stmt:
            stmt += line
            stmts.append(stmt.strip()) 
            stmt = ''
        else:
            stmts.append(line.strip())
    return stmts