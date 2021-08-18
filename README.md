# getInformation
Este repositório tem como o propósito obter as informações de uma instância, VPC, Sg, Route Tables e Nacl.

A estrutura das pastas está organizada da seguinte maneira:

-> app/             - Diretório principal para a aplicação 
    -> src/         - Diretório com a logica de negócio 
    -> tests/       - Diretório para testes unitários futuros

-> lambda/          - Diretório para futuramente será adicionada uma lambda funcion que irá acionar a aplicação

-Modo de usar:

Dentro do diretório, execute o arquivo app/src/getInformation.py.

-Requisitos:
Você precisa já ter configurado em seu ambiente o AWS CLI com a access key.
Instalar a biblioteca boto3 com o seguinte comando:

python -m pip install boto3

Obs:
A região default onde será feita a busca é us-east-1. Para alterar a região
é necessário editar o arquivo app/src/getInformation.py e na variável global
REGION_NAME colocar a região desejada.: Ex REGION_NAME = 'sa-east-1'