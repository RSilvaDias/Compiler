from typing import NamedTuple
import functions

class token(NamedTuple):
    classe: str
    lexema: str
    tipo: str

tabela_de_simbolos = []
tabela_de_simbolos.append(token('inicio','inicio','inicio'))
tabela_de_simbolos.append(token('varinicio','varinicio','varinicio'))
tabela_de_simbolos.append(token('varfim','varfim','varfim'))
tabela_de_simbolos.append(token('escreva','escreva','escreva'))
tabela_de_simbolos.append(token('leia','leia','leia'))
tabela_de_simbolos.append(token('se','se','se'))
tabela_de_simbolos.append(token('entao','entao','entao'))
tabela_de_simbolos.append(token('fimse','fimse','fimse'))
tabela_de_simbolos.append(token('repita','repita','repita'))
tabela_de_simbolos.append(token('fimrepita','fimrepita','fimrepita'))
tabela_de_simbolos.append(token('fim','fim','fim'))
tabela_de_simbolos.append(token('inteiro','inteiro','inteiro'))
tabela_de_simbolos.append(token('literal','literal','literal'))
tabela_de_simbolos.append(token('real','real','real'))

#functions.inList('entao',tabela_de_simbolos)
#functions.inList('isabela',tabela_de_simbolos)


pos = 0

file = open("teste.txt", "r")
lexema = ''
LINHA = 1
for line in file:
    #print("Linha : ", LINHA)
    pos = 0
    while pos <= len(line):
        if ( pos < len(line)):
            if ( line[pos] == '"'):  #Literal
                x = functions.get_Lit(line,pos)
                lexema = ''
                pos = pos + x + 2
                continue
            if ( line[pos].isdigit()): #Num
                x = functions.get_Num(line,pos)
                lexema = ''
                pos = pos + x
                continue
            if ( line[pos].isalpha()): # id
                x = functions.get_ID(line,pos)
                lexema = ''
                pos = pos + x
                continue
            if ( line[pos] == '{'):  #comentario
                x = functions.get_Comentario(line,pos)
                lexema = ''
                pos = pos + x + 2
                continue
            if (line[pos] == '<' or line[pos] == '>'
                or line[pos] == '=' ): #Operador Relacional
                x = functions.get_OPR(line,pos)
                lexema = ''
                pos = pos + x
                continue
            if (line[pos] == '('): #AB_P
                x = functions.get_ABP(line,pos)
                lexema = ''
                pos = pos + x
                continue
            if (line[pos] == ')'): #FC_P
                x = functions.get_FCP(line,pos)
                lexema = ''
                pos = pos + x
                continue
            if (line[pos] == '+' or line[pos] == '-' or
                line[pos] == '*' or line[pos] == '/'):
                x = functions.get_OPM(line,pos) #OPM
                lexema = ''
                pos = pos + x
                continue
            if (line[pos] == ';'): #PTV
                x = functions.get_PTV(line,pos)
                lexema = ''
                pos = pos + x
                continue

        pos = pos + 1
    LINHA = LINHA + 1
