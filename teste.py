import states
import pandas
import functions
import lexico


file = open("test.txt", "r")

for line in file:
    print("teste : ",line)
    lexico.lexico(line)

while lexico.tokens:
    token = lexico.tokens.pop(0)
    a = token.classe
    print(a)
