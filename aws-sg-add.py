## Script para adicionar permissão de IP no Grupo de Segurança de uma instância EC2 no Amazon Web Services(AWS) ##
## Versão 2.0.0
## Adriano Baumart
## Data: 22/09/2022
import os
import json
import requests
file = open('instances.json')
instances = json.load(file)
file.close()
sgs = list()

# Pegando o endereço IP válido
url = 'https://checkip.amazonaws.com/'
checkip = requests.get(url)
meuip = str(checkip.text)

print('-' * 55)
print('### PERMISSÕES EM GRUPOS DE SEGURANÇA EC2 - AWS ####')
print('-' * 55)
print(f'Meu IP: {meuip}')
ip = str(input(f'Informe o IP (ENTER para meu IP): '))
if ip == '':
    ip = meuip

print(f'SELECIONE A INSTÂNCIA QUE DESEJA LIBERAR ACESSO:')
for cod, item in enumerate(instances['instances']):
    # Lista as instâncias
    print(f'[ {cod} ]  [{item["instance"]}]')
print('[999]  [Sair]')
while True:
    sg = int(input('Código da Instância: '))
    if sg == 999:
        break
    for codigo, valor in enumerate(instances['instances']):
        # insere a instância na lista de liberação
        if codigo == sg:
            sgs.append(valor['sg_id'])
print('!' *40)
while True:
    confirma = str(input(f'CONFIRMA A LIBERAÇÃO DO IP {ip}? [S/N]: ').upper().strip())
    if confirma == 'S':
        os.system('cls')
        print('Iniciando...')
        for item in sgs:
            comando = f'aws ec2 authorize-security-group-ingress --group-id {item} --protocol tcp --port 22 --cidr {ip}/32'
            os.system(comando)
            print('CONCLUÍDO')
        break
    elif confirma == 'N':
        break
    else:
        print('Opção inválida!')
