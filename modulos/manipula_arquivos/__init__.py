from time import sleep


def arquivoExiste(nome):
    """
    Verifica se arquivo TXT existe
    :param nome: nome do arquivo
    :return: TRUE ou FALSE
    """
    try:
        a = open(nome, 'rt')
        a.close()

    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """
    Cria arquivo TXT
    :param nome: nome do arquivo TXT
    :return:
    """
    try:
        a = open(nome, 'a')
        a.close()
    except:
        print('Erro ao Criar Arquivo')
        sleep(1)
    else:
        print('Arquivio criado com sucesso')
        sleep(1)


def cadastroPeças(arq, nome='<Não Identificado>', codigo=0):
    """
    Escreve cadastro em arquivo TXT
    :param arq: nome do arquivo TXT
    :param nome: nome da peça a ser cadastrada
    :param codigo: codigo da peça a ser cadastrada
    :return:
    """
    try:
        a = open(arq, 'at')
    except:
        print('ERRO. Falha ao abrir o arquivo.')
        sleep(1)
    else:
        try:
            a.write(f'{nome};{codigo}\n')
        except:
            print('Erro ao cadastrar peça.')
            sleep(1)
        else:
            print('Peça cadastrada com sucesso!')
            sleep(1)


def lerArquivo(nome):
    """
    Cria lista com cada elementos das linhas do arquivo TXT
    :param nome: nome do arquivo TXT.
    :return: tabela com peças e codigos cadastrados
    """
    try:
        a = open(nome, 'rt')
    except:
        print('\033[1;101mErro ao ler o Arquivo\033[m')
        sleep(1)
    else:
        try:
            print(f'{"<PEÇA>":<30}{"<CODIGO>":<10}')
            for linha in a:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:.<30}{dado[1]:>8}')
        except:
            print('\033[1;101mERRO. Nunhuma peça cadastrada.\033[m')
            sleep(1)
    finally:
        a.close()
