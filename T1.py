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

def Scanner2(entrada):
    #Estado inicial
    if (entrada == ''):
        return
    #print(entrada[0])
    if (entrada[0].isalpha()):
        #transicao estado id
        print("id")
    elif (entrada[0].isdigit()):
        #transicao estado num
        print("digito")
    elif (entrada[0] == "("):
        #transicao estado AB_P
        result = token('AB_P','(','Nulo')
        print("Classe: ",result.classe,", Lexema: ",result.lexema,", Tipo: ",result.tipo)
        return result
    elif (entrada[0] == ')'):
        result = token('FC_P',')','Nulo')
        print("Classe: ",result.classe,", Lexema: ",result.lexema,", Tipo: ",result.tipo)
        return result
    elif (entrada[0] == '+' or entrada[0] == '-' or entrada[0] == '/' or entrada[0] == '*'):
        result = token('OPR',entrada[0],'Nulo')
        print("Classe: ",result.classe,", Lexema: ",result.lexema,", Tipo: ",result.tipo)
        return result
    return entrada


file = open("teste.txt", "r")
lexema = ''
operador = ''
quebra = ''
for line in file:
    for character in line:
        if (character == ' ' or character == '/n'):
            print(lexema)
            lexema = ''
        elif ( character == '(' or character == ')'):
            print(lexema)
            lexema = ''
            lexema = lexema + character
            print(lexema)
            lexema = ''
        elif (character == '<' or character == '>' or character == '=' or character == '-'):
            if ( operador == ''):
                print(lexema)
                lexema = ''
                operador = operador + character
            else:
                operador = operador + character
                print(operador)
                operador = ''
                lexema = ''
        elif ( character == '"'):
            if (lexema != ''):
                print(lexema)
                lexema = ''
                lexema = lexema + character
            else:
                lexema = lexema + character
        elif ( character == ';'):
            if ( lexema != ''):
                print(lexema)
                lexema = ''
                lexema = lexema + character
        elif ( character == ':' or character == '+' or character == '/' or character == '*'):
            if ( lexema != ''):
                print(lexema)
                lexema = ''
                lexema = lexema + character
        elif ( character == '\\'):
            print(lexema)
            lexema = ''
            quebra = quebra + character
            #lexema = lexema + character
        elif ( character == 'n' and quebra == '\\'):
            if ( operador != ''):
                print(operador)
                operador = ''
            if (lexema == '"' or lexema == ';' or lexema == ':' or lexema == '+' or lexema == '/' or lexema == '*'):
                print(lexema)
                lexema = ''
            print(lexema)
            lexema = ''
            quebra = quebra + character
            print (quebra)
            quebra = ''
        else:
            if ( operador != ''):
                print(operador)
                operador = ''
            if (lexema == '"' or lexema == ';' or lexema == ':' or lexema == '+' or lexema == '/' or lexema == '*'):
                print(lexema)
                lexema = ''
            lexema = lexema + character
    print(lexema)

def Scanner(entrada):
    print(entrada)
    return entrada
#Separar quebra de linha
#isalpha() #verifica letras
#isdigit() #verifica digitos
