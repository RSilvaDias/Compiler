import states

global LINHA
LINHA = 1
global pos
pos = 0
global colunaErro
colunaErro = 0

def scanner(entrada):
    return states.state0(entrada)

def printResult(result):
    if (result.token.classe) != "Ignorar":
        print("Classe:",result.token.classe ,
              ",Lexema:",result.token.lexema ,
              ",Tipo:",result.token.tipo)



def inList(lexema,tabela_de_simbolos):
    flag = False
    for i in range(len(tabela_de_simbolos)):
        if ( lexema == tabela_de_simbolos[i].lexema):
            flag = True
            return True
    if ( flag == False):
        return False

def get_error(line,pos):
    count = 0
    lexema = ''
    lexema = lexema + line[pos]
    pos = pos + 1
    count = count + 1
    # Error position is : pos - 1
    return (states.result(lexema,count,pos-1,LINHA))

def get_Lit(line,pos): #Pega a constante literal
    count = 0
    lexema = ''
    lexema = lexema + line[pos]
    pos = pos + 1
    while (line[pos] != '"'):
        lexema = lexema + line[pos]
        pos = pos + 1
        count = count + 1
    lexema = lexema + line[pos]
    pos = pos + 1
    return (states.result(lexema,count,pos-1,LINHA))

def get_Comentario(line,pos):
    count = 0
    lexema = ''
    lexema = lexema + line[pos]
    pos = pos + 1
    while ( line[pos] != '}'):
        lexema = lexema + line[pos]
        pos = pos + 1
        count = count + 1
    lexema = lexema + line[pos]
    pos = pos + 1
    return (states.result(lexema,count,pos-1,LINHA))

def get_Num(line,pos):
    count = 0
    lexema = ''
    while ( line[pos].isdigit() or line[pos] == 'e' or line[pos] == '.'
            or line[pos] == 'E' or line[pos] == '+' or line[pos] == '-'):
            lexema = lexema + line[pos]
            pos = pos + 1
            count = count + 1
    return (states.result(lexema,count,pos-1,LINHA))

def get_ID(line,pos):
    count = 0
    lexema = ''
    while ( line[pos].isalpha() or line[pos].isdigit() or line[pos] == '_'):
        lexema = lexema + line[pos]
        pos = pos + 1
        count = count + 1
    return (states.result(lexema,count,pos-1,LINHA))

def get_OPR(line,pos):
    count = 0
    lexema =  ''
    # Pode gerar erro nos operadores , REVISAR
    while ( line[pos] == "-" or line[pos] == '<' or line[pos] == '>' or line[pos] == '=' ):
        lexema = lexema + line[pos]
        pos = pos + 1
        count = count + 1
    return (states.result(lexema,count,pos-1,LINHA))

def get_ABP(line,pos):
    count = 0
    lexema = ''
    lexema = lexema + line[pos]
    pos = pos + 1
    count = count + 1
    return (states.result(lexema,count,pos-1,LINHA))

def get_FCP(line,pos):
    count = 0
    lexema = ''
    lexema = lexema + line[pos]
    pos = pos + 1
    count = count + 1
    return (states.result(lexema,count,pos-1,LINHA))

def get_OPM(line,pos):
    count = 0
    lexema = ''
    lexema = lexema + line[pos]
    pos = pos + 1
    count = count + 1
    return (states.result(lexema,count,pos-1,LINHA))

def get_PTV(line,pos):
    count = 0
    lexema = ''
    lexema = lexema + line[pos]
    pos = pos + 1
    count = count + 1
    return (states.result(lexema,count,pos-1,LINHA))
