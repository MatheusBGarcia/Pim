# crie uma senha

senha_correta = input('Crie uma senha: ')
while True :
    senha = input('Digite a senha: ')
    if senha == senha_correta :
        print('Acesso liberado')
        break
    else:
        print('Senha incorreta, tente novamente')
#-----------------------------------------------------------------------------#


import os
import shutil
from datetime import datetime

diretorio_origem = '/caminho/do/diretorio/de/origem'
diretorio_destino = '/caminho/do/diretorio/de/destino'

if not os.path.exists(diretorio_destino):
    os.makedirs(diretorio_destino)

nome_arquivo_backup = 'backup_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.zip'

shutil.make_archive(os.path.join(diretorio_destino, nome_arquivo_backup), 'zip', diretorio_origem)

print(f'Backup criado com sucesso em {os.path.join(diretorio_destino, nome_arquivo_backup)}')
#-----------------------------------------------------------------------------#

import urllib
import urllib.parse

def verificar_url(url):
    try:
        resultado = urllib.parse.urlparse(url)
        if resultado.scheme not in ['http', 'https']:
            return False
        if resultado.netloc == '':
            return False
        return True
    except ValueError:
        return False
    
url = input("Digite a URL: ")
if verificar_url(url):
    print("URL válida")
else: 
    print("URL suspeita")
