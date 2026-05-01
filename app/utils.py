import json
import os
from pathlib import Path
import os


caminho_script = os.path.abspath(__file__)
pasta_app = os.path.dirname(caminho_script)
pasta_raiz = os.path.dirname(pasta_app)
caminho_json = os.path.join(pasta_raiz, 'certificados.json')

def carregar_certificados():

    with open(caminho_json,'r') as file:

        data=json.load(file) 

        return data








