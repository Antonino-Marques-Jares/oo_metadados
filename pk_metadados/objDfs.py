import importlib
import json
import os
from pathlib import Path
import pandas as pd
from pk_metadados.objTabela import Tabela

def extrair_informacoes_do_artefato_json(in_path: str):
    """
    Extrai informações de um arquivo JSON de artefato
    
    Args:
        in_path (str): Caminho para o arquivo JSON
        
    Returns:
        dict: Dicionário com as informações do artefato
    """
    path = Path(in_path)
    with path.open(encoding='utf-8') as file:
        info = json.load(file)
    return info

def dfs(in_diretorio: str):
    """
    Processa todos os artefatos em um diretório e retorna um DataFrame consolidado
    
    Args:
        in_diretorio (str): Diretório base contendo as camadas
        
    Returns:
        pd.DataFrame: DataFrame consolidado com todas as informações
    """
    camadas = os.listdir(in_diretorio)
    caminhos_todos_artefatos = []
    for camada in camadas:
        for caminho_do_artefato in os.listdir(f"artefatos/{camada}"):
            caminhos_todos_artefatos.append(
                f"artefatos/{camada}/{caminho_do_artefato}"
            )
    lista_tabelas = []
    for artefato in caminhos_todos_artefatos:
        infos = extrair_informacoes_do_artefato_json(artefato)
        meta_tabela = Tabela()
        meta_tabela.load_from_artefato(infos)
        meta_tabela.calcula_camada()
        meta_tabela.converte_colunas_em_objetos()
        lista_tabelas.append(meta_tabela)

    todos_dfs = []
    for objeto_tabela in lista_tabelas:
        df = objeto_tabela.converte_para_dataframe()
        todos_dfs.append(df)

    return pd.concat(todos_dfs)