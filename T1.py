from typing import NamedTuple
import functions
import states

if __name__ == '__main__':

    file = open("teste.txt", "r")
    lexeme = ''
    for line in file:
        pos = 0
        while pos <= len(line):
            if ( pos < len(line)):
                if ( line[pos] == '"'):
                    x = functions.get_Lit(line,pos)
                    lexeme = ''
                    result = functions.scanner(x.result)
                    functions.printResult(states.TOKEN(result,x.count,x.pos,x.linha))
                    pos = pos + x.count + 2
                    continue
                if ( line[pos].isdigit()):
                    x = functions.get_Num(line,pos)
                    lexeme = ''
                    result = functions.scanner(x.result)
                    functions.printResult(states.TOKEN(result,x.count,x.pos,x.linha))
                    pos = pos + x.count
                    continue
                if ( line[pos].isalpha()):
                    x = functions.get_ID(line,pos)
                    lexeme = ''
                    result = functions.scanner(x.result)
                    functions.printResult(states.TOKEN(result,x.count,x.pos,x.linha))
                    pos = pos + x.count
                    continue
                if ( line[pos] == '{'):
                    x = functions.get_Comentario(line,pos)
                    lexeme = ''
                    result = functions.scanner(x.result)
                    functions.printResult(states.TOKEN(result,x.count,x.pos,x.linha))
                    pos = pos + x.count + 2
                    continue
                if (line[pos] == '<' or line[pos] == '>'
                    or line[pos] == '=' ):
                    x = functions.get_OPR(line,pos)
                    lexeme = ''
                    result = functions.scanner(x.result)
                    functions.printResult(states.TOKEN(result,x.count,x.pos,x.linha))
                    pos = pos + x.count
                    continue
                if (line[pos] == '('):
                    x = functions.get_ABP(line,pos)
                    lexeme = ''
                    result = functions.scanner(x.result)
                    functions.printResult(states.TOKEN(result,x.count,x.pos,x.linha))
                    pos = pos + x.count
                    continue
                if (line[pos] == ')'):
                    x = functions.get_FCP(line,pos)
                    lexeme = ''
                    result = functions.scanner(x.result)
                    functions.printResult(states.TOKEN(result,x.count,x.pos,x.linha))
                    pos = pos + x.count
                    continue
                if (line[pos] == '+' or line[pos] == '-' or
                    line[pos] == '*' or line[pos] == '/'):
                    x = functions.get_OPM(line,pos)
                    lexeme = ''
                    result = functions.scanner(x.result)
                    functions.printResult(states.TOKEN(result,x.count,x.pos,x.linha))
                    pos = pos + x.count
                    continue
                if (line[pos] == ';'):
                    x = functions.get_PTV(line,pos)
                    lexeme = ''
                    result = functions.scanner(x.result)
                    functions.printResult(states.TOKEN(result,x.count,x.pos,x.linha))
                    pos = pos + x.count
                    continue
                else:
                    x = functions.get_error(line,pos)
                    lexeme = ''
                    result = functions.scanner(x.result)
                    functions.printResult(states.TOKEN(result,x.count,x.pos,x.linha))
                    pos = pos + x.count
                    continue

            pos = pos + 1
        functions.LINHA = functions.LINHA + 1
