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
    if (result.token.classe) != "Ignorar" and (result.token.classe) != "ERRO" :
        print("Classe:",result.token.classe ,
              ",Lexema:",result.token.lexema ,
              ",Tipo:",result.token.tipo)
    if (result.token.classe) == "ERRO":
        if(result.token.lexema[len(result.token.lexema)-1] == '\n'):
            if (result.token.lexema[0] == '{'):
                lexema = result.token.lexema[:len(result.token.lexema)-1]
                print("Classe:",result.token.classe ,
                      ",Lexema:",lexema,
                      ",Tipo:",result.token.tipo)
                print("ERRO léxico - Comentario Incompleto . ""Linha: ",result.linha,"Coluna: ",result.pos+1)
            if (result.token.lexema[0] == '"'):
                lexema = result.token.lexema[:len(result.token.lexema)-1]
                print("Classe:",result.token.classe ,
                      ",Lexema:",lexema,
                      ",Tipo:",result.token.tipo)
                print("ERRO léxico - Aspas Incompleta . ""Linha: ",result.linha,"Coluna: ",result.pos+1)
        else:
            print("Classe:",result.token.classe ,
                  ",Lexema:",result.token.lexema ,
                  ",Tipo:",result.token.tipo)
            print("ERRO léxico - Caractere Inválido. ""Linha: ",result.linha,"Coluna: ",result.pos+1)

def inList(lexema,tabela_de_simbolos):
    for i in range(len(tabela_de_simbolos)):
        if ( lexema == tabela_de_simbolos[i].lexema):
            return tabela_de_simbolos[i]
    return None

def get_error(line,pos):
    count = 0
    lexema = ''
    lexema = lexema + line[pos]
    pos = pos + 1
    count = count + 1
    # Error position is : pos - 1
    return (states.result(lexema,count,pos-1,LINHA))

def get_Lit(line,pos):
    count = 0
    lexema = ''
    lexema = lexema + line[pos]
    pos = pos + 1
    while (line[pos] != '"' and line[pos] != '\n'):
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
    while ( line[pos] != '}' and line[pos] != '\n'):
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
