import pandas as pd
import lexico
import functions
import states as s
import semantica as sem
import sintatico

programa = ["#include<studio.h>\n\n",
             "typedef char literal[256];\n",
             "void main(void)\n",
             "{\n"]


def main():


    sintatico.Parser()

    #IMPRESSAO DO ARQUIVO
    if not s.erro_lexico and not s.erro_semantico and not s.erro_sintatico:
        for i in sem.arquivo_final:
            programa.append(i)

        final = []

        for j in range(len(programa)):

            if j == 4:
                final.append("\n")
                for valor in range(s.valortx):
                    nome = "int T" + str(valor) + ";\n"
                    final.append(nome)
                final.append("\n")
            final.append(programa[j])


        f = open("programa.c","w")
        indent = 0

        for i in range(len(final)):
            if (len(final[i]) != 0 ) and final[i][0] == '}':
                indent -= 1
            for x in range(indent):
                f.write("  ")
            if final:
                f.write(final[i])
            if len(final[i]) != 0 and final[i][0] == "{":
                indent += 1
        f.write("}")



main()
