###   Script para adicionar permissão de IP no Grupo de Segurança de uma instância EC2 no Amazon Web Services(AWS) ##
###   Versão 3.0.0
###   Adriano Baumart
###   Criação: 22/09/2022    ###   Atualizado: 28/09/2022
import os
import json
import requests

# Lendo lista de Instâncias
try:
    with open('instances.json') as file:
        instances = json.load(file)

except:
    print('ERRO! O arquivo instances.json não pôde ser lido!')
    exit()

# Pegando o endereço IP válido
try:
    url = 'https://checkip.amazonaws.com/'
    checkip = requests.get(url)
    meuip = str(checkip.text).strip()

except:
    print('Não foi possível obter seu endereço IP!')
    meuip = 'IP NÃO ENCONTRADO'

print('-' * 55)
print('### PERMISSÕES EM GRUPOS DE SEGURANÇA EC2 - AWS ####')
print('-' * 55)

sgs = list()

ip = str(input(f'Informe o endereço IP (ENTER para {meuip}): '))
if ip == '':
    ip = meuip

# Menu de Instãncias
print(f'SELECIONE A INSTÂNCIA QUE DESEJA LIBERAR ACESSO:')

for cod, item in enumerate(instances['instances']):
    # Lista as instâncias
    print(f'[ {cod} ]  [{item["instance"]}]')
print('[999]  [Sair]')

while True:
    try:
        sg = int(input('Código da Instância: '))

    except ValueError:
        print(f'ERRO! Digite um número!')
    else:
        if sg == 999:
            break
        for codigo, valor in enumerate(instances['instances']):
            # insere a instância na lista de liberação. Se o número digitado não existir, ignora.
            if codigo == sg:
                sgs.append(valor['sg_id'])


while True:
    print('!' * 40)
    confirma = str(input(f'CONFIRMA A LIBERAÇÃO DO IP {ip}? [S/N]: ').upper().strip())
    if confirma == 'S':
        # Inicia a execução do comando.
        os.system('cls')
        print('Iniciando...')
        for item in sgs:
            comando = f'aws ec2 authorize-security-group-ingress --group-id {item} --protocol tcp --port 22 --cidr {ip}/32 > response.json'
            # executa e grava o retorno no arquivo response.json
            os.system(comando)

            # validação da execução
            # verifica se o retorno foi gravado no arquivo response.json
            try:
                with open('response.json') as file:
                    retorno = json.load(file)

                if retorno['Return']:
                    # Recebeu um Json com a confirmação de sucesso.
                    print(f'IP Liberado com sucesso!')
                else:
                    # Não foi gravado nada no arquivo de retorno.
                    print('Falha ao autorizar acesso!')
            except:
                # não encontrou o arquivo
                print('Arquivo response.json não encontrado!')
        break

    elif confirma == 'N':
        # Não confirmou a autorização.
        print('Finalizado.')
        break
    else:
        # Digitou algo diferente de S ou N
        print('Opção inválida!')
