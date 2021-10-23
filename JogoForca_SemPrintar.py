import random
import time
import csv
import unidecode
import emoji
import os

# Função de boas vindas


def boasVindas():
    print(" "*33, "#"*32)
    print(" " * 33, "*  Bem-vindo ao Jogo da Forca  *")
    print(" "*33, "#"*32)
    print("""
Descrição do Jogo: é um jogo em que o jogador tem que acertar qual é a palavra proposta, tendo como dica 
o número de letras. A cada letra errada, é desenhado uma parte do corpo do enforcado. Quando estiverem
faltando 2 erros para que o jogo acabe, o jogador recebe uma dica com o tema da palavra. O jogo termina 
ou com o acerto da palavra ou com o término do preenchimento das partes corpóreas do enforcado.""")

# Função desenha forca


def desenhaForca(erros, txt):
    cabeca = "(*_*)"
    corpo = "|"
    bracoE = "/|"
    bracoD = "\\"
    pernaE = "/"
    pernaD = " \\"
    print("  _______\n |       |")
    print(" |      ___" if erros > 0 else " | ")
    print(f" |     {cabeca}" if erros > 0 else " | ")
    print(f" |      {bracoE}" if erros > 2 else " | ", end="")
    print(f"      {corpo}" if erros == 2 else "", end="")
    print(bracoD if erros > 3 else "")
    print(f" |       {corpo}" if erros > 1 else " | ")
    print(f" |      {pernaE}" if erros > 4 else " | ", end="")
    print(pernaD if erros > 5 else "")
    print(f" |\n |\n_|___ {' '*10} {txt}\n")

# Função dica


def dica(dicionario, palavra):
    for chave, valor in dicionario.items():
        if palavra in valor:
            return chave

# Função resultado


def resultado(erros):
    if erros < 6:
        print(" 🏆🎉🍾 Parabéns! Você descobriu a palavra! 🏆🎉🍾")
        print("               ___________")
        print("               .=_=_=_=_=.")
        print("               -\\       /-")
        print("              |(|:.     |)|")
        print("               -|:.     |-")
        print("                \\::.    /")
        print("                  ::. .")
        print("                   ) (")
        print("                 _.' '._")
        print("                '======='\n")
    else:
        print("😭😭😭 Infelizmente não foi dessa vez. Tente novamente! 😭😭😭\n")
        print(f"A palavra era \"{sorteada}\".\n")


# Inicio do Jogo
boasVindas()

# Lê o arquivo csv com as palavras, armazena em um dicionério (chave = categoria, valor = lista de palavras)
with open('ListaPalavras.csv', mode='r', encoding='utf-8') as arquivo:
    reader = csv.reader(arquivo)
    dicionarioPalavras = {lista[0]: lista[1:] for lista in reader}

# Lista com todas as palavras para sortear
listaPalavras = [palavra for lista in dicionarioPalavras.values()
                 for palavra in lista]

iniciar = input("\nVamos iniciar o jogo? (Sim ou Não) ").lower()

if iniciar == "sim":
    print("\nÓtimo! Sorteando a palavra... ")
    time.sleep(2)
    sorteada = random.choice(listaPalavras).lower()  # Sorteia a palavra
    print(sorteada)
    txt = "___ " * len(sorteada) # Variável que armazena os traços para indicar quantas letras tem a palavra
    erros = 0

    desenhaForca(erros, txt)
    tentativas_letras = []  # Lista para armazenas todas as tentativas de letras

    while erros < 6 and ("___" in txt):

        letra = input("Digite uma letra: ").lower()

        if not letra.isalpha() or len(letra) > 1:  # Verifica se é uma letra, ou mais de uma letra
            os.system('cls||clear')
            desenhaForca(erros, txt)
            print("\nEntrada inválida.")
            print(f"Letras que você já tentou: {', '.join(tentativas_letras)}\n")
            continue

        if unidecode.unidecode(letra) in tentativas_letras: # Verifica se a letra é repetida
            os.system('cls||clear')
            desenhaForca(erros, txt)
            print("\nLetra repetida! Tente novamente.")
            print(f"Letras que você já tentou: {', '.join(tentativas_letras)}\n")
            continue

        tentativas_letras.append(letra)  # Adiciona a letra à lista

        if letra in unidecode.unidecode(sorteada): # Verifica se a letra está na palavra
            os.system('cls||clear')
        
            for i, item in enumerate(sorteada):
                if unidecode.unidecode(item) == letra:
                    txt = txt[:4*i] + " " + item + " " + \
                        txt[(4*i + 3):]  # Substitui os traços pela letra

            desenhaForca(erros, txt)
            print(f"\nA letra {letra} está na palavra. \n")
            print(f"Letras que você já tentou: {', '.join(tentativas_letras)}\n")

        else:
            os.system('cls||clear')
            erros += 1
            desenhaForca(erros, txt)
            print(f"A letra {letra} não está na palavra. \n")
            print(
                f"Letras que você já tentou: {', '.join(tentativas_letras)}\n")

            # Quando erros = 4, chamamos a função dica, que mostrará a categoria da palavra sorteada
            if erros == 4:
                dica = dica(dicionarioPalavras, sorteada)
                if dica == "fruta" or dica == "cidade" or dica == "profissão":
                    print("\nVocê só pode errar mais duas vezes.",
                          f"\nAqui vai uma dica: a palavra sorteada é uma {dica}.\n")
                else:
                    print("\nVocê só pode errar mais duas vezes.",
                          f"\nAqui vai uma dica: a palavra sorteada é um {dica}.\n")

    resultado(erros)  # Ao final do loop while, mostra o resultado.

elif iniciar == unidecode.unidecode("não"):
    print("\nAté a próxima.")
else:
    print("\nOpção inválida.")
# Fim do jogo
