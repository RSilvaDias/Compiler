from collections import namedtuple
import pandas as pd
import lexico
import functions
import states as s

qtdRegras = 38
pilha = []
arquivo_final = ["#include<studio.h>\n\n",
                 "typedef char literal[256];\n",
                 "void main(void)\n",
                 "{\n"]


def analise_semantica(pilha_semantica,A,B):
    # Acha o numero correto da regra gramatical
    for i in range(1,qtdRegras+1):
        if ( s.regras[i][0] == A and s.regras[i][1] == B):
            regra = i;
            #print("REGRA : ",regra)
            break;

    beta = functions.tamanho_beta(B)
    j = 0
    while (j < beta) and pilha_semantica:  #enquanto a pilha nao estiver vazia
        pilha.append(pilha_semantica[-1])
        pilha_semantica.pop()
        j = j + 1

    if regra == 1:
        token_p = pilha.pop()
        new_token = s.TOKEN(s.token("P'","P'","P'"),token_p.count,token_p.pos,token_p.linha)
        pilha_semantica.append(new_token)

    if regra == 2:
        token_inicio = pilha.pop()
        new_token = s.TOKEN(s.token("P","P","P"),token_inicio.count,token_inicio.pos,token_inicio.linha)
        pilha_semantica.append(new_token)

    if regra == 3:
        token_varinicio = pilha.pop()
        token_LV = pilha.pop()

        new_token = s.TOKEN(s.token("V","V","V"),token_varinicio.count,token_varinicio.pos,token_varinicio.linha)
        pilha_semantica.append(new_token)

    if regra == 4:
        token_D = pilha.pop()
        token_LV = pilha.pop()

        new_token = s.TOKEN(s.token("LV","LV","LV"),token_D.count,token_D.pos,token_D.linha)
        pilha_semantica.append(new_token)

    if regra == 5:
        token_varfim = pilha.pop()
        token_pt_v = pilha.pop()

        new_token = s.TOKEN(s.token("LV","LV","LV"),token_pt_v.count,token_pt_v.pos,token_pt_v.linha)
        pilha_semantica.append(new_token)

        for x in range(3):
            arquivo_final.append("\n")

    if regra == 6:
        token_TIPO = pilha.pop()
        token_L = pilha.pop()
        token_pt_v = pilha.pop()

        new_token = s.TOKEN(s.token("D","D",token_TIPO.token.tipo),token_TIPO.count,token_TIPO.pos,token_TIPO.linha)
        tipo = ""

        if ( token_TIPO.token.tipo == "inteiro"):
            tipo = "int"
        elif ( token_TIPO.token.tipo == "real"):
            tipo = "double"
        elif ( token_TIPO.token.tipo == "literal"):
            tipo = "literal"
        arquivo_final.append(tipo)
        arquivo_final.append(" ")
        arquivo_final.append(token_L.token.lexema)
        arquivo_final.append(";\n")
        pilha_semantica.append(new_token)

    if regra == 7: #Rever
        token_id = pilha.pop()
        token_vir = pilha.pop()
        token_L = pilha.pop()

        new_token = s.TOKEN("L",token_id.token.lexema+", "+token_L.token.lexema,token_L.token.tipo)
        token_id.token.tipo = token_L.token.tipo

        for i in range(len(s.tabela_de_simbolos)):
            if (s.tabela_de_simbolos[i].classe == token_id.token.classe and
                s.tabela_de_simbolos[i].lexema == token_if.token.lexema):

                if ( s.tabela_de_simbolos[i].tipo == "Nulo"):
                    s.tabela_de_simbolos[i].tipo = token_id.token.tipo

                elif ( s.tabela_de_simbolos[i].tipo == token_id.token.tipo):
                    s.erro_semantico = True;
                    print("Erro : tipo ja declarado ",token_id.token.lexema,
                    "regra 7 --- Linha : ",token_id.linha,"coluna :", token_id.pos)
                else:
                    s.erro_semantico = True;
                    print("Erro : tipo ja declarado , tipo diferente ",token_id.token.lexema,
                    "regra 7 --- Linha : ",token_id.linha,"coluna :", token_id.pos)

        pilha_semantica.append(new_token)

    if regra == 8:
        pilha_auxiliar = []
        while pilha_semantica:
            if (pilha_semantica[-1].token.classe == "TIPO"):
                token_id = pilha.pop()
                token_TIPO = pilha_semantica[-1]
                id2 = s.TOKEN(s.token(token_id.token.classe,token_id.token.lexema,token_TIPO.token.tipo),token_id.count,token_id.pos,token_id.linha)
                new_token = s.TOKEN(s.token("L",id2.token.lexema,id2.token.tipo),token_id.count,token_id.pos,token_id.linha)
                for x in range(len(s.tabela_de_simbolos)):
                    if (s.tabela_de_simbolos[x].classe == id2.token.classe and
                        s.tabela_de_simbolos[x].lexema == id2.token.lexema):
                        if (s.tabela_de_simbolos[x].tipo == "Nulo"):
                            aux = s.tabela_de_simbolos[x]                        #guarda o valor antigo
                            s.tabela_de_simbolos.pop(x)                          #tira da tabela
                            novo = s.token(aux.classe,aux.lexema,id2.token.tipo) #nova entrada
                            s.tabela_de_simbolos.insert(x,novo)                  #troca de tipo


                        elif (s.tabela_de_simbolos[x].tipo == id2.token.tipo):
                            s.erro_no_semantico = True
                            print("Erro: ja foi declarado com esse mesmo tipo" ,id2.token.lexema,"Regra 8. Linha: ",id2.linha,"COluna: ",id2.pos)

                        else: #PRECISA VOLTAR AQUI E ATUALIZAR A POSICAO
                            s.erro_no_semantico = True
                            print("Erro: ja foi declarado e o tipo e diferente do declarado. Linha :",token_TIPO.linha,"Coluna: ",token_TIPO.pos)

            pilha_auxiliar.append(pilha_semantica[-1])
            pilha_semantica.pop()

        while pilha_auxiliar:
            pilha_semantica.append(pilha_auxiliar[-1])
            pilha_auxiliar.pop()

        pilha_semantica.append(new_token)


    if regra == 9 or regra == 10 or regra == 11 :
        token_TIPO = pilha.pop()

        new_token = s.TOKEN(s.token("TIPO","TIPO",token_TIPO.token.tipo),token_TIPO.count,token_TIPO.pos,token_TIPO.linha)
        pilha_semantica.append(new_token)

    if regra == 12:
        token_ES = pilha.pop()
        token_A = pilha.pop()

        new_token = s.TOKEN(s.token("A","A","A"),token_A.count,token_A.pos,token_A.linha)
        pilha_semantica.append(new_token)

    if regra == 13:

        token_leia = pilha.pop()
        token_id = pilha.pop()
        token_pt_v = pilha.pop()

        nome = ''

        for i in range(len(s.tabela_de_simbolos)):
            if (s.tabela_de_simbolos[i].classe == token_id.token.classe and
                s.tabela_de_simbolos[i].lexema == token_id.token.lexema):
                if (s.tabela_de_simbolos[i].tipo != "Nulo"):
                    lexema = token_id.token.lexema;

                    if (s.tabela_de_simbolos[i].tipo == "literal"):
                        nome = "scanf(\"%s\", " + lexema + ");\n"
                        arquivo_final.append(nome)

                    elif (s.tabela_de_simbolos[i].tipo == "inteiro"):
                        nome = "scanf(\"%d\", &" + lexema + ");\n"
                        arquivo_final.append(nome)

                    elif (s.tabela_de_simbolos[i].tipo == "real"):
                        nome = "scanf(\"%lf\", &" + lexema + ");\n"
                        arquivo_final.append(nome)

                else:
                    s.erro_semantico = True
                    print("Erro : Variavel nao declarada" , token_id.token.lexema ,
                    " --- regra 13 -- linha : ", token_id.linha , "coluna : ", token_id.pos)

        new_token = s.TOKEN(s.token("ES",nome,"Nulo"),token_id.count,token_id.pos,token_id.linha)
        pilha_semantica.append(new_token)


    if regra == 14:

        token_escreva = pilha.pop()
        token_ARG = pilha.pop()
        token_pt_v = pilha.pop()

        nome = ''

        if ( token_ARG.token.tipo == "literal"):
            if(token_ARG.token.lexema[0] == '"'):
                nome = "printf(" + token_ARG.token.lexema +");\n"
            else:
                nome = "printf(\"%s\", " + token_ARG.token.lexema +");\n"
            arquivo_final.append(nome)

        elif (token_ARG.token.tipo == "inteiro"):
            nome = "printf(\"%d\", " + token_ARG.token.lexema +");\n"
            arquivo_final.append(nome)
        elif (token_ARG.token.tipo == "real"):
            nome = "printf(\"%lf\", " + token_ARG.token.lexema +");\n"
            aquivo_final.append(nome)

        new_token = s.TOKEN(s.token("ES",nome,"Nulo"),token_ARG.count,token_ARG.pos,token_ARG.linha)
        pilha_semantica.append(new_token)

    if regra == 15:

        token_lit = pilha.pop()

        new_token = s.TOKEN(s.token("ARG",token_lit.token.lexema,token_lit.token.tipo),token_lit.count,token_lit.pos,token_lit.linha)
        pilha_semantica.append(new_token)

    if regra == 16:

        token_num = pilha[-1]
        pilha.pop()

        new_token = s.TOKEN("ARG",token_num.token.lexema,token_num.token.tipo)
        pilha_semantica.append(new_token)

    if regra == 17:

        token_id = pilha[-1]
        pilha.pop()

        flag = False;
        for i in range(1,len(s.tabela_de_simbolos)):
            if (s.tabela_de_simbolos[i].classe == token_id.token.classe and
                s.tabela_de_simbolos[i].lexema == token_id.token.lexema ):
                flag = True

        if flag == False:
            s.erro_semantico = True
            print("Erro : Variavel nao declarada ",token_id.token.lexema,
            " Regra 17 -- Linha : ", token_id.linha , "Coluna : ", token_id.pos)

        new_token = s.TOKEN(s.token("ARG",token_id.token.lexema,token_id.token.tipo),token_id.count,token_id.pos,token_id.linha)
        pilha_semantica.append(new_token)

    if regra == 18:
        token_CMD = pilha.pop()
        token_A = pilha.pop()

        new_token = s.TOKEN(s.token("A","A","Nulo"),token_A.count,token_A.pos,token_A.linha)
        pilha_semantica.append(new_token)

    if regra == 19:
        nome = ''
        flag = False
        token_id = pilha.pop()
        token_rcb = pilha.pop()
        token_LD = pilha.pop()
        token_pt_v = pilha.pop()

        for i in range(1,len(s.tabela_de_simbolos)):
            if (s.tabela_de_simbolos[i].classe == token_id.token.classe and
                s.tabela_de_simbolos[i].lexema == token_id.token.lexema):

                if (token_LD.token.tipo == s.tabela_de_simbolos[i].tipo):
                    nome = token_id.token.lexema + " = "+token_LD.token.lexema+";\n"
                    arquivo_final.append(nome)
                else:
                    s.erro_semantico = True
                    print("Erro: Tipos diferentes para atribuicao. Regra 19 . Linha :",
                            token_id.linha,"Coluna: ",token_id.pos)
                flag = True
                break

        if flag == False:
            s.erro_semantico = True
            print("Erro: Variavel nao declarada ",token_id.token.lexema,"Regra 19. Linha:",
                    token_id.linha,"Coluna: ",token_id.pos)

        new_token = s.TOKEN(s.token("CMD",nome,"CMD"),token_pt_v.count,token_pt_v.pos,token_pt_v.linha)
        pilha_semantica.append(new_token)

    if regra == 20:
        token_OPRD1 = pilha.pop()
        token_opm = pilha.pop()
        token_OPRD2 = pilha.pop()

        new_token = s.TOKEN(s.token("LD","T"+str(s.valortx),token_OPRD1.token.tipo),token_OPRD1.count,token_OPRD1.pos,token_OPRD1.linha)
        pilha_semantica.append(new_token)
        if ((token_OPRD1.token.tipo == token_OPRD2.token.tipo) and
            (token_OPRD1.token.tipo != "literal") and
            (token_OPRD2.token.tipo != "literal")):

            nome = "T"+str(s.valortx)+"="+token_OPRD1.token.lexema+" "+token_opm.token.lexema+" "+token_OPRD2.token.lexema+";\n"
            arquivo_final.append(nome)
        else:
            s.erro_semantico = True
            print("Erro: Operandos com tipos incompativeis. Regra 20. Linha :",
                    token_OPRD2.linha," Coluna : ",token_OPRD2.pos)

    if regra == 21:
        token_OPRD = pilha.pop()

        new_token = s.TOKEN(s.token("LD",token_OPRD.token.lexema,token_OPRD.token.tipo),token_OPRD.count,token_OPRD.pos,token_OPRD.linha)
        pilha_semantica.append(new_token)

    if regra == 22:
        token_id = pilha.pop()

        flag = False
        for i in range(1,len(s.tabela_de_simbolos)):
            if (s.tabela_de_simbolos[i].classe == token_id.token.classe and
                s.tabela_de_simbolos[i].lexema == token_id.token.lexema):
                # OPRD.atributos <- id.atributos
                token_id2 = s.TOKEN(s.token(s.tabela_de_simbolos[i].classe,s.tabela_de_simbolos[i].lexema,s.tabela_de_simbolos[i].tipo),
                                    token_id.count,token_id.pos,token_id.linha)

                flag = True
                break

        if flag == False :
            s.erro_semantico = True
            print("Erro : Variavel nao declarada ",token_id.token.lexema ,"  Regra 22.  Linha " , token_id.linha , " Coluna ",  token_id.pos)

        new_token = s.TOKEN(s.token("OPRD",token_id2.token.lexema,token_id2.token.tipo),token_id2.count,token_id2.pos,token_id2.linha)
        pilha_semantica.append(new_token)

    if regra == 23:
        token_num = pilha[-1]
        pilha.pop()

        new_token = s.TOKEN(s.token("OPRD",token_num.token.lexema,token_num.token.tipo),token_num.count,token_num.pos,token_num.linha)
        pilha_semantica.append(new_token)

    if regra == 24:
        token_COND = pilha.pop()
        token_A = pilha.pop()

        new_token = s.TOKEN(s.token("A","A","Nulo"),token_A.count,token_A.pos,token_A.linha)
        pilha_semantica.append(new_token)

    if regra == 25:
        token_CAB = pilha.pop()
        token_CP = pilha.pop()

        new_token = s.TOKEN(s.token("COND","COND","COND"),token_CP.count,token_CP.pos,token_CP.linha)
        pilha_semantica.append(new_token)

    if regra == 26:
        token_se = pilha.pop()
        token_ab_p = pilha.pop()
        token_EXP_R = pilha.pop()
        token_entao = pilha.pop()

        nome = "if("+ token_EXP_R.token.lexema + ")\n"
        arquivo_final.append(nome)
        arquivo_final.append("{\n")

        new_token = s.TOKEN(s.token("CAB",nome,"CAB"),token_entao.count,token_entao.pos,token_entao.linha)
        pilha_semantica.append(new_token)

    if regra == 27:
        token_OPRD1 = pilha.pop()
        token_opm = pilha.pop()
        token_OPRD2 = pilha.pop()

        auxiliar = []

        for i in range(2):
            auxiliar.append(pilha_semantica[-1])
            pilha_semantica.pop()

        token_se_ou_repita = auxiliar[-1]

        while auxiliar:
            pilha_semantica.append(auxiliar[-1])
            auxiliar.pop()

        new_token = s.TOKEN(s.token("EXP_R","T"+str(s.valortx),token_OPRD1.token.tipo),token_OPRD1.count,token_OPRD1.pos,token_OPRD1.linha)
        pilha_semantica.append(new_token)

        if ( token_OPRD1.token.tipo == token_OPRD2.token.tipo):

            name = "T" + str(s.valortx) + "=" + token_OPRD1.token.lexema + " " + token_opm.token.lexema + " " + token_OPRD2.token.lexema + ";\n"
            arquivo_final.append(name)

            if (token_se_ou_repita.token.classe == "repita"):
                name = "while(T" + str(s.valortx) + ")\n"
                arquivo_final.append(name)
                arquivo_final.append("{\n")

            s.valortx = s.valortx + 1

        else:
            s.erro_semantico = True
            print("Erro: Operandos com tipos incompativeis. Regra 27. Linha :",token_OPRD2.linha," Coluna : ",token_OPRD2.pos)

    if regra == 28 or regra == 29 or regra == 30:
        token_ES_CMD_COND = pilha.pop()
        token_CP = pilha.pop()

        new_token = s.TOKEN(s.token("CP","CP","CP"),token_CP.count,token_CP.pos,token_CP.linha)
        pilha_semantica.append(new_token)

    if regra == 31:
        token_fimse = pilha.pop()

        new_token = s.TOKEN(s.token("CP","CP","CP"),token_fimse.count,token_fimse.pos,token_fimse.linha)
        pilha_semantica.append(new_token)

    if regra == 32:
        token_R = pilha.pop()
        token_A = pilha.pop()

        new_token = s.TOKEN(s.token("A","A","A"),token_A.count,token_A.pos,token_A.linha)
        pilha_semantica.append(new_token)

    if regra == 33:
        token_repita = pilha.pop()
        token_ap_b = pilha.pop()
        token_EXP_R = pilha.pop()
        token_fc_p = pilha.pop()
        token_CP_R = pilha.pop()

        new_token = s.TOKEN(s.token("R","R","R"),token_CP_R.count,token_CP_R.pos,token_CP_R.linha)
        pilha_semantica.append(new_token)

    if regra == 34 or regra == 35 or regra == 36:
        token_ES_CMD_COND = pilha.pop()
        token_CP_R = pilha.pop()

        new_token = s.TOKEN(s.token("CP_R","CP_R","CP_R"),token_CP_R.count,token_CP_R.pos,token_CP_R.linha)
        pilha_semantica.append(new_token)

    if regra == 37:
        token_fimrepita = pilha.pop()

        new_token = s.TOKEN(s.token("CP_R","CP_R","CP_R"),token_fimrepita.count,token_fimrepita.pos,token_fimrepita.linha)
        pilha_semantica.append(new_token)

        arquivo_final.append("}\n")
    if regra == 38:
        token_fim = pilha.pop()

        new_token = s.TOKEN(s.token("A","A","A"),token_fim.count,token_fim.pos,token_fim.linha)
        pilha_semantica.append(new_token)

    return pilha_semantica
