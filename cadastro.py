from modulos.layout import *  # funçoes relacionadas ao layout do programa
from modulos.manipula_arquivos import *  # funçoes relacionadas à manipulação de arquivos no programa
from time import sleep
import sys

while True:  # Laço infinito do cadastro de equipamento
    titulo('Cadastro de peças')  # Função para criação de títulos principais
    equipamento = str(input('Nome do Equipamento: '))
    moldura()  # Função para criar separadores
    limpar()  # limpa o terminal
    if not arquivoExiste(equipamento):  # verifica se o arquivo existe retorna TRUE ou FALSE
        print(f'O cadastro de {equipamento} não existe.')
        sleep(1)  # tempo para leitura de erros e mensagens de status
        titulo(f'OPÇÕES para {equipamento}')
        menu(['Realizar Cadastro', 'Cancelar Consulta', 'Fechar Programa'])  # Função para criação de menus
        moldura()
        # Lê numeros inteiros e retorna erro se valor digitado for Float ou String
        resposta = leiaInt('Digite a opção desejada: ')
        if resposta == 3:
            sleep(1)
            titulo('Muito Obrigado, até logo!')
            sys.exit()  # fecha programa
        elif resposta == 2:
            moldura()
            print('Retornando para nova consulta!')
            sleep(1)
            limpar()
            continue  # Retorna ao início do programa
        elif resposta == 1:
            criarArquivo(equipamento)  # Cria um arquivo TXT com o nome do equipamento
        else:  # Retorna erro para opçoes diferentes das diponiveis
            print('ERRO. Opção inválida.')
            sleep(1)
            limpar()
            continue  # Retorna ao início do programa
    else:
        print('Cadastro encontrado...')
        sleep(1)
    while True:  # Laço do cadastro de peças
        titulo(f'OPÇÕES para {equipamento}')
        menu(['Cadastrar Peças', 'Visualizar Peças', 'Trocar equipamento', 'Sair'])
        moldura()
        resposta = leiaInt('Digite a Opção desejada: ')
        if resposta == 1:
            limpar()
            titulo(f'Cadastro de peças para {equipamento}')
            nome_peça = str(input('Nome da peça: '))
            codido_peça = leiaInt('Codigo da Peça: ')
            # Cadastra nome e codigo de peça em um TXT
            cadastroPeças(equipamento, nome_peça, codido_peça)
            limpar()
        elif resposta == 2:
            limpar()
            titulo(f'Lista de Peças {equipamento}')
            lerArquivo(equipamento)  # Retorna lista de cada linha do TXT e cria uma tabela com os cadastros
            voltar = leiaInt('Digite 0 para voltar: ')
            while True:  # Laço para interromper a visualização da tabela
                if voltar == 0:
                    limpar()
                    break
                else:
                    print('Erro. Para voltar digite 0.')
        elif resposta == 4:
            titulo('Muito Obrigado e até logo')
            sys.exit()  # Fecha programa
        # Retorna erro carro uma opção diferente das disponiveis for digitada
        elif resposta < 0 or resposta > 4:
            limpar()
            print('Erro. Digite uma opção valida')
            sleep(1)
            continue
        elif resposta == 3:
            limpar()
            print('Retornando para nova consulta!')
            sleep(1)
            break
    if resposta == 3:
        continue  # Retorna ao inicio do programa
