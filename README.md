### Script para adicionar permissão de IP no Grupo de Segurança de uma instância EC2 no Amazon Web Services(EC2) ###

#### Pré-Requisitos ####  
- Python3
- Instalar o AWS Cli e configurar pelo aws configure --> https://docs.aws.amazon.com/pt_br/cli/latest/userguide/getting-started-install.html  
- Gerar um Access Key ID e Secret Access key para configuração do AWS Cli  
  - Configurar a região   
  - default output format: json  

#### Instalação ####  
- git clone https://github.com/tcheweb/aws-sg-add.git
- Renomeie o arquivo **instances_modelo.json** para **instances.json** e insira as VM´s com os respectivos Security Group Id´s  
- Execute o aws-sg-add.bat  

### Uso ###
Este script deve ser usado com crontab. Especifique a frequência
```bash
# ┌───────────── minut0 (0 - 59)
# │ ┌───────────── hora (0 - 23)
# │ │ ┌───────────── dia do mês (1 - 31)
# │ │ │ ┌───────────── mês (1 - 12)
# │ │ │ │ ┌───────────── dia da semana (0 - 6) (Domingo até Sábado 7 pode ser Domingo em alguns sistemas)
# │ │ │ │ │ ┌───────────── comando para executar                               
# │ │ │ │ │ │
# │ │ │ │ │ │
# * * * * * /bin/bash {local do script}
```
#### Contribuições ####
Pull requests são bem vindos. Para mudanças grandes, abra uma Issue primeiro para avaliarmos o que você deseja mudar.
