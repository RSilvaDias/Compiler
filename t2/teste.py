import states
import pandas as pd
import functions
import lexico
import numpy as np



file = open("test.txt", "r")

for line in file:
    lexico.lexico(line)

GOTO = pd.read_csv('tabela_goto.csv')
ACTION = pd.read_csv('tabela_action.csv')
#ACTION.reset_index(drop = False, inplace = True)
print(GOTO.to_string())
