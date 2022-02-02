from typing import NamedTuple
import functions
import states


file = open("teste.txt", "r")
lexeme = ''
LINHA = 1
for line in file:
    pos = 0
    while pos <= len(line):
        if ( pos < len(line)):
            if ( line[pos] == '"'):
                x = functions.get_Lit(line,pos)
                lexeme = ''
                pos = pos + x + 2
                continue
            if ( line[pos].isdigit()):
                x = functions.get_Num(line,pos)
                lexeme = ''
                pos = pos + x
                continue
            if ( line[pos].isalpha()):
                x = functions.get_ID(line,pos)
                lexeme = ''
                pos = pos + x
                continue
            if ( line[pos] == '{'):
                x = functions.get_Comentario(line,pos)
                lexeme = ''
                pos = pos + x + 2
                continue
            if (line[pos] == '<' or line[pos] == '>'
                or line[pos] == '=' ):
                x = functions.get_OPR(line,pos)
                lexeme = ''
                pos = pos + x
                continue
            if (line[pos] == '('):
                x = functions.get_ABP(line,pos)
                lexeme = ''
                pos = pos + x
                continue
            if (line[pos] == ')'):
                x = functions.get_FCP(line,pos)
                lexeme = ''
                pos = pos + x
                continue
            if (line[pos] == '+' or line[pos] == '-' or
                line[pos] == '*' or line[pos] == '/'):
                x = functions.get_OPM(line,pos)
                lexeme = ''
                pos = pos + x
                continue
            if (line[pos] == ';'):
                x = functions.get_PTV(line,pos)
                lexeme = ''
                pos = pos + x
                continue
            else:
                x = functions.get_error(line,pos)
                lexeme = ''
                pos = pos + x
                continue

        pos = pos + 1
    LINHA = LINHA + 1
