import webbrowser as wb
import os
import random as rm
# Assitente Virtual 2.0 sem UI.

#Feito por Gianluca Zugno 

# Data da ultima versão: 24/06/2022

def main():
    # Tag
    print(r"""

     _____                          ___  ___                 
    /  __ \ |   (_) | (_)       ( ) |  \/  |                 
    | /  \/ |__  _| | |_ _ __   |/  | .  . | ___ _ __  _   _ 
    | |   | '_ \| | | | | '_ \      | |\/| |/ _ \ '_ \| | | |
    | \__/\ | | | | | | | | | |     | |  | |  __/ | | | |_| |
    \_____/_| |_|_|_|_|_|_| |_|     \_|  |_/\___|_| |_|\__,_|

                """)

    print("Selecione operação: \n")
    print("-- Abrir Jogo[1] -- \n")
    print("-- Abrir Google[2] -- \n")

main()


def selection():
    try:
        select = int(input())
        if select == 1:
            os.system("cls")
            print("Escolha seu Jogo: ")
            print('[1] - Rainbow Six Siege') # steam://rungameid/359550
            print('[2] - Counter Strike Global Offensive') # steam://rungameid/730
            print('[3] - Valorant (Soon)')
            print('[4] - Driver Booster') # steam://rungameid/920490
            print('[5] - Surpresa')
            print('[6] - Exit')
            gameselect = int(input())
            if gameselect == 1:
                wb.open("steam://rungameid/359550")
            elif gameselect == 2:
                wb.open('steam://rungameid/730')
            elif gameselect == 3:
                print("Avalible soon")
            elif gameselect == 4:
                wb.open('steam://rungameid/920490')
            elif gameselect == 5:
                lista = ["steam://rungameid/359550", 'steam://rungameid/730','steam://rungameid/920490']
                c = rm.randint(0,2)
                wb.open(lista[c])
            elif gameselect == 6:
                quit()
            else:
                return -1

        elif select == 2:
            wb.open('https://www.google.com.br')
        else:
            os.system("cls")
            print("--**-- Opção inválida --**--")
            main()

    except:
        return -1
selection()