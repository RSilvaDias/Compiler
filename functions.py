import token

#Verify that lexeme is on list
def inList(lexema,tabela_de_simbolos):
    flag = False
    for i in range(len(tabela_de_simbolos)):
        if ( lexema == tabela_de_simbolos[i].lexema):
            flag = True
            break
    if ( flag == False):
        tabela_de_simbolos.append(token.token(lexema,lexema,lexema))

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
    print(lexema)
    lexema = ''
    return count

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
    print(lexema)
    lexema = ''
    return count

def get_Num(line,pos):
    count = 0
    lexema = ''
    while ( line[pos].isdigit() or line[pos] == 'e' or line[pos] == '.'
            or line[pos] == 'E' or line[pos] == '+' or line[pos] == '-'):
            lexema = lexema + line[pos]
            pos = pos + 1
            count = count + 1
    print(lexema)
    lexema = ''
    return count

def get_ID(line,pos):
    count = 0
    lexema = ''
    while ( line[pos].isalpha() or line[pos].isdigit() or line[pos] == '_'):
        lexema = lexema + line[pos]
        pos = pos + 1
        count = count + 1
    print(lexema)
    lexema = ''
    return count

def get_OPR(line,pos):
    count = 0
    lexema =  ''
    # Pode gerar erro nos operadores , REVISAR
    while ( line[pos] == "-" or line[pos] == '<' or line[pos] == '>' or line[pos] == '=' ):
        lexema = lexema + line[pos]
        pos = pos + 1
        count = count + 1
    print(lexema)
    lexema = ''
    return count

def get_ABP(line,pos):
    count = 0
    lexema = ''
    lexema = lexema + line[pos]
    pos = pos + 1
    count = count + 1
    print(lexema)
    lexema = ''
    return count

def get_FCP(line,pos):
    count = 0
    lexema = ''
    lexema = lexema + line[pos]
    pos = pos + 1
    count = count + 1
    print(lexema)
    lexema = ''
    return count

def get_OPM(line,pos):
    count = 0
    lexema = ''
    lexema = lexema + line[pos]
    pos = pos + 1
    count = count + 1
    print(lexema)
    lexema = ''
    return count

def get_PTV(line,pos):
    count = 0
    lexema = ''
    lexema = lexema + line[pos]
    pos = pos + 1
    count = count + 1
    print(lexema)
    lexema = ''
    return count
