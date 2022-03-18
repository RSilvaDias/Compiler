import pandas as pd
import lexico
import functions
import states

pilha = []
GOTO = pd.read_csv('tabela_goto.csv')
ACTION = pd.read_csv('tabela_action.csv')
#ACTION.reset_index(drop = False, inplace = True)
ACTION.fillna("e", inplace=True)
GOTO.fillna("e", inplace=True)

regras = [[],
          ["P'","P"],
          ["P","inicio V A"],
          ["V","varinicio LV"],
          ["LV","D LV"],
          ["LV","varfim pt_v"],
          ["D","TIPO L pt_v"],
          ["L","id vir L"],
          ["L","id"],
          ["TIPO","inteiro"],
          ["TIPO","real"],
          ["TIPO","literal"],
          ["A","ES A"],
          ["ES","leia id pt_v"],
          ["ES","escreva ARG pt_v"],
          ["ARG","lit"],
          ["ARG","num"],
          ["ARG","id"],
          ["A","CMD A"],
          ["CMD","id rcb LD pt_v"],
          ["LD","OPRD opm OPRD"],
          ["LD","OPRD"],
          ["OPRD","id"],
          ["OPRD","num"],
          ["A","COND A"],
          ["COND","CAB CP"],
          ["CAB","se ab_p EXP_R fc_p entao"],
          ["EXP_R","OPRD opr OPRD"],
          ["CP","ES CP"],
          ["CP","CMD CP"],
          ["CP","COND CP"],
          ["CP","fimse"],
          ["A","R A"],
          ["R","repita ab_p EXP_R fc_p CPR"],
          ["CPR","ES CPR"],
          ["CPR","CMD CPR"],
          ["CPR","CND CPR"],
          ["CPR","fimrepita"],
          ["A","fim"]]

file = open("test.txt", "r")

for line in file:
    lexico.lexico(line)

######## IMPLEMENTACAO ALGORITMO #########
lexico.tokens.append(states.token("$","$","$"))
pilha.append(0)     #State 0

token = lexico.tokens.pop(0)
a = token.classe

while True:

    estado = pilha[-1]
    acao =  ACTION.at[int(estado),a.lower()]     #Pega a acao na tabela ACTION

    if acao[0] == 's':      #SHIFT
        t = acao[1:]        # Pega o numero da acao
        pilha.append(t)     # Estado no topo da pilha
        if lexico.tokens:
            token = lexico.tokens.pop(0)
        a = token.classe

    elif acao[0] == 'r':    #REDUCE
        t = acao[1:]        # Pega o numero da acao
        A = regras[int(t)][0]    # Pega a parte esquerda da regra
        B = regras[int(t)][1]    # Pega a prte direita da regra
        beta = functions.tamanho_beta(B)

        for i in range(beta):       #Deletando tamanho de beta da pilha
            pilha.pop();

        t = pilha[-1]       # Topo da pilha
        acao2 = GOTO.at[int(t),A] # Pega o estado na tabela GOTO
        # TODO: verificar esse empilhamento
        pilha.append(int(acao2)) #acao2[1:]
        print(A,"->",B)

    elif acao == "ACEITO":
        A = regras[int(estado)][0]
        B = regras[int(estado)][1]

        print(A,"->",B)
        break
    else:
        #Tratamento de ERRO
        erro = ''
        for i in range(len(states.terminais)):
            erro = states.terminais[i][0]
            if (ACTION.at[int(estado),erro] != "e"):
                break

        print("ERRO SINTATICO - Token Missing - ",erro,"na posicao: ")
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
            if a == "$":

                print("PARSER FINALIZADO")
                exit()

            token = lexico.tokens.pop(0)
            a = token.classe

#print(ACTION.to_string())
#print(GOTO.iat[0,0])

## GETTING AN ELEMENT
#print(ACTION.at[0,"inicio"])
#print(ACTION.iat[0,0]) using int only
