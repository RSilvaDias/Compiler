from typing import NamedTuple
import functions

class token(NamedTuple):
    classe: str
    lexema: str
    tipo: str

class result(NamedTuple):
    token: token
    count: int
    pos: int

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


lexema = ''

def state0(entrada):
    global lexema
    lexema = ''
    global pos
    global colunaErro
    #print(entrada)
    if not entrada:
        return None
    elif entrada[0].isdigit():
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state12(entrada)
    elif entrada[0].isalpha():
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state11(entrada)
    elif entrada[0] == EOFError:
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state2(entrada)
    elif entrada[0] == '+' or entrada[0] == '-' or entrada[0] == '*' or entrada[0] == '/':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state6(entrada)
    elif entrada[0] == '<':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state4(entrada)
    elif entrada[0] == '{':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state1(entrada)
    elif entrada[0] == '>':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state19(entrada)
    elif entrada[0] == '=':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state20(entrada)
    elif entrada[0] == ')':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state7(entrada)
    elif entrada[0] == '(':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state8(entrada)
    elif entrada[0] == ';':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state9(entrada)
    elif entrada[0] == '"':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state10(entrada)
    elif entrada[0] == ' ' or ('\n' in entrada):
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state22(entrada)
    else:
        return tokenErro(entrada)

def state1(entrada):
    global lexema

    if not entrada:
        return tokenErro(entrada)
    elif entrada[0] == '}':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state21(entrada)
    elif hasAlphabet(entrada[0]):
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state1(entrada)
    else:
        return tokenErro(entrada)

def state2(entrada):
    global lexema

    if not entrada:
        return token('EOF', lexema, 'Nulo')
    else:
        return tokenErro(entrada)

def state3(entrada):
    global lexema

    if not entrada:
        return token('OPR', lexema, 'Nulo')
    else:
        return tokenErro(entrada)

def state4(entrada):
    global lexema
    if not entrada:
        return token('OPR', lexema, 'Nulo')
    elif entrada[0] == '-':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state5(entrada)
    elif entrada[0] == '=' or entrada[0] == '>':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state3(entrada)
    else:
        return tokenErro(entrada)

def state5(entrada):
    global lexema

    if not entrada:
        return token('RCB', lexema, 'Nulo')
    else:
        return tokenErro(entrada)

def state6(entrada):
    global lexema

    if not entrada:
        return token('OPM', lexema, 'Nulo')
    else:
        return tokenErro(entrada)

def state7(entrada):
    global lexema

    if not entrada:
        return token('FC_P', lexema, 'Nulo')
    elif entrada[0].isdigit():
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state25(entrada)
    else:
        return tokenErro(entrada)

def state8(entrada):
    global lexema

    if not entrada:
        return token('AB_P', lexema, 'Nulo')
    else:
        return tokenErro(entrada)

def state9(entrada):
    global lexema

    if not entrada:
        return token('PT_V', lexema, 'Nulo')
    else:
        return tokenErro(entrada)

def state10(entrada):
    global lexema

    if not entrada:
        return tokenErro(entrada)
    elif entrada[0] == '"':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state18(entrada)
    elif hasAlphabet(entrada[0]):
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state10(entrada)
    else:
        return tokenErro(entrada)

def state11(entrada):
    global lexema

    if not entrada:
        if ( functions.inList(lexema,tabela_de_simbolos)):
            return token(lexema,lexema,lexema)
        else:
            return token('id', lexema, 'Nulo')
    elif entrada[0].isdigit or entrada[0].isalpha or entrada[0] == '_':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state11(entrada)
    else:
        return tokenErro(entrada)

def state12(entrada):
    global lexema

    if not entrada:
        return token('NUM', lexema, 'inteiro')
    elif entrada[0].isdigit():
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state12(entrada)
    elif entrada[0] == '.':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state13(entrada)
    elif entrada[0] == 'E' or entrada[0] == 'e':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state15(entrada)
    else:
        return tokenErro(entrada)

def state13(entrada):
    global lexema

    if not entrada:
        return tokenErro(entrada)
    elif entrada[0].isdigit():
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state14(entrada)
    else:
        return tokenErro(entrada)

def state14(entrada):
    global lexema

    if not entrada:
        return token('NUM', lexema, 'real')
    elif entrada[0].isdigit():
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state14(entrada)
    elif entrada[0] == 'E' or entrada[0] == 'e':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state23(entrada)
    else:
        return tokenErro(entrada)

def state15(entrada):
    global lexema

    if not entrada:
        return tokenErro(entrada)
    elif entrada[0].isdigit():
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state17(entrada)
    elif entrada[0] == '+':
        lexema = lexema + entrada[0]
        entrada = entrada[1:]
        return state16(entrada)
    elif entrada[0] == '-':
        lexema = lexema + entrada[0]
        entrada = entrada[1:]
        return state24(entrada)
    else:
        return tokenErro(entrada)

def state16(entrada):
    global lexema

    if not entrada:
        return tokenErro(entrada)
    elif entrada[0].isdigit():
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state17(entrada)
    else:
        return tokenErro(entrada)

def state17(entrada):
    global lexema

    if not entrada:
        return token('NUM', lexema, 'inteiro')
    elif entrada[0].isdigit():
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state17(entrada)
    else:
        return tokenErro(entrada)

def state18(entrada):
    global lexema

    if not entrada:
        return token('Lit', lexema, 'literal')
    else:
        return tokenErro(entrada)

def state19(entrada):
    global lexema

    if not entrada:
        return token('OPR', lexema, 'Nulo')
    elif entrada[0] == '=':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state20(entrada)
    else:
        return tokenErro(entrada)

def state20(entrada):
    global lexema

    if not entrada:
        return token('OPR', lexema, 'Nulo')
    else:
        return tokenErro(entrada)

def state21(entrada):
    global lexema

    if not entrada:
        return token('Comentário', lexema, 'Nulo')
    else:
        return tokenErro(entrada)


def state22(entrada):
    global lexema

    return token('Ignorar', lexema, 'Nulo')

def state23(entrada):
    global lexema

    if not entrada:
        return tokenErro(entrada)
    elif entrada[0] == '+' or entrada[0] == '-':
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state24(entrada)
    elif entrada[0].isdigit():
        lexema = lexema + entrada[0]
        entrada = entrada[1:]
        return state25(entrada)
    else:
        return tokenErro(entrada)

def state24(entrada):
    global lexema

    if not entrada:
        return tokenErro(entrada)
    elif entrada[0].isdigit():
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state25(entrada)
    else:
        return tokenErro(entrada)

def state25(entrada):
    global lexema

    if not entrada:
        return token('NUM', lexema, 'real')
    elif entrada[0].isdigit():
        lexema  = lexema + entrada[0]
        entrada = entrada[1:]
        return state25(entrada)
    else:
        return tokenErro(entrada)

def tokenErro(entrada):
    global lexema

    lexema = lexema + entrada[0]
    functions.colunaErro = functions.pos - len(entrada)
    return token('ERRO', lexema, 'Nulo')

def hasAlphabet(value):
    if (value.isdigit() or value.isalpha()):
        return True
    elif value in ',:;!?/\*+-(){}[]<>= \'.':
        return True
    else:
        return False
