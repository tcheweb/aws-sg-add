### Script para liberação de IP em Grupos de Segurança de Instâncias EC2 ###

**Pré-Requisitos**  
    - Python3  
    - Instalar o AWS Cli e configurar pelo aws configure --> https://docs.aws.amazon.com/pt_br/cli/latest/userguide/getting-started-install.html  
        - Gerar um Access Key ID e Secret Access key para configuração do AWS Cli  
        - Configurar a região   
        - default output format: json  

**Instruções**  
- Renomeie o arquivo instances_modelo.json para instances.json e insira as VM´s com os respectivos Security Group Id´s  
- Execute o aws-sg-add.bat  