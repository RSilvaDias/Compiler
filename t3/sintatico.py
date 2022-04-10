import pandas as pd
import lexico
import functions
import states
import semantica


def Parser():
    pilha_semantica = []
    pilha = []
    GOTO = pd.read_csv('tabela_goto.csv')
    ACTION = pd.read_csv('tabela_action.csv')
    ACTION.fillna("e", inplace=True)
    GOTO.fillna("e", inplace=True)



    file = open("test.txt", "r")

    for line in file:
        lexico.lexico(line)


    ######## IMPLEMENTACAO ALGORITMO #########
    lexico.tokens.append(states.TOKEN(states.token("$","$","$"),0,0,0))
    pilha.append(0)                 #State 0

    token = functions.SCANNER()
    a = token.token.classe

    while True:

        estado = pilha[-1]
        acao =  ACTION.at[int(estado),a.lower()]     #Pega a acao na tabela ACTION

        if acao[0] == 's':      #SHIFT
            t = acao[1:]        # Pega o numero da acao
            pilha.append(t)     # Estado no topo da pilha

            pilha_semantica.append(token)
            antigo = token
            if lexico.tokens:
                token = functions.SCANNER()

            a = token.token.classe

        elif acao[0] == 'r':         # REDUCE
            t = acao[1:]             # Pega o numero da acao
            A = states.regras[int(t)][0]    # Pega a parte esquerda da regra
            B = states.regras[int(t)][1]    # Pega a prte direita da regra
            beta = functions.tamanho_beta(B)

            for i in range(beta):       #Deletando tamanho de beta da pilha
                pilha.pop();

            t = pilha[-1]               # Topo da pilha
            acao2 = GOTO.at[int(t),A]   # Pega o estado na tabela GOTO
            pilha.append(int(acao2))
            print(A,"->",B)

            #CHAMADA SEMANTICA
            pilha_semantica = semantica.analise_semantica(pilha_semantica,A,B)

        elif acao == "ACEITO":
            A = states.regras[int(estado)][0]
            B = states.regras[int(estado)][1]

            print(A,"->",B)
            break
        else:
            #Tratamento de ERRO
            states.erro_sintatico = True
            erro = ''
            for i in range(len(states.terminais)):
                erro = states.terminais[i][0]
                if (ACTION.at[int(estado),erro] != "e"):
                    break

            print("ERRO SINTATICO -- Missing token:  ",erro," Linha : ", antigo.linha," Coluna: ", antigo.pos+2)
            flag = False

            while (pilha and flag == False):
                s = pilha[-1]

                for i in range(len(states.nao_terminais)):
                    if GOTO.at[int(s),states.nao_terminais[i][0]] != 'e':
                        flag = True
                        s2 = GOTO.at[int(s),states.nao_terminais[i][0]]
                        break;

                if flag == True:
                    pilha.append(int(s2))
                if flag == False:
                    pilha.pop()
                if not pilha:
                    print("PILHA VAZIA")

            s = pilha[-1]

            while True:
                if(ACTION.at[int(s),a.lower()] != 'e'):
                    break
                if a == "$" and not lexico.tokens:

                    print("PARSER FINALIZADO")
                    exit()

                antigo = token
                if lexico.tokens:
                    token = functions.SCANNER()
                    a = token.token.classe

    #print(ACTION.to_string())
    #print(GOTO.to_string())
