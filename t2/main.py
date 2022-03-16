import pandas as pd

pilha = []
GOTO = pd.read_csv('tabela_goto.csv')
ACTION = pd.read_csv('tabela_action.csv')


# pilha[-1] - Get the top element on stack

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
          ["R","repita ab_p EXP_R fc_p CP_R"],
          ["CP_R","ES CP_R"],
          ["CP_R","CMD CP_R"],
          ["CP_R","CND CP_R"],
          ["CP_R","fimrepita"],
          ["A","fim"]]
j = 1
while ( j < len(regras)):
    print(regras[j][0], "->", regras[j][1])
    j = j + 1

######## IMPLEMENTACAO ALGORITMO #########
pilha.append(0) #State 0

token = get_token()
a = token.classe
while True:
    estado = pilha[-1]
    acao =  ACTION.at[estado,a]     #Pega a acao na tabela ACTION

    if acao[0] == 's':   #SHIFT
        t = acao[1:]     # Pega o numero da acao
        pilha.append(t)  # Estado no topo da pilha
        token            # pega o proximo token

    elif acao[0] == 'r':    #REDUCE
        t = acao[1:]        # Pega o numero da acao
        A = regras[t][0]    # Pega a parte esquerda da regra
        B = regras[t][1]    # Pega a prte direita da regra
        beta = functions.tamanho_beta(B)

        for i in range(beta):       #Deletando tamanho de beta da pilha
            pilha.pop();

        t = pilha[-1]       # Topo da pilha
        acao = GOTO.at[t,A] # Pega o estado na tabela GOTO
        pilha.append(acao[1:])

        print(A,"->",B)

    elif acao == "ACEITO":
        A = regras[estado][0]
        B = regras[estado][1]

        print(A,"->",B)
        break
    else:
        #Tratamento de ERRO

#print(ACTION.to_string())
#print(GOTO.iat[0,0])

## GETTING AN ELEMENT
#print(ACTION.at[0,"inicio"])
#print(ACTION.iat[0,0]) using int only
