
"""
Pacote Metadados
"""
# Importa funções para disponibilizar diretamente no pacote
from .objTabela import Tabela  
from .objTabela import Coluna 
from .objDfs import dfs, extrair_informacoes_do_artefato_json

__all__ = ['Tabela', 'Coluna', 'dfs', 'extrair_informacoes_do_artefato_json']  # Opcional: controla o que é exportado