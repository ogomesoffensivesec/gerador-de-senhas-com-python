
import random
import gensecurepass

# Criando os dicionários
# Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Oo Pp Qq Rr Ss Tt Uu Vv Ww Xx Yy Zz @#$ ̈&*()_+ 1234567890

# Importando o Menu do módulo gensecurepass (Módulo da Aplicação)

while True:
    menu = gensecurepass.menu()

    if menu == 1:
        gensecurepass.genPass()
    elif menu == 2:
        gensecurepass.viewHashes()
        input('Aperte qualquer coisa para continuar...')
        # Gerando senha
        # gensecurepass.genPass()
    elif menu == 3:
        gensecurepass.viewPass()
        input('Aperte qualquer coisa para continuar...')
    elif menu == 99:
        exit()
