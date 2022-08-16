
from multiprocessing.sharedctypes import Value
from rich.console import Console
from rich.progress import track
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table
from rich import print
import time
import os
import random
from collections.abc import MutableMapping
from datetime import date
from datetime import datetime
import hashlib
#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=# IMPORTAÇÃO CONCLÚIDA #=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#


data = date.today()


def hora_atual():
    hora = datetime.now()
    horaformatada = str(hora)
    hora_atual1 = horaformatada[11:16]
    return hora_atual1


def data_atual():
    d = datetime.now()
    dataf = str(d)
    data_a = dataf[0:11]
    return data_a


console = Console()


def clear(): return os.system('cls')


def panelLayout(text): return console.print(Panel(
    Padding(f'''{text}''', 1), title=f"[red] Gerador de Senha Segura [/] {data}"))


def menu():  # Menu Principal
    while True:
        clear()
        console.print(Panel(Padding('''1 - Gerar Senha Segura
2 - Exibir Hashes
3 - Exibir Senhas Geradas

99 - Sair
Obs.: Somente a insersão de [yellow]NÚMEROS INTEIROS[/] são permitidos!''', 1), title=f"[red] Gerador de Senha Segura [/] {data}"))
        try:
            # console.print(Panel(Padding((), 1), title="[red] Gerador de Senhas Seguras [/] {data}"))
            imenu = int(input('Escolha uma opção:  '))
            clear()
            return imenu
            break
        except ValueError:
            itext = 'Insira um número inteiro válido'
            clear()
            # console.print(Panel(Padding(f'{text}' , 1), title="[red] Ferramenta de Previsão no Tempo [/] {data}"))
            panelLayout('Digite um número [green]inteiro válido [/]')
            time.sleep(1)

        except KeyboardInterrupt:
            clear()
            # console.print('PARA SAIR DIGITE [red]"SAIR"[/]')
            panelLayout('Para sair, basta digitar "99"')
            time.sleep(1)


def genPass():
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '@#$&*()_+'
    nums = '1234567890'
    User_For = upper + lower + symbols + nums

    panelLayout('Tamanho da senha: ')
    length_pass = int(input())
    clear()

    if length_pass <= 32 and length_pass >= 6:
        try:
            passwd = ''.join(random.sample(User_For, length_pass))
            # for x in track(range(5), 'Gerando [red]senha segura [/]'):
            #   time.sleep(2)
            clear()
            panelLayout(
                f'Sua senha segura de {length_pass} caracteres foi gerada com sucesso....')
            time.sleep(1)
            clear()
            panelLayout(f'Sua senha segura é: {passwd}')
            panelLayout(
                '''Deseja criptografar a senha em Hash MD5 e salvar em um arquivo?
                    [green][S] - Sim [/] ou [red][SS] - Salvar sem Criptografar [/] ou [yellow][N] - Voltar ao Menu Principal''')
            save_question = input('Digite aqui: ')

            if save_question == 's' or save_question == 'S':
                clear()
                gerandohash = gerarHash(passwd)
                savePassinFiles(gerandohash)
                input('Aperte qualquer coisa para continuar...')

            elif save_question == 'ss' or save_question == 'SS':
                clear()
                decodeHash(passwd)

                input('Aperte qualquer coisa para continuar...')

            else:
                pass

        except ValueError:
            return

    elif length_pass < 6 or length_pass > 32:
        panelLayout(f'Insira um valor de 6 até 32')
        input('Aperte qualquer coisa para continuar...')
        clear()


def savePassinFiles(hash_pass_bytes):
    hora_atual_atual = hora_atual()
    data_atual_atual = data_atual()

    hash_pass = str(hash_pass_bytes)
    with open('arch_pass.txt', 'a', encoding='utf-8') as arch:
        arch.write(hash_pass + '\n')
    with open('date.txt', 'a', encoding='utf-8') as datearch:
        datearch.write(hora_atual_atual + '\n')
    with open('datehour.txt', 'a', encoding='utf-8') as datehourarch:
        datehourarch.write(data_atual_atual + '\n')
    return panelLayout('[green]Salvo com sucesso[/]')


def gerarHash(passwd_no_hash):
    md5_hash = hashlib.md5()
    passwd_no_hash_bytes = bytes(passwd_no_hash, 'utf-8')
    md5_hash.update(passwd_no_hash_bytes)
    hashfinal = md5_hash.hexdigest()
    return hashfinal


def decodeHash(password_var):
    with open('passwd.txt', 'a', encoding='utf-8') as passwdarch:
        passwdarch.write(password_var + '\n')
    return panelLayout('[green]Salvo sem criptografar com sucesso[/]')


def viewHashes():
    with open('arch_pass.txt', 'r', encoding='utf-8') as arch:
        lista = arch.readlines()

    with open('date.txt', 'r', encoding='utf-8') as datearch:
        listadehoras = datearch.readlines()

    with open('datehour.txt', 'r', encoding='utf-8') as datehourarch:
        listadedatas = datehourarch.readlines()

    tabela = Table(title='[blue]HASHES GERADOS[/]')
    tabela.add_column('DATA DE CRIAÇÃO', justify="center",
                      style="cyan", no_wrap=False)
    tabela.add_column('HORA DA CRIAÇÃO', justify="center",
                      style="cyan", no_wrap=False)
    tabela.add_column('HASH', justify="center", style="cyan", no_wrap=False)

    for data, hora, item in zip(listadedatas, listadehoras, lista):
        tabela.add_row(data, hora, item)
        tabela.add_row('', '', '')
    console.print(tabela, justify='center')


def viewPass():
    with open('passwd.txt', 'r', encoding='utf-8') as passwdarch:
        listadesenhas = passwdarch.readlines()

    tabela2 = Table(title='[green]SENHAS GERADAS[/]')
    # tabela2.add_column('DATA DE CRIAÇÃO', justify="center", #NOTA PARA O IGOR: AINDA FALTA APLICAR AS COLUNAS A SEGUIR, NECESSÁRIO CRIAR UMA FUNÇÃO QUE REGISTRE AS INFORMAÇÕES DE DATA E HORA DA CRIAÇÃO DA SENHA
    #                 style="cyan", no_wrap=False)

    # tabela2.add_column('HORA DA CRIAÇÃO', justify="center",
    #                 style="cyan", no_wrap=False)
    tabela2.add_column('PASSWORDS', justify='center')

    for item in listadesenhas:
        tabela2.add_row(item)
        tabela2.add_row('')
    console.print(tabela2, justify='center')
