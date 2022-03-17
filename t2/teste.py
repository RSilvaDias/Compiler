import states
import pandas as pd
import functions
import lexico
import numpy as np



file = open("test.txt", "r")

for line in file:
    lexico.lexico(line)


ACTION = pd.read_csv('tabela_action.csv')
ACTION.reset_index(drop = False, inplace = True)

print(ACTION.to_string())
print(ACTION.at[0,"inicio"])
print(ACTION.at[int("2"),"varinicio"])

#while lexico.tokens:
#    token = lexico.tokens.pop(0)
#    a = token.classe
#    print(a)
