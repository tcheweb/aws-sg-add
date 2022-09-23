## Script para adicionar permissão de IP no Grupo de Segurança de uma instância EC2 no Amazon Web Services(AWS) ##
## Versão 1.2.1
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
meuip = requests.get(url)

print('-' * 50)
print('###PERMISSÕES EM GRUPOS DE SEGURANÇA EC2 - AWS####')
print('-' * 50)
print(f'Seu IP é: {meuip.text}')
ip = str(input('Informe o endereço IP: '))

print(f'SELECIONE A INSTÂNCIA QUE DESEJA LIBERAR ACESSO:')
for cod, item in enumerate(instances['instances']):
    # Lista as instâncias
    print(f'[ {cod} ]  {item["instance"]}')

while True:
    sg = int(input('Código da Instância[ 999 para sair ]: '))
    if sg == 999:
        break
    for codigo, valor in enumerate(instances['instances']):
        # insere a instância na lista de liberação
        if codigo == sg:
            sgs.append(valor['sg_id'])
print('!' *35)
confirma = str(input('CONFIRMA A LIBERAÇÃO DO IP? [S/N]: ').upper().strip())
if confirma == 'S':
    os.system('cls')
    print('Iniciando...')
    for item in sgs:
        comando = f'aws ec2 authorize-security-group-ingress --group-id {item} --protocol tcp --port 22 --cidr {ip}/32'
        os.system(comando)
        print('IP autorizado com sucesso!')
