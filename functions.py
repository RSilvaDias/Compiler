import token

#Verify that lexeme is on list
def inList(lexema,tabela_de_simbolos):
    flag = False
    for i in range(len(tabela_de_simbolos)):
        if ( lexema == tabela_de_simbolos[i].lexema):
            flag = True
            break
    if ( flag == False):
        tabela_de_simbolos.append(token.token(lexema,lexema,lexema))
