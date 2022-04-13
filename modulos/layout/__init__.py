import os
from time import sleep


def moldura():
    """
    Cria tracejados para separar assuntos
    :return: '-' repetido 50 vezes
    """
    print('-' * 50)


def titulo(frase):
    """
    Cria Titulos formatado para assuntos principais.
    :param frase: str Palavra
    :return: Palavra formatada
    """
    moldura()
    print(f'{frase:^50}')
    moldura()


def menu(opçoes):
    """
    Cria menu de opçoes com base na quantidade de elementos na lista
    :param opçoes: Lista com opções
    :return: Opçoes formatadas como menu numerico
    """
    contador = 1
    for elemento in opçoes:
        print(f'{contador} - {elemento}')
        contador += 1


def leiaInt(frase):
    """
    Lê valor inteiro e trata erros com valores float, str e interrupções
    :param frase: Frase para input de usúario
    :return: valor INTEIRO ou mensagem de erro
    """
    while True:
        try:
            nint = int(input(frase))
            return nint
        except (ValueError, TypeError):
            print('Erro. Digite uma opção válida.')
            sleep(1)
            continue
        except KeyboardInterrupt:
            print('Erro. Usuário interrompeu o programa')
            sleep(1)
            return 4
        except:
            print('Erro na escolha de opções')
            sleep(1)
            return 4


def limpar():
    """
    limpa terminal
    :return: Limpa terminal
    """
    os.system('cls')

