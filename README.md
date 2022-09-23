### Script para adicionar permissão de IP no Grupo de Segurança de uma instância EC2 no Amazon Web Services(EC2) ###

#### Pré-Requisitos ####  
- Python3
- Instalar o AWS Cli e configurar pelo aws configure --> https://docs.aws.amazon.com/pt_br/cli/latest/userguide/getting-started-install.html  
- Gerar um Access Key ID e Secret Access key para configuração do AWS Cli  
  - Configurar a região   
  - default output format: json  

#### Instruções ####  
- Renomeie o arquivo **instances_modelo.json** para **instances.json** e insira as VM´s com os respectivos Security Group Id´s  
- Execute o aws-sg-add.bat  


#### Release Notes ####

1.2.1 - 2022-09-23
- Remoção de exibição destinada a debug.  
- 

2.0.0 - 2022-09-23  
- Modificada a lista de VM´s. Agora consulta por um arquivo json separado do código.  
  
1.0.0 - 2022-09-22  
- Primeira versão  